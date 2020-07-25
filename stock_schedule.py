import time
from datetime import datetime
from tratamentos.info_acao import verifica_acao
from twilioBotWhat import mensagem_retorno




def conferencia(watch_list, numeros_cadastrados, tempo_conferencia=900):
    contador = 0
    mensagem_conferencia = []

    for acao in watch_list:
        retorno = verifica_acao(acao[0].lower(),acao[1],acao[2],acao[3])
        time.sleep(2)
        for mensagem in retorno:
            if mensagem != None:
                if mensagem not in mensagem_conferencia:
                    #essa sms vai ser adicionada na lista de sms conferencia, para nao ser enviada sempre... somente no intervalo de 1 Hora
                    mensagem_conferencia.append(mensagem)
                    mensagem_retorno(mensagem, numeros_cadastrados)
                    #contador de tempo vai zerar, caso a sms seja enviada
                    contador = 0


    contador += tempo_conferencia
    time.sleep(tempo_conferencia)
    if contador >= 1800:
        #apos 1 hora será limpa a lista das conferencia de mensagem
        mensagem_conferencia = []
