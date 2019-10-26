# Python & Twilio


There is a lot of Cool APIs in the internet and the one we are going to Discuss is Twilio that has a different features such as :

  - SMS marketing
  - phone verification
  - Alerts and notifications
  - Push Notifications
  - Call tracking
  - web chat 

# Create Twilio Account

  - Go to https://www.twilio.com/try-twilio
  - Fill the required Fields
  - Verify Email
  - Put your number and verify the sent code
  
### Welcome to The Dashborad

    -You will find your Trial number-
    -You will find your Account SID -
    -You will find your Auth Token -

 Three things required for our code
 
 
**Open your favorite Terminal and run these commands*

### Python File Creation 

```
$ create a python file (send_sms.py)
$ cd acces_to_your_directory (where the file exist)
```

### Twilio Installation
 

```
$ pip install twilio
```

# Steps to Send SMS To Your Phone 

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


### Run your python file

python send_sms.py

PS: as much as you run your file as much you recieve a text massage on your phone.

License
----

AHED BAHRI 

Enjoy.
