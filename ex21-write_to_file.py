# need to go to bash shell
# then run:   pipenv install requests    only if requests isn't already installed
# then run:   pipenv shell

import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com'
r = requests.get(url)
r_html = r.text
# print(r_html)

page = BeautifulSoup(r_html, "html.parser")

story_titles = page.find_all(class_ = 'story-heading')   # or put this directl in the for loop

fn = str(input("what file name? "))
with open(fn, 'w') as file_to_write:
    for story_title in story_titles:
        if story_title.a:
            file_to_write.write(story_title.a.text.strip())
        else:
            file_to_write.write(story_title.contents[0].strip())
        file_to_write.write('\n')



