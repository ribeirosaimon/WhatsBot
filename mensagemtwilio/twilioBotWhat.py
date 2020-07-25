from twilio.rest import Client
from arquivo_confidencial import ACCONT_SIT , AUTH_TOKEN
account_sid = ACCONT_SIT
auth_token = AUTH_TOKEN
client = Client(account_sid, auth_token)


def mensagem_retorno(mensagem, numeros):
    if mensagem != None:
        for numero in numeros:
            message = client.messages.create(
                                          from_='whatsapp:+14155238886',
                                          body=f'{mensagem}',
                                          to=f'whatsapp:+{numero}'
                                      )
