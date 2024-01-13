
import requests

def gpt(text):
    url = "http://216.98.10.228:5000/gpt"
    params = {
    "query":text}
    response = requests.get(url, params=params)
    data = response.json()
    return data['answer']

# Example usage:
text_input = "hello world"
result = gpt(text_input)
print(result)
