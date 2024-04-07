"""
Old computer jokes:
- you have a problem and then decide to use regular expression to solve it, now you have 2 problems
"""

import re
import requests

from bs4 import BeautifulSoup

html = requests.get('http://www.pythonscraping.com/pages/page3.html').text
bs = BeautifulSoup(html, 'lxml')

images = bs.find_all('img', {"src": re.compile('\.\.\/img\/gifts\/img.*\.jpg')})
for image in images:
    # attributes of tags can be accessed with the attrs attribute
    # this returns a dictionary of the attributes which can then be 
    # accessed with the normal dictionary key access
    print(image.attrs)
    print(image.attrs.get('src'))
    # i should note that i realized that attributes can be accessed directly from the tag as if the tag is itself a dictionary object
    print(image.get('src'))