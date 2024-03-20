import requests

from icecream import ic
from bs4 import BeautifulSoup
from urllib.request import urlopen 


html = urlopen('http://www.pythonscraping.com/pages/page1.html') 
html_2 = requests.get('http://www.pythonscraping.com/pages/page1.html').content.decode('utf-8')


bs_one = BeautifulSoup(html.read(), 'html.parser')
bs_two = BeautifulSoup(html_2, 'html.parser')
bs_three = BeautifulSoup(html_2, 'html.parser')


ic(bs_one.h1, bs_two.h1, bs_three.h1)