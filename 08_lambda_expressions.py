"""
Beautiful Soup allows lambda expressions in most of it methods
to better allow for confitional filterations of tags,

the lambda expression must tag a compulsory argument which is the tag
object and must evaluate to a boolean
"""

from bs4 import BeautifulSoup
import requests


html = requests.get('http://www.pythonscraping.com/pages/page3.html').text
bs = BeautifulSoup(html, 'lxml')

tags_with_2_attrs = bs.find_all(lambda tag: len(tag.attrs) == 2)

for tag in tags_with_2_attrs:
    print(tag)