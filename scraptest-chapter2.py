from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

tagName = 'span'
tagAttribute = {'class':{'green', 'red'}}

nameList = bs.find_all(tagName, tagAttribute, limit=3)
title = bs.find_all(id='title')
nameList = bs.find_all(string='the prince')
print(title)
for name in nameList:
    print(name.get_text().replace('\n', ' '))

print(len(nameList))