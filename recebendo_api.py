import bs4
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from principal_stocks import *
import urllib.parse


def simular_site(acao):
    with

def get_api(stock):
    api = 'https://secure-wildwood-34847.herokuapp.com/stock'
    resposta = requests.request('GET', api + f'/{stock}')
    acao = resposta.json()
    print(acao[f'{stock}']['close'])

get_api('movi3')
