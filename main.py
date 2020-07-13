import time
from datetime import datetime
from tratamentos.info_acao import retorno_funcional

watch_list = ['movi3','shul4']

if __name__ == '__main__':
    try:
        a = datetime.now()
        retorno_funcional(watch_list)
        b = datetime.now()
        print(b - a, ' TEMPO DE EXECUÇÃO DO APP')

    except Exception as e:
        print(e)
