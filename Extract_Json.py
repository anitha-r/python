import json
import numpy as np
''' 
# Opening JSON file
f = open('C:\\Users\\anith\\blog\\customer1.json',"r")
  
# returns JSON object as 
# a dictionary
data = json.load(f)
  
# Iterating through the json
# list
for i in data['Customers']:
    print(i)
  
# Closing file
f.close()
 '''

import pandas as pd
with open('C:\\Users\\anith\\blog\\customer2.json') as json_data:
   obj = json.load(json_data)
   #frame = pd.DataFrame(obj['TimeSeries']['Row'], columns=['CLOSE', 'TIMESTAMP'])
   frame = pd.DataFrame(obj['Customers'], columns=['_id', 'balance','age','name','gender'])

frame['balance'] = frame['balance'].str.replace('$','')
frame['balance'] = frame['balance'].str.replace(',','')
frame['balance'] = frame.balance.astype(float)

###print("start")
###print(frame.dtypes)
##print(frame.describe())
#print("test")

###frame.to_csv (r'C:\\Users\\anith\\blog\\customer2.csv', index = False, header=True)

###BalTot = frame.groupby("gender")
###print(BalTot.describe())
###print(BalTot["balance"].describe())

###Bal_GrpAge = frame.groupby(["gender","age"])
###print(Bal_GrpAge["balance"].describe())

###print("gpAge")
gp_Age = frame.groupby(['gender','age']).agg({'balance': ['mean', 'min', 'max']})
###print(gp_Age)

gp_Age.columns = ['age_mean', 'age_min', 'age_max']

# reset index to get grouped columns back
gp_Age = gp_Age.reset_index()

###print(gp_Age.applymap(str))

text_file = open("C:\\Users\\anith\\blog\\customer2.csv", "w")
n = text_file.write('List of aggregates for the customer by gender and age\n')
n = text_file.write(gp_Age.to_string(index=False))
n = text_file.write('\n\n End of Report')

text_file.close()
