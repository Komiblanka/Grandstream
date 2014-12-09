import urllib
import urllib2
import json
import argparse

# Parsing arguments
parser = argparse.ArgumentParser(description='Configures some options of the GPX1450 phone')
parser.add_argument('target', help='IP address of the phone.')

args = parser.parse_args()

# Recovering IP address and urls
IP = args.target
login_url = 'http://' + IP + '/cgi-bin/dologin'
options_url = 'http://' + IP + '/cgi-bin/api.values.post'

# POST parameters
login_values = {'password' : '123'}

# Create request and get the response
login_data = urllib.urlencode(login_values)
login_req = urllib2.Request(login_url, login_data)
login_response = urllib2.urlopen(login_req)

#Obtaining the sid (session id) in JSON format
login_response_json = json.loads(login_response.read())
sid = login_response_json["body"]["sid"]

# POST values (first three are for voice gain and P335 is the backlight. Last value is the session id.
option_values = {'P1301': '2', 'P1302' :'2','P1464': '2', 'P335': '0', 'sid' : sid}

# Load request and do the request
data = urllib.urlencode(option_values)
req = urllib2.Request(options_url, data)
options_response = urllib2.urlopen(req)

print options_response.read()
