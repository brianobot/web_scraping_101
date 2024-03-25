from urllib.request import urlopen
from urllib.error import HTTPError, URLError

from bs4 import BeautifulSoup

from icecream import ic

# catching errors related to the requests process
try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    ic(e)
except URLError as e:
    ic(e)
else:
    bs = BeautifulSoup(html.read(), 'lxml')
    ic(bs.body.div)


# catching errors related to the parsing process
"""
it is important to note that calling a tag on a BeautifulSoup object that does not exist will return None
and trying to access a tag on None will raise an AttributeError.
"""
try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
    bs = BeautifulSoup(html.read(), 'lxml')
    title = bs.h1
except AttributeError as e:
    ic(e)