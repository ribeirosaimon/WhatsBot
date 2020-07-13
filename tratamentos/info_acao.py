from tratamento_acao import get_api
from datetime import datetime
import time

def minima_ou_maxima(*dados):
    max = False
    if dados[2] <= dados[1]:
        max = True
    if dados[3] >= dados[1]:
        max = False
    return [max, False]


def verifica_acao(watch_list):
    for stock in watch_list:
        a = minima_ou_maxima(*get_api(stock))
        print(a)




verifica_acao(['movi3', 'shul4'])
