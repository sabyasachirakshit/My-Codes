"""import os
from twilio.rest import Client 
 
account_sid = 'ACdc8f0e23e2286d4976874657334e1e48' 
auth_token = '[AuthToken]' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+918910124047',  
                              body='hi',      
                              to='whatsapp:+919123662963' 
                          ) 
 
print(message.sid)"""

import pywhatkit
pywhatkit.sendwhatmsg('+919123662963', 'Hello', 11,20)
