import time
from datetime import datetime
from tratamentos.info_acao import verifica_acao
from twilioBotWhat import mensagem_retorno

numero_ralney = '554899628260'

watch_list = [['movi3',15.00,17.00],['mypk3',12.00,14.54],['wege3',53.20,55.80]]
numeros_cadastrados = ['554891784586','555596985884']



if __name__ == '__main__':
    hora_do_dia = int(datetime.now().strftime('%H'))
    try:
        while True:
            print(f'Ainda não esta na hora de começar {hora_do_dia}')
            while 10 <= hora_do_dia <= 17:
                for acao in watch_list:
                    try:
                        retorno = verifica_acao(acao[0],acao[1],acao[2])
                        time.sleep(5)
                        for mensagem in retorno:
                            print(mensagem)
                            if mensagem != None:
                                mensagem_retorno(mensagem,*numeros_cadastrados)
                    except Exception as ex:
                        print(f'Nao consegui verificar a ação {acao[0]}', ex)
                time.sleep(300)
            hora_do_dia = int(datetime.now().strftime('%H'))
            print('dormindo por 15 minutos')
            time.sleep(900)


    except Exception as e:
        print(e)
