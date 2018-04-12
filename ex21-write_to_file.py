"""
https://www.practicepython.org

Exercise 21: Write to a File
1 chili

Take the code from the How To Decode A Website exercise (if you didn’t
do it or just want to play with some different code, use the code from
the solution), and instead of printing the results to a screen, write
the results to a txt file. In your code, just make up a name for the
file you are saving to.

Extras:

- Ask the user to specify the name of the output file that will be saved.

"""
# need to go to bash shell
# then run:   pipenv shell
# then run:   pip install requests
# then run    pip install beautifulsoup4


import requests
from bs4 import BeautifulSoup

fn = str(input("what file name? "))
with open(fn, 'w') as file_to_write:
    url = 'http://www.nytimes.com'
    r = requests.get(url)
    r_html = r.text
    page = BeautifulSoup(r_html, "html.parser")

    story_titles = page.find_all(class_ = 'story-heading')
    for story_title in story_titles:
        if story_title.a:
            file_to_write.write(story_title.a.text.strip())
        else:
            file_to_write.write(story_title.contents[0].strip())
        file_to_write.write('\n')



