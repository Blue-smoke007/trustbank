from twilio.rest import Client

# Replace these with your Twilio Account SID and Auth Token
account_sid = 'ACca8e92f22a9545888981187f2ac15213'
auth_token = 'a6221b3d3f8c66e24a0fd64a0e7333ba'

# Create a Twilio client
client = Client(account_sid, auth_token)
# Replace these with your Twilio phone number and the recipient's mobile number
from_number = '+19419496785'
to_number = '+12039184057'

# The message you want to send
message_body = 'Testing sms by the backend Team lead!'

# Send the SMS
message = client.messages.create(
    from_=from_number,
    body=message_body,
    to=to_number
)

# Print the SID (a unique identifier) of the sent message
print(f"Message SID: {message.sid}")