import requests
from bs4 import BeautifulSoup

URL = r'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(URL)
html = BeautifulSoup(response.text, 'html.parser')

for pergunta in html.select('.s-post-summary.js-post-summary'):
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')

    print(f'{data.text}:   {titulo.text}    {votos.text} votos')
