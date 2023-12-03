

import requests
import json

url = "http://127.0.0.1:8000"

data = {
    "username" : "90",
    "password" : "90"
}
headers = {
    "Content-Type" : "application/json"
}
# data = json.dumps(data)
res = requests.post(url,headers=headers,json=data)

print(res.text)