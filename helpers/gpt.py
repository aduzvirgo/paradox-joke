
import requests

def gpt(hello world):
    url = "http://216.98.10.228:5000/gpt"
    params = {
    "ask":hello world}
    response = requests.get(url, params=params)
    data = response.json()
    return data['answer']

print(data)
