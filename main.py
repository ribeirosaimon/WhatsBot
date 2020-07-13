import time
from datetime import datetime
from tratamentos.info_acao import verifica_acao

watch_list = ['movi3','shul4']

if __name__ == '__main__':
    try:
        a = datetime.now()
        while True:
            verifica_acao(watch_list)
            time.sleep(300)
        b = datetime.now()
        print(b - a, ' TEMPO DE EXECUÇÃO DO APP')

    except Exception as e:
        print(e)
