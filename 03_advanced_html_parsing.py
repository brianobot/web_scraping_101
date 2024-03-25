import requests

from icecream import ic
from bs4 import BeautifulSoup, Tag


url = "http://www.pythonscraping.com/pages/warandpeace.html"
html = requests.get(url).text

ic(html)

bs = BeautifulSoup(html, 'lxml')

# find all the text in the span tag
name_list: list[Tag] = bs.find_all('span', {'class': ['green']})

ic(name_list)

for name in name_list:
    ic(name.get_text(), name.text)