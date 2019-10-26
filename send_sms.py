from twilio.rest import Client

#This is my Final Project (Happy to do it & Sad because the Course is Done)
#IN this Project i used TWILIO API to send Messages to the Phone 

account_sid = 'AC3927434e663fb7dae01bc1c610ff58b0' #My SID
auth_token = '33d866da086cd55f83ab36348dd892b8' #My Auth Token
client = Client(account_sid, auth_token) 
#put my message and pass the source , destination and the body
message = client.messages \
                .create(
                     body="Welcome To my First API. #Ahed Bahri",
                     from_='+12562740230',
                     to='+21653541907'
                 )
#print the message result
print(message.sid)