import requests
from bs4 import BeautifulSoup
import json

URL = "https://finance.yahoo.com/quote/NQ%3DF?p=NQ%3DF"
r = requests.get(URL)

soup = BeautifulSoup(r.content,'html5lib')

summary = []

table = soup.find('table', attrs={'class': 'W(100%)'})
table.append(soup.find('table', attrs={'class': 'W(100%) M(0) Bdcl(c)'}))
#print(table)
for row in table.findAll('tr', attrs={'class': 'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px)'}):
    summary.append(row.text)
for row in table.findAll('tr', attrs={'class': 'Bxz(bb) Bdbw(1px) Bdbs(s) Bdc($seperatorColor) H(36px) '}):
    summary.append(row.text)
#print(summary)
json_string = json.dumps(summary)
print(json_string)
