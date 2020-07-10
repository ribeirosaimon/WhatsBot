import bs4
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from principal_stocks import *
import urllib.parse


def get_api(stock):
    api = 'http://127.0.0.1:5000/stock'
    resposta = requests.request('GET', api + f'/{stock}')
    acao = resposta.json()
    print(acao['high'])

get_api('movi3')
