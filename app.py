import os
from twilio.rest import Client

message = os.getenv("INPUT_MESSAGE")
sender = os.getenv('INPUT_FROM')
receiver = os.getenv('INPUT_TO')
account_sid=os.getenv('INPUT_TWILIO_ACCOUNT_SID')
authtoken=os.getenv('INPUT_TWILIO_AUTH')


#creating twilio client

sender='whatsapp:'+sender
receiver='whatsapp:'+receiver
client=Client()
client.messages.create( from_=sender, body=message, to=receiver)
