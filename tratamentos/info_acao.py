from tratamentos.tratamento_acao import get_api
from datetime import datetime
import time

def maxima_do_dia(*dados):
    max = None
    if dados[2] <= dados[1]:
        max = f'Sua {dados[0]} Está na maxima do Dia! no valor de {dados[1]}'
    return max

def minima_do_dia(*dados):
    min = None
    if dados[3] >= dados[1]:
        min = f'Sua {dados[0]} Está na mínima do Dia! no valor de {dados[1]}'
    return min


def volume(*dados):
    hora_do_dia = datetime.now().strftime('%H')
    horas_passadas = 7 - (17 - int(hora_do_dia))
    volume_medio_diario = dados[5]/ horas_passadas
    avg_vol = dados[4] / 7
    if volume_medio_diario > avg_vol:
        return f'O volume de {dados[0]} está projetado acima da média'
    return None


def verifica_acao(stock, stop_loss, stop_gain, entrada):
    retorno_max, retorno_min, retorno_volume, retorno_stop, retorno_entrada = None, None, None, None, None
    dados_tratamento = get_api(stock)
    max_diaria = maxima_do_dia(*dados_tratamento)
    min_diaria = minima_do_dia(*dados_tratamento)
    volume_diario = volume(*dados_tratamento)
    if dados_tratamento[1] <= stop_loss:
        retorno_stop = f'Ação {dados_tratamento[0]} atingiu StopLoss de R${stop_loss}'
    if dados_tratamento[1] >= stop_gain:
        retorno_stop = f'Ação {dados_tratamento[0]} atingiu StopGain de R${stop_gain}'
    if dados_tratamento[1] >= entrada:
        retorno_entrada = f'Sua Ação {dados_tratamento[0]} atingiu o Valor de Entrada de R${entrada}'
    if volume_diario != None:
        retorno_volume = volume_diario
    if max_diaria != None:
        retorno_max = max_diaria
    if min_diaria != None:
        retorno_min = min_diaria
    return [retorno_volume, retorno_min, retorno_max, retorno_stop, retorno_entrada]
