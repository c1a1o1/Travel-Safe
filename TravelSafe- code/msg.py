#!/usr/bin/python
	 
import urllib2
import cookielib
from getpass import getpass
import sys

def message1():
    username = '9700739743'
    passwd = 'A5442A'
    message = 'hey! I am in danger!! Help me out!! Latitude: 17.5207937 Longitude: 78.6302698'
    number = '8686246278'
    message = "+".join(message.split(' '))


#Logging into the SMS Site
    url = 'http://site24.way2sms.com/Login1.action?'
    data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
 
#For Cookies:
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	 
# Adding Header detail:
    opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120Safari/537.36')]
	 
    try:
	    usock = opener.open(url, data)
    except IOError:
	    print "Error while logging in."
	    sys.exit(1)
	 
	 
    jession_id = str(cj).split('~')[1].split(' ')[0]
    send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
    send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
    opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
	 
    try:
	    sms_sent_page = opener.open(send_sms_url,send_sms_data)
    except IOError:
	    print "Error while sending message"
		
    #sys.exit(1)
    #print "SMS has been sent."
	
