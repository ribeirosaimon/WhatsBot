import time
from datetime import datetime
from tratamentos.info_acao import verifica_acao
from twilioBotWhat import mensagem_retorno

watch_list = [['movi3',15.00,17.00],['mypk3',12.00,14.54],['wege3',53.20,55.80]]
numeros_cadastrados = ['554891784586','554899628260']

if __name__ == '__main__':
    try:
        while True:
            for acao in watch_list:
                try:
                    retorno = verifica_acao(acao[0],acao[1],acao[2])
                    time.sleep(5)
                    for mensagem in retorno:
                        if mensagem != None:
                            mensagem_retorno(mensagem,*numeros_cadastrados)
                except:
                    print(f'Nao consegui verificar a ação {acao[0]}')
            time.sleep(300)


    except Exception as e:
        print(e)
