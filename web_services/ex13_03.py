import urllib.request, urllib.parse, urllib.error
import json
import ssl



# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

api_key = False
# If you have a Google Places API key, enter it here
api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
while True:
    location = input('Enter Location-')
    if len(location) < 1: break
    params = dict()
    params['location'] = location
    if api_key is not False:params['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    #make a request
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    try:
        js = json.loads(data)
    except:
        js = None

#verify status indicator is ok
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
