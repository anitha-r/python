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
###frame = frame.astype({'balance',np.float32 })

print(frame.dtypes)
print(frame.describe())


frame.to_csv (r'C:\\Users\\anith\\blog\\customer2.csv', index = False, header=True)