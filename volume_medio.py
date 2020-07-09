import bs4
import requests
from bs4 import BeautifulSoup
import json
from principal_stocks import *

def find_stock(stock):
    td_stock = []
    r = requests.get(f'https://finance.yahoo.com/quote/{stock}.SA/history?p={stock}.SA')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    tr_soup = soup.find('tr',{'class':'BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)'})
    for td in tr_soup:
        td_stock.append(td.text)
    r = requests.get(f'https://statusinvest.com.br/acoes/{stock}')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    soup = soup.find('div',{'class':'card rounded text-main-green-dark'})
    soup = soup.find_all('strong',{'class':'value'})
    vol_medio = soup[2].text.replace('.','').replace(',','.')
    if vol_medio == '-':
        vol_medio = 0
    else:
        vol_medio = format((float(vol_medio)/7),'.2f')
        vol_medio = float(vol_medio)
    if td_stock[6] == '-':
        td_stock[6] = 0
    else:
        td_stock[6] = format(float(td_stock[2]),'.2f')
    dict_stock = {'stock':stock,
        'date':td_stock[0],
        'open':float(td_stock[1]),
        'high':float(td_stock[2]),
        'low':float(td_stock[3]),
        'close':float(td_stock[4]),
        'volume':td_stock[6],
        'volume medio':vol_medio
    }
    json_stock = json.dumps(dict_stock)
    return json_stock

a = find_stock('klb')
'''
for x in principal_stocks:
    acaook = find_stock(x)
    print(acaook)
'''
