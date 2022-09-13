# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
total_comments = 0
counts = 0
# Retrieve all of the anchor spans
spans = soup('span')
for span in spans:
    # Look at the parts of a span
    print('SPAN:', span)
    print('URL:', span.get('href', None))
    print('Contents:', span.contents[0])
    comment = int(span.contents[0])
    total_comments = total_comments + comment
    counts = counts + 1
    print('Count:', counts)
    print('Sum:',total_comments)

    # print('Attrs:', tag.attrs)
