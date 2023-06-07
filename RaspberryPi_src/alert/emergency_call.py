# Code for Emergency Call
import sys
sys.path.append('/home/roboin/ResQ4U/RaspberryPi_src/common')
from imports import *


class EmergencyCaller():
    def __init__(self):
        self.account_sid = 'ACb1#########f5734af36#########6c962dc6#########79feb4a7' # dahyun account.. will be used
        self.auth_token = '9a713#########e1d865e91#########009872f8#########0a1617f956'
        self.resq4u_number = '+13159225838' # fraud number (just to make calls)
        self.recipient_number = '+821090531622' # dahyun phone number
        
    def callHELP(self):
        # Create client
        client = Client(self.account_sid, self.auth_token)

        # Create call from created client & req. url
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=self.recipient_number,
            from_=self.resq4u_number
        )
        print('Calling Dahyun')
        print('SID Log: ', call.sid)
        
if __name__ == '__main__':
    caller = EmergencyCaller()
    caller.callHELP()