import re
import requests
from bs4 import BeautifulSoup


url = "https://brianobot.github.io"

html = requests.get(url).text
bs = BeautifulSoup(html, "lxml")

tags_with_brian = bs.find_all(lambda tag: "brian" in tag.text.lower())

wikipedia_url = "http://en.wikipedia.org/wiki/Kevin_Bacon"
html = requests.get(wikipedia_url).text

bs = BeautifulSoup(html, "lxml")
links = bs.find_all('a')

images = bs.find_all('img')


for link in links:print(link.attrs.get('href'))
for image in images:print(image.attrs.get('src'))

print(f"\nNumber of Image found = {len(images)}")
print(f"\nNumber of Links found = {len(links)}")


# Even more effectively we can work with the understanding that links on wikipedia follow certain patterns
# article links contains the following features
# • They reside within the div with the id set to bodyContent.
# • The URLs do not contain colons.
# • The URLs begin with /wiki/.

article_links = bs.find('div', {'id': "bodyContent"}).find_all('a', {'href': re.compile('(/wiki/)((?!:).)*$')})

for link in article_links:
    print(link.attrs.get('href'))