"""
with the lessons picked up from the previous script, we can now get the titles of the articles
"""

from bs4 import BeautifulSoup
import requests
from icecream import ic
import asyncio
import json


def get_title(url: str) -> str | None:
    """
    Get the title of a webpage as specified by the H1 tag
    """
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return None
    try:
        bs = BeautifulSoup(response.text, 'lxml')
        title = bs.h1
    except AttributeError as e:
        print(e)
        return None
    return title
    

urls = [
    'http://www.pythonscraping.com/pages/page1.html',
    'http://www.pythonscraping.com/pages/page2.html',
    'http://www.pythonscraping.com/pages/page3.html',
    'http://www.pythonscraping.com/pages/page4.html',
    'http://www.pythonscraping.com/pages/page5.html',
    'http://www.pythonscraping.com/pages/page6.html',
]

async def main():
    titles = {}
    for url in urls:
        title = await asyncio.to_thread(get_title, url)
        # always try to access the text attribute of the title tag just before storing it
        titles[url] = title.text if title else None
        ic(url, title)
    
    ic(titles)
    json.dump(titles, open('titles.json', 'w'))

asyncio.run(main())