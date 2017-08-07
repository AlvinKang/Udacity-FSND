from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3535f25a74328fd4f50f258bda1c3fcd"
# Your Auth Token from twilio.com/console
auth_token  = "c29d879a8d90272da41d80dc995f67a4"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17025314260", 
    from_="+18598881215",
    body="Hello from Python!")

print(message.sid)
