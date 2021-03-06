import json
import requests
import time


def get_api(stock):
    stock = stock
    api = 'https://secure-wildwood-34847.herokuapp.com'
    resposta = requests.request('GET', api + f'/{stock}')
    time.sleep(1)
    acao = resposta.json()
    dados_acao = acao[stock]
    nome_acao = stock
    adj_close = acao[stock]['adj_close']
    avg_vol = acao[stock]['avg_vol']
    vol = acao[stock]['vol']
    high = acao[stock]['high']
    low = acao[stock]['low']
    mov_avg = acao[stock]['mov_avg']
    rsi = acao[stock]['rsi']
    return [nome_acao, adj_close, high, low, avg_vol, vol, mov_avg, rsi]
