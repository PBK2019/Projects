import os
import sys
import urllib.request

import requests
from bs4 import BeautifulSoup

list = []
li = []
fo=open("tickers.txt","r")
i=0
for line in fo :
    list +=line.split('\n')
while list.count('')>0:
    list.remove('')
for i in list:
    qw = i.split("@")
    li +=qw[0]
    print(qw[0])
    filename="%s" % qw[1]
    print(filename)
    dir = 'stack/%s'% filename
    if not os.path.exists(dir):
        os.makedirs(dir)

    else:
        print("already exists.")
        abr = '%s' % qw[0]
        url = ("https://finance.yahoo.com/quote/{}/profile?p={}") .format(abr,abr)
        page = urllib.request.Request(url)
        mypath = "E:\MSIT\Python\Week-2\Stock_market_Scrapping\stack\%s" % qw[1]

        fullpath = os.path.join(mypath, "Statistics.html")
        fullpath1 = os.path.join(mypath, "Financials.html")
        fullpath2 = os.path.join(mypath, "profile.html")
        fullpath3 = os.path.join(mypath, "Summary.html")
        url = ("https://finance.yahoo.com/quote/{}/Statistics?p={}").format(abr,abr)
        url1 = ("https://finance.yahoo.com/quote/{}/Financials?p={}").format(abr,abr)
        url2 = ("https://finance.yahoo.com/quote/{}/profile?p={}").format(abr,abr)
        url3 = ("https://finance.yahoo.com/quote/{}?p={}").format(abr, abr)
        urllib.request.urlretrieve(url, fullpath)
        urllib.request.urlretrieve(url1, fullpath1)
        urllib.request.urlretrieve(url2, fullpath2)
        urllib.request.urlretrieve(url3, fullpath3)