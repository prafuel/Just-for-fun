
import requests,json
from datetime import datetime

def getData():
    url = "https://ipinfo.io/json"
    response = requests.get(url=url)
    if response.status_code == 200:
        return response.json()
    return "Not Found"

def to_personal_server():
    response = getData()
    with open('info.txt','w') as text:
        text.write(str(datetime.now())+"\n")
        for i in response:
            if i != "readme":
                text.write(response[i]+"\n")
    # print(response)

def reader():
    labels = ['date','ip','city','region','country','loc','org','postal','timezone']
    data = {}
    with open('info.txt','r') as text:
        for index,line in enumerate(text.readlines()):
            data[labels[index]] = line.strip()
    return data
            

def to_discord():
    date = datetime.now()
    url = "https://discord.com/api/v9/channels/1160642283775987795/messages"

    response = getData()

    ip = response['ip']
    city = response['city']
    loc = response['loc']
    postal = response['postal']

    payload = f"Date = {date} ip={ip} , city={city}, loc={loc}, postal={postal}"

    data = {
        "content": payload
    }

    data = json.dumps(data)

    headers = {
        "Authorization": "OTUxNDkyMTI1MDA5MjU2NDU4.G-7L62.urUVhT7dhCvMlubDEgCD28WNpgnbR99J9q6IFk",
        "Content-Type": "application/json"
    }

    print(data)
    res = requests.post(url=url, data=data, headers=headers)

    print(res.status_code)
    if res.status_code != 200:
        print("if code is 401, change Autherization key")


if __name__ == "__main__":
    # to_discord()
    to_personal_server()
    reader()