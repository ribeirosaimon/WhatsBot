from flask import Flask, request, jsonify
from create_json_api import *


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/stock/<stock>", methods=['GET'])
def stock(stock):
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
        vol_medio = format((float(vol_medio)/30),'.2f')
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
    return dict_stock

if __name__ == "__main__":
    app.run(debug=True)


'''
@app.route("/<str:stock>", methods=['GET'])
def stock(stock):
    list = []
    with open('stock.json','r') as arquivo:
        for x in arquivo:
            list.append(json.loads(x))
    return jsonify(list),200
'''
