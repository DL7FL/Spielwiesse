import requests, bs4, lxml

res = requests.get('http://darc.de/f17')
res.raise_for_status()
exampleSoup = bs4.BeautifulSoup(res.text,"lxml")
pElems = exampleSoup.select('p')


len(pElems)
str(pElems[1])
pElems[1].getText()
