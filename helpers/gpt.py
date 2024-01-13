
import requests

def gpt(text):
    url = "http://216.98.10.228:5000/gpt"
    params = {
    "ask":text}
    response = requests.get(url, params=params)
    data = response.json()
    return data['answer']

print(data)
