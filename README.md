# Reasoning-Using-Link-Prediction---Mini-Project

The aim was to try and find a way to use the concept of "Link Prediction" to perform reasoning between a person(user) and an automated AI to respond in a meaningful manner.

**Programming Language** - Python 3

## Concepts Used - 

1. **TFIDF** - Term Frequency Inverse Document Frequency
2. **Cosine Similarity**

## Steps to execute (and understand the working of the project with the concepts used) - 

1. The _**'initial_code_hardcoded_concepts.ipynb'**_ shows the initial work and also the usage of the above listed concepts without the use of any special Python libraries which have the above listed concepts in pre-defined python libraries such as,
   - **cosine_similarity**
   - **TfidfVectorizer** 
2. Download the **'.json'** files.
3. Run the _**'dataset_formation.py'**_ file.
4. You will observe the _**'final_dataset.csv'**_ file is created.
5. Run the _**'mini_project_final_code.py'**_ file.
6. You will observe that two _**'pickle'**_ files will be created - vectorizor and training matrix
7. In the _**command prompt or terminal**_ you will observe the following,
   - The first 5 rows of the dataset.
   - The total rows of the dataset - Q/A count
   - The passed and failed test cases
   - Accuracy

### Visit the _"mini_project_report_AUG_DEC_2020.pdf"_ for the detailed report of the mini-project.

## Datasets:

1. Aadhar_Faq.json
2. Amazon_sagemaker_Faq.json
3. faq_results.json
4. HDFC_Faq.json
5. Sevenhillshospital_faq.json
6. Tata_comm_faq.json

## Dataset Reference Links:

- *Dataset ref1*: - https://www.kaggle.com/narendrageek/mental-health-faq-for-chatbot
- *Dataset ref2*: - https://www.kaggle.com/abbbhishekkk/faq-datasets-for-chatbot-training 
