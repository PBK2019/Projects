import requests
from bs4 import BeautifulSoup

ticker = []
abrivation = []
url = 'https://finance.yahoo.com/trending-tickers'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)
f = open('tickers.txt','w')
data =[]
a = soup.find_all('td',class_='data-col0')
aa= soup.find_all('td',class_='data-col1')
print("Ticker' , 'Name'")
for ti,abr in zip(a,aa) :
    ticker += str(ti.text).split(' ')
    abrivation += str(abr.text).split('\n')
for i in range(6):
    f.write(ticker[i] +'@'+ abrivation[i] + '\n')
    #data.append(tr.text)