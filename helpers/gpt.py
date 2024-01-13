import requests

const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://ronreiter-meme-generator.p.rapidapi.com/meme',
  params: {
    top: 'Top Text',
    bottom: 'Bottom Text',
    meme: 'Condescending-Wonka',
    font_size: '50',
    font: 'Impact'
  },
  headers: {
    'X-RapidAPI-Key': 'SIGN-UP-FOR-KEY',
    'X-RapidAPI-Host': 'ronreiter-meme-generator.p.rapidapi.com'
  }
};

try {
	const response = await axios.request(options);
	console.log(response.data);
} catch (error) {
	console.error(error);
}
