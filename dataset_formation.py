import pandas as pd
import csv

# dataset ref1: - https://www.kaggle.com/narendrageek/mental-health-faq-for-chatbot
# dataset ref2: - https://www.kaggle.com/abbbhishekkk/faq-datasets-for-chatbot-training        

data1 = pd.read_json("Aadhar_Faq.json")
data2 = pd.read_json("Amazon_sagemaker_Faq.json")
data3 = pd.read_json("faq_results.json")
data4 = pd.read_json("HDFC_Faq.json")
data5 = pd.read_json("Sevenhillshospital_faq.json")
data6 = pd.read_json("Tata_comm_faq.json")

Qs = []

for i in data1.question:
    Qs.append(i)   

for i in data2.question:
    Qs.append(i) 

for i in data3.Question:
    Qs.append(i) 
   
for i in data4.question:
    Qs.append(i) 
    
for i in data5.question:
    Qs.append(i)     

for i in data6.question:
    Qs.append(i)  

#len(Qs)

As = []

for i in data1.answer:
    As.append(i)  

for i in data2.answer:
    As.append(i) 

for i in data3.Answer:
    As.append(i) 
    
for i in data4.answer:
    As.append(i) 
  
for i in data5.answer:
    As.append(i)     

for i in data6.answer:
    As.append(i) 
    

#len(As)

new_df = pd.DataFrame({'Questions': Qs, 'Answers': As})

#new_df.head()
print("new_df.shape: ", new_df.shape)

new_df.to_csv('final_dataset.csv', index = False)

final_df = pd.read_csv("final_dataset.csv")

print("final_df.shape: ", final_df.shape)

#final_df.head()

#final_df["Questions"]
