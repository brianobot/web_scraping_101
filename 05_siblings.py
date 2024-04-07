import requests
from bs4 import BeautifulSoup


html = requests.get('http://www.pythonscraping.com/pages/page3.html').text

bs = BeautifulSoup(html, 'lxml')
table = bs.find('table', {'id': 'giftList'})

for sibling in table.tr.next_siblings:
    print(f"{sibling = }")

"""
In addition to the next_siblings property
there is a previoud_siblings property that does the same thing in the order direction
there is also a next_sibling and previous_sibling property that return a single tag
"""