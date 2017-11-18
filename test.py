# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACa75631f2ff48457ae608c513ad1b5063"
auth_token = "cfb8a82fecaa3535de4fd52dab2b09c1"

client = Client(account_sid, auth_token)

client.messages.create(
    to="+16476071664",
    from_="+16136998144",
    body="Hello there!")