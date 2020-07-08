import bs4
import requests
from bs4 import BeautifulSoup


acao = 'movi3'
url = 'https://statusinvest.com.br/acoes/'

r = requests.get(url+f'{acao}')
soup = bs4.BeautifulSoup(r.text, 'xml')

print(soup)

print('ok')
