# need to go to bash shell
# then run:   pipenv install requests
# then run:   pipenv shell

import requests
from bs4 import BeautifulSoup

url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text
# print(r_html)

soup = BeautifulSoup(r_html, "html.parser")
#for para in soup.find_all('section', 'p'):
#    print("found something")
#    print(para)


for story_content in soup.find_all('section'):
    for para in story_content.find_all('p'):
        print(para.text)

# the below works better because it somehow excludes the privacy policy statement at the end
#print("\n\n her answer, modified \n\n")

#all_p_cn_text_body = soup.select("section > p")
#for elem in all_p_cn_text_body:
#    print(elem.text)


