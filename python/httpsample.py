"""httpsample.py
Http examples
"""
import requests
import os

payload = {"name":"Fred", "ID":"007"}

# wsget
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
fname = url.split('/')[-1]
path = os.path.join(os.getcwd(), fname)

r = requests.get(url)
with open(path, "wb") as f:
    f.write(r.content)

# get request
url_get = "http://httpbin.org/get"

r = requests.get(url_get, params=payload)
print(r.headers["content-type"])
print(r.json())
print(r.json()["args"])

# post request
url_post = "http://httpbin.org/post"
rp = requests.post(url_post, data=payload)

print("POST request body:", rp.request.body)
print(rp.json())
print(rp.json()["form"])