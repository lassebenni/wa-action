import os
from twilio.rest import Client

message = os.getenv("INPUT_MESSAGE")
sender = os.getenv("INPUT_FROM")
receiver = os.getenv("INPUT_TO")
account_sid = os.getenv("INPUT_TWILIO_ACCOUNT_SID")
auth_token = os.getenv("INPUT_TWILIO_AUTH")


# creating twilio client

sender = "whatsapp:" + sender
receiver = "whatsapp:" + receiver

client = Client(account_sid, auth_token)
message = client.messages.create(from_=sender, body=message, to=receiver)
