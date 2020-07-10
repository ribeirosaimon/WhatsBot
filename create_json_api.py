import bs4
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
from principal_stocks import *



def find_stock(stock):
    td_stock = []
    data = date_treatment()
    r = requests.get(f'https://finance.yahoo.com/quote/{stock}.SA/history?p={stock}.SA')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    tbody_soup = soup.find('tbody')
    for tr_soup in tbody_soup:
        td_soup = tr_soup.find('span')
        if td_soup.text == data:
            tr_soup_today = tr_soup
    for td in tr_soup_today:
        td_stock.append(td.text)
    r = requests.get(f'https://statusinvest.com.br/acoes/{stock}')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    soup = soup.find('div',{'class':'card rounded text-main-green-dark'})
    soup = soup.find_all('strong',{'class':'value'})
    vol_medio = soup[2].text.replace('.','').replace(',','.')
    if vol_medio == '-':
        vol_medio = 0
    else:
        vol_medio = format(((float(vol_medio)/30)/7),'.2f')
        vol_medio = float(vol_medio)
    if td_stock[6] == '-':
        td_stock[6] = 0
    else:
        td_stock[6] = td_stock[6].replace(',','')
        td_stock[6] = float(td_stock[6])
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

def date_treatment():
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    if month == 1:
        month = 'Jan'
    if month == 2:
        month = 'Fev'
    if month == 3:
        month = 'Mar'
    if month == 4:
        month = 'Abr'
    if month == 5:
        month = 'Mai'
    if month == 6:
        month = 'Jun'
    if month == 7:
        month = 'Jul'
    if month == 8:
        month = 'Ago'
    if month == 9:
        month = 'Set'
    if month == 10:
        month = 'Out'
    if month == 11:
        month = 'Nov'
    if month == 12:
        month = 'Dez'

    if len(str(day)) == 1:
        day = f'0{day}'
    return f'{month} {day}, {year}'


if __name__ == '__main__':
    with open('stock.json','w') as arquivo:
        for x in principal_stocks:
            try:
                json_stock = find_stock(x)
                arquivo.write(json_stock + '\n')
                print(x)
            except Exception as e:
                pass
