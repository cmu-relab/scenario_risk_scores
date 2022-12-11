import sys, json, random, os

# read scenarios indexed by scenario_id
def read_data(filename):
    data = {}
    lines = open(filename, 'r').readlines()
    for i in range(len(lines)):
        if lines[i].startswith('https'):
            continue
        if lines[i].startswith('MAS'):
            # initialize the scenario data dictionary
            scenario_id = lines[i][0:lines[i].index(':')]
            data[scenario_id] = {'scenario_id': scenario_id}
            
            # read the scenario text
            text = [lines[i][lines[i].index(':')+1:].strip()]
            i += 1
            while i < len(lines) and not lines[i].startswith('https'):
                text.append(lines[i])
                i += 1
            data[scenario_id]['text'] = ' '.join(text)
        i += 1
    # print(data)
    return data

# randomly sample raw data
def read_raw_sample(filename, sample_size, dest):
    data = ""
    f = open(filename, 'r')
    jlist = json.load(f)
    sample_size = min(len(jlist), sample_size)
    sample_list = random.sample(jlist, sample_size)
    for sample in sample_list:
        data += sample["app_url"] + "\n" + sample['scenario_id'] + ": " + sample["text"] + "\n\n"
    if not os.path.exists(dest):
        with open(dest, 'w') as f:
            f.write(data)


# convert coded scenarios into code sequences per word
import spacy
nlp = spacy.load("en_core_web_sm")

def parse_codes(text):
    # build map containing offsets
    offsets = []
    scores = []
    clean_text = ''
    skip = 0
    for i in range(len(text)):
        if skip > 0:
            skip -= 1
            continue
        elif text[i] == '|':
            code = clean_text[-1]
            clean_text = clean_text[:-1]
            offsets.append((code, len(clean_text)))
        elif text[i] == '[':
            # scores.append(text[i+1])
            offsets.append(('[', len(clean_text)))
            skip = 0
            inside = True
        elif text[i] == ']':
            offsets.append((']', len(clean_text)))
            inside = False
        else:
            clean_text += (text[i])

    # tokenize the words sequence
    words = []
    codes = []
    i = 0
    inside = False
    for token in nlp(clean_text):
        if i < len(offsets) and token.idx >= offsets[i][1]:
            if offsets[i][0] == '[':
                words.append(str(token))
                codes.append('b-i')
                inside = True
            elif offsets[i][0] == ']':
                words.append(str(token))
                codes.append('o')
                inside = False
            else:
                words.append(str(token))
                codes.append('b-' + offsets[i][0])
            i += 1
        elif inside:
            words.append(str(token))
            codes.append('i-i')
        else:
            words.append(str(token))
            codes.append('o')
                
    return clean_text, words, codes, scores

def read_and_parse_data(filename):
    scenarios = read_data(filename)
    for scenario_id, data in scenarios.items():
        clean_text, words, codes, scores = parse_codes(data['text'])
        data['clean_text'] = clean_text
        data['words'] = words
        data['codes'] = codes
        data['scores'] = scores
    return scenarios

def is_consistent(data1, data2):
    # check scenario ids match between datasets
    id1 = set(data1.keys()) - set(data2.keys())
    id2 = set(data2.keys()) - set(data1.keys())
    if len(id1) != len(id2) and len(id1) != 0:
        print('Scenario ID mismatch:\t%s\t%s' % (id1, id2))
    else:
        print('Scenario IDs matched.')

    # for matching scenario ids, check words match
    id_match = set(data1.keys()).intersection(set(data2.keys()))
    for scenario_id in id_match:
        words1 = data1[scenario_id]['words']
        words2 = data2[scenario_id]['words']
        for i, (w1, w2) in enumerate(zip(words1, words2)):
            if w1 != w2:
                print('%s != %s' % (w1, w2))
                region1 = words1[max(0, i-5): min(len(words1), i+5)]
                region2 = words2[max(0, i-5): min(len(words1), i+5)]
                print('%s: Word misalignment at word index %i' % (
                    scenario_id, i))
                print('Region1: %s' % region1)
                print('Region2: %s' % region2)
                break

def main(args):
    text = 'This is a g|test [1 scenario]. This is a [2 second sentence].'
    print('Text: %s' % text)
    clean_text, words, codes, scores = parse_codes(text)
    for word, code in zip(words, codes):
        print('%s\t%s' % (word, code))
    print(scores)
    
if __name__ == '__main__':
    main(sys.argv)

