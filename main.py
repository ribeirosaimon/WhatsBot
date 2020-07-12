import time
from tratamentos.tratamento_acao import get_api
from tratamentos.info_acao import tratamento_acao


principal_stocks = ['SQIA3', 'COGN3', 'CAML3']
primeira_vez = True
contador = 0


if __name__ == '__main__':
    while True:
        try:
            for x in principal_stocks:
                if primeira_vez == True:
                    primeiro_retorno = tratamento_acao(*get_api(x))
                    primeira_vez = False
                    print(x,primeiro_retorno)
                elif contador >= 1800:
                    segundo_retorno = tratamento_acao(*get_api(x))
                    contador = 0
                    print(x,segundo_retorno)
                time.sleep(3)
                #contador em segundos
                contador += 900

        except Exception as e:
            print(x ,e)
