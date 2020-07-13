from twilio.rest import Client

account_sid = 'AC14c5ca1da8d1c175b968fcdaaca55654'
auth_token = '5850fed33bdd2c1fde8d09a61f7975f5'
client = Client(account_sid, auth_token)

def mensagem_retorno(mensagem):
    if mensagem != '':
        message = client.messages.create(
                                      from_='whatsapp:+14155238886',
                                      body=f'{mensagem}',
                                      to='whatsapp:+554891784586'
                                  )
    else:
        pass
