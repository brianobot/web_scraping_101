import re
import random
import requests
from datetime import datetime
from bs4 import BeautifulSoup, Tag


random.seed(str(datetime.now()))


def get_articles(article_url: str) -> list[Tag]:
    url = f"http://en.wikipedia.org{article_url}"
    html = requests.get(url).text
    bs = BeautifulSoup(html, "lxml")

    return bs.find("div", {"id": "bodyContent"}).find_all('a', {'href': re.compile('^(/wiki/)((?!:).*$)')})


def main():
    file = open("start_data.txt")
    
    url = file.readline()
    file.close()

    links = get_articles(url)

    while len(links) > 0:
        new_article = random.choice([link.attrs.get("href") for link in links])
        print(new_article)
        links = get_articles(new_article)


if __name__ == "__main__":
    main()