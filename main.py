import time
from datetime import datetime
from tratamentos.info_acao import verifica_acao
from twilioBotWhat import mensagem_retorno

watch_list = ['movi3','shul4','itsa4','prio3','wege3']

if __name__ == '__main__':
    try:
        a = datetime.now()
        contador = 0
        while True:
            for x in watch_list:
                retorno = verifica_acao(x,contador)
                time.sleep(5)
                if retorno != None:
                    contador += 1
                    mensagem_retorno(retorno)
            time.sleep(300)
        b = datetime.now()
        print(b - a, ' TEMPO DE EXECUÇÃO DO APP')

    except Exception as e:
        print(e)
