import os
from twilio.rest import Client

message = os.getenv("INPUT_MESSAGE")
From = os.getenv('INPUT_FROM')
To = os.getenv('INPUT_TO')
account_sid=os.getenv('INPUT_TWILIO_ACCOUNT_SID')
authtoken=os.getenv('INPUT_TWILIO_AUTH')


#creating twilio client

From='whatsapp:'+From
To='whatsapp:'+To
client=Client()
message = client.messages \
    .create(
         from_=From,
         body=message,
         to=To
     )
print('Message Sent')
