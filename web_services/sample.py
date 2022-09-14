#imports
import urllib.error, urllib.request, urllib.parse
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#default api_key and serviceurl, serviceurl is variable that represents the api you want to retrieve data from
api_key = False
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'

#while loop prompting user for address and encoding in a way out of the loop
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

#create parameter dictionary assign prompted address to key "address" if api_key is provided assign it in dict under key "key"
#assign url variable to be the serviceurl plus the parms gained from the api encoded in urlencode
    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

#create data variable and assign it the json
    data = urllib.request.urlopen(url).read().decode()

#put the json in a varable called js and try to parse it as a string
    try:
        js = json.loads(data)
    except:
        js = None
#verify status indicator is ok
    if not js or 'status' not in js or js['status'] != 'OK':
        print('not today homeslice')
        print(data)
        continue
