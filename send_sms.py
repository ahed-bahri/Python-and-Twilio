 from twilio.rest import Client
    account_sid = 'YOUR SID' 
    auth_token = 'YOUR AUTH KEY' 
    client = Client(account_sid, auth_token) 
    message = client.messages \
                .create(
                     body=" Put Your massage here",
                     from_='Your trial number', #remove any space between
                     to='Your original number'  #remove any space between
                 )
    print(message.sid)
