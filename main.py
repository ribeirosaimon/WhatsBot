import time
from datetime import datetime
from tratamentos.info_acao import verifica_acao
from twilioBotWhat import mensagem_retorno

watch_list = [['movi3',15.00,17.00],['mypk3',13.50,14.54],['tcsa3',10.58,14.00]]
numeros_cadastrados = ['554891784586','554899628260']



if __name__ == '__main__':
    hora_do_dia = int(datetime.now().strftime('%H'))
    try:
        while True:
            while 10 <= hora_do_dia <= 17:
                for acao in watch_list:
                    try:
                        retorno = verifica_acao(acao[0],acao[1],acao[2])
                        time.sleep(5)
                        for mensagem in retorno:
                            if mensagem != None:
                                print(mensagem)
                                mensagem_retorno(*numeros_cadastrados)
                    except Exception as ex:
                        print(f'Nao consegui verificar a ação {acao[0]}', ex)
                time.sleep(300)


            hora_do_dia = int(datetime.now().strftime('%H'))
            time.sleep(900)


    except Exception as e:
        print(e)
