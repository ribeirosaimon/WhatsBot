import time
from datetime import datetime
from tratamentos.info_acao import verifica_acao
from mensagemtwilio.twilioBotWhat import mensagem_retorno
from arquivo_confidencial import WATCH_LIST, NUMBERS




def schedule_conferencia():
    ''' a WATCH_LIST é uma lista onde as ações que deve ser verificada nesse formato:
    formato:['ACAO3',       10.00,        20.00,      11.00]
    ou seja:  stock,      stop_loss,    stop_gain,   entrada
        O NUMBERS é uma lista de todos os numeros que deve enviar mensagem no whats
    formato: 55xxXXXXxxxx
    ou seja: DDI, DDD e telefone de 8 digitos
    '''
    conferencia(WATCH_LIST, NUMBERS)

def conferencia(watch_list, numeros_cadastrados, mensagem_conferencia = [], tempo_conferencia=600, contador = []):
#    try:
    for acao in watch_list:
        #retorno da ação com as mensagens a enviar, coloquei esse sleep só pra não sobrecarregar
        retorno = verifica_acao(acao[0].lower(),acao[1],acao[2],acao[3])
        time.sleep(2)
        for mensagem in retorno:
            if mensagem != None:
                #se tiver algo na mensagem vai abrir o arquivo em modo leitura pra conferir se não foi enviado nos ultimos 60 minutos
                if mensagem not in mensagem_conferencia:
                    #se essa sms não tiver nas sms enviadas nos ultimos 60 minutos vamos fazer um arquivo com as novas mensagens
                    mensagem_retorno(mensagem, numeros_cadastrados)
                    mensagem_conferencia.append(mensagem)
                    #contador de tempo vai zerar, caso a sms seja enviada
                    del(contador[:])

#    except Exception as e:
#        print('Ocorreu algum erro de : ', e)
    contador.append(tempo_conferencia)
    time.sleep(tempo_conferencia)
    if len(contador) >= 6:
        #apos 1 hora será limpa a lista das conferencia de mensagem
        del(mensagem_conferencia[:])
