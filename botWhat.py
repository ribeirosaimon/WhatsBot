from twilio.rest import Client

account_sid = 'ACd5235092aad431eeb7d2871c2fb59b08'
auth_token = 'ff04b3b2fb6bcda074ce8915f1b5aab6'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='whatsapp:+14155238886',
                              body='Teste',
                              to='whatsapp:+554891784586'
                          )

print(message.sid)
