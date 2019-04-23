import urllib.request

import mysql.connector
import os

from bs4 import BeautifulSoup
db = mysql.connector.connect(user='root', password='root', host='localhost', port='3306', database='data_scrap')
l1 = []
l2 = []
l3 = []
a1, a2, a3, a4, a5 = str(), str(), str(), str(), str()
f = open("E:/MSIT/Python/Week-2/Stock_market_Scrapping/tickers.txt", 'r')
for line in f:
    l1 += line.split('\n')
while l1.count('') > 0:
    l1.remove('')
for i in l1:
    s1 = i.split('@')
    l2.append(s1[0])
    l3.append(s1[1])
files = os.listdir("E:/MSIT/Python/Week-2/Stock_market_Scrapping/stack")

for file in files:
   # print(file+" ******** ")
    if file != 'tickers':
        h1 = os.listdir('E:/MSIT/Python/Week-2/Stock_market_Scrapping/stack/%s' % file)
        for i in h1:
            # print(file)
            # print(i)
            if i == 'Financials.html':
                url = 'stack/{}/{}'.format(file, i)
                print(url)
                f = open(url, 'r')
                soup = BeautifulSoup(f)
                features = "html.parser"
                str1 = ''.join(l2)
                table1 = soup.findAll('td', attrs={'class': 'Fz(s)'})
                table2 = soup.find('td', attrs={'class': 'Fw(600)'})

                print(table1)
                print(table2)
                if file == 'Alphabet Inc':
                    for l in range(len(l3)):
                        f = str(file + '.')

                        if l3[l] == f:
                            a5 = str(str1[l].text)
                            print(f + "************"+a5)
                    for line in table1:
                        print(line)
                        temp = line.get('data-reactid')
                        if temp == '42':
                            a1 = str(line.text)
                            print("**"+a1)
                        if temp == '53':
                            a2 = str(line.text)
                            print(a2)
                        if temp == '172':
                            a3 = str(line.text)
                            print("*****"+a3)
                    a4 = str(table2.text)
                    print(a4)
                    mycursor = db.cursor()
                    sql = "INSERT INTO finances (fin_ticker, total_revenue, cost_of_revenue, income_before_tax, net_income) VALUES (%s, %s, %s, %s, %s)"
                    val = (a5, a1, a2, a3, a4)
                    mycursor.execute(sql, val)
                    db.commit()
