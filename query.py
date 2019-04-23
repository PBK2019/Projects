import re
import mysql.connector
db = mysql.connector.connect(user='root', password='root', host='localhost', port='3306', database='data_scrap')
q = 'what is phone number and where address of apple'
#q= str(input())

quest = []
stp_bots = []
final_qsn = []
file = open('stopwords.txt','r')

dictionary = { 'finance':{'fin_ticker'  :'what','total_revenue' :'how much','total_revenue' :'what','cost_of_revenue' :'how much','cost_of_revenue' :'what','Income_tax' :'how much','Income_tax' :'what','NET_income' :'what'},
               'statistics':{'sno' : 'None','stat_ticker' :'what','market_cap' :'what','market_cap' :'how much','enterprise_value' :'what','enterprise_value' :'how much','return_on_assets' :'how much','return_on_assets' :'what','total_cash' :'what','operating_cashflow' :'what','levered_free_cashflow' :'what','total_debt' : 'what','current_ratio' :'what','current_ratio' :'how much','gross_profit' :'what','gross_profit' :'how much','profit_margin' :'what','profit_margin' :'how much'},
               'profile':{'prof_ticker' :'what','name' :'what','address' :'where','address' :'what','phone_num' :'what','Website' :'what','sector' :'what','sector' :'which','industry' :'what','industry' :'which','full_time_emplys' :'how many','full_time_emplys' :'what','Bus_summ' :'what'}}

print(dictionary)
print(dictionary['finance']['total_revenue'])

quest = q.split(" ")
print(quest)
for line in file:
    stp_bots +=line.split('\n')
while stp_bots.count('') > 0:
    stp_bots.remove('')

#print(stp_bots)
for i in quest:
    f='"'+i+'"'
    print(f)
    for j in stp_bots:
        print(j)
        print(f)
        if f == j:
            while quest.count(i) > 0:
                #print(j)
                quest.remove(i)
print(quest)
for i in quest:
    for k,v in dictionary.items():
        for k1,v1 in k[0].items():
            if i== k1:
                print(k1)