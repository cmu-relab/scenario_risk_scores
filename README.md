# Replication Package


## Coding
The coding/ folder contains the datasets used to develop and evaluate the coding frame, including:

* Round 1: sample1-rater1.json, sample1-rater2.json - the initial sample of 10 scenarios coded by two raters to identify information types; the coding frame for sub-codes simple, complex and question types was discovered by analyzing disagreements in this dataset
* Round 2: sample2-rater1.json, sample2-rater2.json - a second sample used to evaluate the coding frame for simple, complex and question types
* Round 3: sample2-rater1-reann.json, sample2-rater2-reann.json - the second sample re-annotated after discussing disagreements using the new coding frame
* Round 4: sample3-rater1.json, sample3-rater2.json - a third sample used to evaluate the raters refined understanding of the new coding frame

**Notebooks**

* Interrater Relability - computer Cohen's Kappa for each of the four rounds of annotation labels provided by the two raters

## Datasets
The datasets/ folder contains the original datasets used for training and evaluation of the named entity recognizer (NER) model, including:

* scenarios-general.json - contains 100 scenarios collected from users without a specific focus on privacy
* scenarios-privacy.json - contains 200 scenarios collected from users with a focus on privacy
* scenarios-labeled.json - contains the 300 total scenarios from the general and privacy datasets, annotation labels for the simple, complex and question information type phrases.

**Notebooks**

* Scenario Summary - summarizes frequencies describing the number of apps
* Prediction Post-Processing - investigates the use of post-processing to improve overall precision by removing false positives from the NER model prediction output.

## Models


## Surveys
The surveys/ folder contains the survey forms used to elicit scenarios and privacy risk scores from users, including:

* survey_page1.pdf - the formative survey to ask questions about personal data collected by the app, a step to redact and upload a screenshot of the app, and to answer questions about the screenshot, before authoring a scenario about the screenshot.

* survey_page2.pdf - the summative survey that presents the user-authored scenario to the user with highlighted information types and asks the user to score the types for privacy risk. This survey page is an example populated with a hypothetical survey to illustrate what a user sees.


