import requests
from bs4 import  BeautifulSoup




r=requests.get('https://newyork.craigslist.org/search/sof','lxml')
soup = BeautifulSoup(r.text)
#print soup


# div = soup.findAll('span', id='titletextonly')

# for links in div:
# 	print links
links=[]

for link in soup.find_all('a'):
    a=link.get('href')
    if (a=='*.html'):
    	print a
    	# links.append(a)

# print links





