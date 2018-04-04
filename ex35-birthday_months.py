
"""
practice exercises from Michele Pratusevich on https://www.practicepython.org
This program works on exact matches to the name, so upper and lower case matter.
Given that some name do start with lower case (Vincent van Gogh) the number of variations gets large
and outside the scope of this exercise.
Turns out I made this easier by having the dates in mmm dd, yyy format instead
of her original mm/dd/yyyy format. With the latter format, have to translate the numbers
into text somewhere.
"""

import json
import sys
from collections import Counter

def get_birthdays(file):
    with open(file) as birthday_list_file:
       return(json.load(birthday_list_file))

if __name__ == '__main__':

    if len(sys.argv) == 2:
        file = str(sys.argv[1])
    else:
        file = 'birthdays.json'
    birthdays = get_birthdays(file)
    print(Counter([item.split()[0] for item in birthdays.values()]))

