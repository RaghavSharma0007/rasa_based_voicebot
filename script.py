import pandas as pd
import numpy as np
import json, sys
import pandas as pd
from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config
import os
import statistics 
path = sys.argv[1]
file_name = sys.argv[2]
accuracy_intent=[]
accuracy_entity=[]
training_data = load_data("Test/Train_Data/output.json")
trainer = Trainer(config.load("Test/Config/config.yml"))
interpreter = trainer.train(training_data)
model_directory = trainer.persist("Test/models/nlu", fixed_model_name="current")
entity_rows= []
intent_rows= []

with open(path+file_name) as json_file:  
    data = json.load (json_file)
    data_extracted = data["rasa_nlu_data"]['common_examples']
    
    
for i in range(0,len(data_extracted)):
    actual_intent = data_extracted[i]['intent']
    actual_entity = data_extracted[i]['entities']
    phrase= data_extracted[i]['text'].lower()
    resp= interpreter.parse(phrase)
    detected_entities= resp['entities']
    detected_entity_confidence= ''
    x = (len(resp['entities']))
    detected_intent = resp['intent']['name']
    detected_intent_confidence= float(resp['intent']['confidence'])
    
    if (actual_intent.lower() == detected_intent.lower() ):
        intent_status="Correct"
        row_intent = [phrase,actual_intent,detected_intent,detected_intent_confidence,intent_status]
        intent_rows.append(row_intent)
        if (detected_entities == []):
            accuracy_intent.append(detected_intent_confidence)
        else:
            accuracy_intent.append(detected_intent_confidence)
            for j in range(x):
                actual_entity = data_extracted[i]['entities'][j]['value']
                detected_entity = resp['entities'][j]['value']
                entity_name=data_extracted[i]['entities'][j]['entity']
                detected_entity_confidence = float(resp['entities'][j]['confidence'])
                actual_entity=actual_entity.replace(" ","")
                detected_entity=detected_entity.replace(" ","")
                if (actual_entity.lower()==detected_entity.lower()):
                    entity_status="Correct"
                    accuracy_entity.append(detected_entity_confidence)
                    entity_row = [phrase,entity_name,actual_entity,detected_entity,detected_entity_confidence,entity_status]
                    entity_rows.append(entity_row)
                else:
                    entity_status="Wrong"
                    detected_entity_confidence=0
                    accuracy_entity.append(detected_entity_confidence)
                    entity_row = [phrase,entity_name,actual_entity,detected_entity,detected_entity_confidence,entity_status]
                    entity_rows.append(entity_row)
                j =+ 1
               
    else:
        
        intent_status="Wrong"
        detected_intent_confidence=0
        accuracy_intent.append(detected_intent_confidence)
        row_intent = [phrase,actual_intent,detected_intent,detected_intent_confidence,intent_status]
        intent_rows.append(row_intent)
        i += 1

accuracy_intent=statistics.mean(accuracy_intent)
accuracy_entity=statistics.mean(accuracy_entity)
row_intent = ["","","Accuracy:",accuracy_intent,""]
entity_row = ["","","","Accuracy",accuracy_entity,""]
intent_columns = ["Input","Actual Intent","Detected Intent","Detected Intent Confidence","Intent Status"]        
entity_columns = ["Input","Entity Name","Actual Entity","Detected Entity","Detected Entity Confidence","Entity Status"]        
intent_matrix = pd.DataFrame (intent_rows, columns = intent_columns)
entity_matrix = pd.DataFrame (entity_rows, columns= entity_columns)
grouped_intent = intent_matrix.groupby(['Actual Intent'])['Detected Intent Confidence'].mean()
grouped_intent = grouped_intent.to_frame()
grouped_entity = entity_matrix.groupby(['Entity Name'])['Detected Entity Confidence'].mean()
grouped_entity= grouped_entity.to_frame()
output_file_name="Results"
intent_rows.append(row_intent)
entity_rows.append(entity_row)
intent_matrix = pd.DataFrame (intent_rows, columns = intent_columns)
entity_matrix = pd.DataFrame (entity_rows, columns= entity_columns)

if output_file_name in os.listdir(path):
    intent_matrix.to_csv(path+output_file_name+'/Intents-Detailed Report.csv', index = False)
    entity_matrix.to_csv(path+output_file_name+'/Entities-Detailed Report.csv')
    grouped_intent.to_csv(path+output_file_name+'/Intent wise accuracy.csv')
    grouped_entity.to_csv(path+output_file_name+'/Entity wise accuracy.csv')
else:
    os.mkdir(path+output_file_name)
    intent_matrix.to_csv(path+output_file_name+'/Intents.csv')
    entity_matrix.to_csv(path+output_file_name+'/Entities.csv')
    grouped_intent.to_csv(path+output_file_name+'/Intent wise accuracy.csv')
    grouped_entity.to_csv(path+output_file_name+'/Entity wise accuracy.csv')
