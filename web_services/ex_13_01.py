#import necessary libraries
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #prompts user for input
    url = input('Enter location:')
    if len(url) < 1: break

    #sends a call to the server
    uh = urllib.request.urlopen(url, context=ctx)
    #reads the response in form of bits
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    #decodes
    #print(data.decode())
tot_sum = 0
tree = ET.fromstring(data)
counts = tree.findall('.//count')
for val in counts:
    #gets val and converts to int
    val = int(val.text)
    tot_sum = tot_sum + val

print('Sum : ',tot_sum)
