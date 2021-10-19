import requests
import json
import pandas as pd

response = requests.get("http://api.open-notify.org/astros.json")
if (response.status_code == 200):
    print("The request was a success!")
    # Code here will only run if the request is successful
elif (response.status_code == 404):
    print("Result not found!")
    # Code here will react to failed requests

#response.content() # Return the raw bytes of the data payload
#response.text() # Return a string representation of the data payload
#response.json() # This method is convenient when the API returns JSON

##Sample call using static parameters
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
##print(response.json())

# Create a new resource
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# Update an existing resource
requests.put('https://httpbin.org/put', data = {'key':'value'})
##print(response.headers["date"]) 

##Sample call to get latest position
response = requests.get('http://api.open-notify.org/iss-now.json')
obj = response.json()
##print(obj)
text = json.dumps(obj, sort_keys=True, indent=4)
##print(text)

df = pd.read_json(text)
##print(df)

latt = df["iss_position"]
print("\nLatitude is " + str(latt["latitude"]))
print("\nLongitude is " + str(latt["longitude"]))