'''
Enviar SMS com o Twilio
www.twilio.com 
'''
from twilio.rest import Client

account_sid = 'AC0557f49b8b9fccc3c9048ee6178033aeUNI9301104'
token = '2a2a82e8e186045e9295c5b74063d7e6UNI9301104aex45j6k987'

client = Client(account_sid, token)

remetente = '+15074188317'
destino = '+5511971775750'

message = client.messages.create(
    to=destino,
    from_=remetente,
    body="Boa noite, é o Davi aqui testando o twilio para mandar mensagens do Python!")

print(message.sid)
