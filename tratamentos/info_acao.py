from tratamentos.tratamento_acao import get_api
from datetime import datetime
import time

def maxima_do_dia(*dados):
    max = ''
    if dados[2] <= dados[1]:
        max = f'Sua {dados[0]} Está na maxima do Dia!'
    return max

def minima_do_dia(*dados):
    min = ''
    if dados[3] >= dados[1]:
        min = f'Sua {dados[0]} Está na mínima do Dia!'
    return min

def volume(*dados):
    hora_do_dia = datetime.now().strftime('%H')
    horas_restantes = 17 - int(hora_do_dia)
    horas_passadas = 7 - horas_restantes
    vol_medio_hora = dados[4] / 7
    vol_por_hora = dados[5]*horas_passadas
    if vol_por_hora > vol_medio_hora:
        print('volume acima da media', vol_por_hora, vol_medio_hora)

    print(vol_medio_hora)


def verifica_acao(watch_list):
    for stock in watch_list:
        dados_tratamento = get_api(stock)
        max_diaria = maxima_do_dia(*dados_tratamento)
        min_diaria = minima_do_dia(*dados_tratamento)
        print(f'Verifiquei a ação {stock}')
        if max_diaria != '':
            print(max_diaria)
            return max_diaria
        if min_diaria != '':
            print(min_diaria)
            return min_diaria
