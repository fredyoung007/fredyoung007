"""datascience.py
Data science examples
"""
import pandas as pd
import numpy as np

import json

df = pd.DataFrame(np.array([[1,2,3], [4,5,6], [7,8,9]]), columns=['a','b','c'])
print(df.transform(func = lambda x: x+10))
print(df.transform(func = ['sqrt']))

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

json_object = json.dumps(person, indent = 4) 
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 

# Opening JSON file 
with open("sample.json", "r") as openfile: 
    # Reading from json file 
    json_object = json.load(openfile) 
  
print(json_object) 
