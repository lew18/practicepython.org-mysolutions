"""
https://www.practicepython.org

Exercise 19: Decode a Web Page two
4 chilis

Using the requests and BeautifulSoup Python libraries, print to the screen the
full text of the article on this website:
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print
out the text to the screen so that you can read the full article without having
to click any buttons.

(Hint: The post here describes in detail how to use the BeautifulSoup and
requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen. It will not
make it easy to read, so next exercise we will learn how to write this text to a .txt file.

"""

# need to go to bash shell
# then run:   pipenv shell
# then run:   pip install requests
# then run    pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
# print(r_html)

soup = BeautifulSoup(r_html, "html.parser")
for story_content in soup.find_all('section'):
    for para in story_content.find_all('p'):
        print(para.text)

# the below works better because it excludes the privacy policy statement at the end
#print("\n\n her answer, modified \n\n")

#all_p_cn_text_body = soup.select("section > p")
#for elem in all_p_cn_text_body:
#    print(elem.text)


