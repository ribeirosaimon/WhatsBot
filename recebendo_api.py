import bs4
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from principal_stocks import *
import urllib.parse


def simular_site(acao):
    with open('stock.json','w') as arquivo:
        for x in principal_stocks:
            try:
                json_stock = find_stock(x)
                arquivo.write(json_stock + '\n')
                print(x)
            except Exception as e:
                pass

def get_api(stock):
    api = 'https://secure-wildwood-34847.herokuapp.com/stock'
    resposta = requests.request('GET', api + f'/{stock}')
    acao = resposta.json()
    avg_vol = acao[f'{stock}']['avg_vol']
    vol = acao[f'{stock}']['vol']
    print(avg_vol)
if __name__ == '__main__':
    get_api('movi3')
