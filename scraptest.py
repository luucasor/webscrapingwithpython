from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
    print('The server could not be found!')
else:
    bs = BeautifulSoup(html.read(), 'html.parser')
    # print(bs.html.body.h1)
    try:
        badContent = bs.find("nonExistentTag").find("someTag")
    except AttributeError as e:
        print('Tag was not found')
    else:
        if badContent == None:
            print('Tag was not found')
        else:
            print(badContent)
