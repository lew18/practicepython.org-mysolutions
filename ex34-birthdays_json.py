
"""
practice exercises from Michele Pratusevich on https://www.practicepython.org
This program works on exact matches to the name, so upper and lower case matter.
Given that some name do start with lower case (Vincent van Gogh) the number of variations gets large
and outside the scope of this exercise.
"""

import json
import sys

def get_birthdays(file):
    with open(file) as birthday_list_file:
       return(json.load(birthday_list_file))

def add_name(bdate_dictionary, file):
    name = input("What is the name? ")
    if name in bdate_dictionary:
        print("We already have " + name)
    else:
        date = input("What is the birthdate? ")
        bdate_dictionary[name] = date
        with open(file, 'w') as new_file:
            json.dump(bdate_dictionary, new_file)
    return()

def tell_birthdays(birthday_dictionary, file):
    while True:
        print("\n\n>>> Welcome to the birthday dictionary. We know the birthdays of:")
        [print(name) for name in birthday_dictionary]
        name = input(">>> Who's birthday do you want to look up? ")
        date = birthday_dictionary.get(name, "not found")
        if date == "not found":
            print("\n\nWe don't have {}'s birthday".format(name))
        else:
            print("\n\n{}'s birthday was {}".format(name, date))
        
        if input("\nDo you want to add a name (y/n)? ") == 'y':
            add_name(birthday_dictionary, file)
        if input("\nDo you want to quit (y/n)? ") == 'y':
            return


if __name__ == '__main__':

    if len(sys.argv) == 2:
        file = str(sys.argv[1])
    else:
        file = 'birthdays.json'
    birthdays = get_birthdays(file)
    tell_birthdays(birthdays, file)
