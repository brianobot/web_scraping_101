import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.pythonscraping.com/pages/page3.html').text

bs = BeautifulSoup(html, 'lxml')

# parents: 부모 태그를 리스트로 반환
image_parent = bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent

image_grand_parent = image_parent.parent

print(f"{image_parent = }")
print(f"{image_grand_parent = }")

