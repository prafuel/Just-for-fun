
import requests
import json

url = "https://learnerapi.vierp.in/AppLogin/NewsignIn"

data = {
    "username" : "12111142",
    "password" : "1"
}

headers = {
    "Content-Type" : "application/json",
}

res = requests.post(url,json=data,headers=headers)

print(res.content)