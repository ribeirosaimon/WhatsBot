import json
import requests


def get_api(stock):
    stock = stock
    api = 'https://secure-wildwood-34847.herokuapp.com/stock'
    resposta = requests.request('GET', api + f'/{stock}')
    acao = resposta.json()
    dados_acao = acao[stock]
    nome_acao = stock
    adj_close = acao[stock]['adj_close']
    avg_vol = acao[stock]['avg_vol']
    vol = acao[stock]['vol']
    high = acao[stock]['high']
    low = acao[stock]['low']
    return [nome_acao, adj_close, high, low, avg_vol, vol]
