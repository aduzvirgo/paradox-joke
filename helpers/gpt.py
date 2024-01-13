import requests

url = "https://ronreiter-meme-generator.p.rapidapi.com/meme"

querystring = {"top":"Top Text","bottom":"Bottom Text","meme":"Condescending-Wonka","font_size":"50","font":"Impact"}

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "ronreiter-meme-generator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())
