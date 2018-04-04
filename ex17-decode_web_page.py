# need to go to bash shell
# then run:   pipenv install requests
# then run:   pipenv shell

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
r_html = r.text
# print(r_html)

soup = BeautifulSoup(r_html, "html.parser")
#for story_title in soup.find_all(class_ = 'story-heading'):
for story_title in soup.find_all(True , 'story-heading'):
    if story_title.a:
        #print(story_title.a.text.replace("\n", " ").strip())
        print(story_title.a.text.strip())
    else:
        print(story_title.contents[0].strip())

#for tag in soup.find_all('div'):
#tag = soup.li
#print(tag.name)
#print(tag.attrs)

