import requests
from bs4 import BeautifulSoup


html = requests.get('http://www.pythonscraping.com/pages/page3.html').text
bs = BeautifulSoup(html, 'lxml')

# children: 자식 태그를 리스트로 반환
print(f"{bs.children = }")


for child in bs.find('table', {'id': 'giftList'}).children:
    print(f"{child = } ")