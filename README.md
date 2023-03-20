# Replication Package

The following notebooks were run using Anaconda 4.12.0 with additional package installs as needed. To train an existing model, we recommend starting in the models/ folder, described below.

## Coding
The coding/ folder contains the datasets used to develop and evaluate the coding frame, including:

* Round 1: round1-sample1-rater1.json, round1-sample1-rater2.json - the initial sample of 10 scenarios coded by two raters to identify information types; the coding frame for sub-codes simple, complex and question types was discovered by analyzing disagreements in this dataset
* Round 2: round2-sample2-rater1.json, round2-sample2-rater2.json - a second sample used to evaluate the coding frame for simple, complex and question types
* Round 3: round3-sample2-rater1-reann.json, round3-sample2-rater2-reann.json - the second sample re-annotated after discussing disagreements using the new coding frame
* Round 4: round4-sample3-rater1.json, round4-sample3-rater2.json - a third sample used to evaluate the raters refined understanding of the new coding frame

**Notebooks**

* Interrater Relability - used to compute Cohen's Kappa for each of the four rounds of annotation labels provided by the two raters

## Datasets
The datasets/ folder contains the datasets used for training and evaluation of the named entity recognition (NER) models, including:

* scenarios-labeled.json - contains the 300 total scenarios with original annotation labels for the simple, complex and question information type phrases. The original labels can overlap, e.g., where a complex phrase includes a simple phrase.
* scenarios-training-X.json - contains the 300 scenarios with non-overlapping labels. Each file for X in [0, 9] contains training, validation and test splits at 90, 10 and 10%, respectively.
* scenarios-risked.json - contains 203 scenarios collected from users, including privacy risk scores for information types predicted using a BERT-based model trained on scenarios-training-0.json.
* app-url-dictionary.json - contains a mapping from mobile app URL to the app name and app store category.

**Notebooks**

* Scenario-Level Dataset Preparation - used to split the scenarios-labeled.json data into train, validate and test sets to yield the the scenarios-training-X.json files for X in [0, 9].
* Sentence-Level Dataset Preparation - used to split the scenarios-labeled.json data into train, validate and test sets to yield the the sentences-training.json file.
* Prediction Post-Processing - investigates the use of post-processing to improve overall precision by removing false positives from the NER model prediction output.
* Summary of Authored Scenarios - used to summarize the data in the scenarios-labeled.json file.
* Summary of Risk Survey Results - used to summarize the data in the scenarios-risked.json file.

## Models
The models/ folder contains the notebooks used to train and evaluate the BERT-based and CRF-based NER model, including:

* BERT-based NER Training - used to train and evaluate the BERT-based NER model. Includes the sklearn.metrics and seqeval.metrics reports.
* CRF NER Training and Testing - used to train and evaluate the CRF-based NER model. Includes the function setup the features, and the sklearn.metrics and seqeval.metrics reports.

## Surveys
The surveys/ folder contains the survey forms used to elicit scenarios and privacy risk scores from users, including:

* survey_page1.pdf - the formative survey to ask questions about personal data collected by the app, a step to redact and upload a screenshot of the app, and to answer questions about the screenshot, before authoring a scenario about the screenshot.
* survey_page2.pdf - the summative survey that presents the user-authored scenario to the user with highlighted information types and asks the user to score the types for privacy risk. This survey page is an example populated with a hypothetical survey to illustrate what a user sees.



