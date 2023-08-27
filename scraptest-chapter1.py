from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    except URLError as e:
        print('Error: The server could not be found!')
    else:
        try:
            bs = BeautifulSoup(html.read(), 'html.parser')
            title = bs.body.h1
        except AttributeError as e:
            return None
        return title

title = getTitle('http://aaapythonscraping.com/pages/page1.html')
if title == None:
    print('Error: Title could not be found')
else:
    print(title)