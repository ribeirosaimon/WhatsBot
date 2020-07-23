import time
from datetime import datetime
from tratamentos.info_acao import verifica_acao
from twilioBotWhat import mensagem_retorno

watch_list = [['HGTX3',15.00, 16.13, 15.64],['MGLU3',84.00, 87.78, 85.04],['EZTC3',40.00, 41.09, 40.99], ['GRND3', 7.30, 8.27, 8.06],]
numeros_cadastrados = ['0']
mensagem_conferencia = []
contador = 0
tempo_conferencia = 900


if __name__ == '__main__':
    hora_do_dia = int(datetime.now().strftime('%H'))
    try:
        while True:
            # Fazendo com que o App somente execute no horario da bolsa
            while 10 <= hora_do_dia <= 17:
                #pra todas as ações da watch list
                for acao in watch_list:
                    try:
                        #retorna a maxima a minima e porventura algum stop gain ou stoploss
                        retorno = verifica_acao(acao[0].lower(),acao[1],acao[2],acao[3])
                        time.sleep(5)
                        #pra cada mensagem no retorno diferente de None vai enviar essa sms pro whatsapp das pessoas cadastradas
                        for mensagem in retorno:
                            if mensagem != None:
                                if mensagem not in mensagem_conferencia:
                                    #essa sms vai ser adicionada na lista de sms conferencia, para nao ser enviada sempre... somente no intervalo de 1 Hora
                                    mensagem_conferencia.append(mensagem)
                                    mensagem_retorno(mensagem, *numeros_cadastrados)
                                    #contador de tempo vai zerar, caso a sms seja enviada
                                    contador = 0
                    except:
                        mensagem_retorno('Deu tudo certo amigao'*numeros_cadastrados)
                contador += tempo_conferencia
                time.sleep(tempo_conferencia)
                if contador >= 1800:
                    #apos 1 hora será limpa a lista das conferencia de mensagem
                    mensagem_conferencia = []
            hora_do_dia = int(datetime.now().strftime('%H'))
            time.sleep(900)
    except Exception as e:
        print(e)
