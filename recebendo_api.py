import requests
import json
import time



def simular_site():
    with open('stock.json','r') as json_file:
        dados = json.load(json_file)
        return dados


lista = ['movi3','tcsa3','shul4']

def get_api(stock):
    #stock = stock
    #api = 'https://secure-wildwood-34847.herokuapp.com/stock'
    #resposta = requests.request('GET', api + f'/{stock}')
    #acao = resposta.json()
    acao = simular_site()
    dados_acao = acao[stock]
    nome_acao = stock
    adj_close = acao[stock]['adj_close']
    avg_vol = acao[stock]['avg_vol']
    vol = acao[stock]['vol']
    high = acao[stock]['high']
    low = acao[stock]['low']
    return [nome_acao, adj_close, high, low, avg_vol, vol]

def teste(*dados):
    if dados[2] <= dados[1]:
        print(f'Uhuul! {dados[0]} está na máxima do dia!')
        return f'Uhuul! {dados[0]} está na máxima do dia!'
    if dados[3] >= dados[1]:
        print(f'A Cotação de {dados[0]} está na mínima do dia!')
        return f'A Cotação de {dados[0]} está na mínima do dia!'

    return print('Passou pelo teste UHUUUUUUUUUUUUUUUUU')


if __name__ == '__main__':
    while True:
        time.sleep(120)
        a = get_api('shul4')
        teste(*a)

'''
    while True:
        for x in lista:
            time.sleep(1)
            a = get_api(x)
            teste(*a)
'''
