import requests

def get_ip():
    url = "https://ipinfo.io/json"
    response = requests.get(url)
    return response.json()
