
"""
https://www.practicepython.org

Exercise 34: Birthday Json
2 chilis

This exercise is Part 2 of 4 of the birthday data exercise series. The other exercises are:
Part 1, Part 3, and Part 4.

In the previous exercise we created a dictionary of famous scientists’ birthdays. In this
exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file
on disk, rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist’s name and birthday to add to the dictionary, and
update the JSON file you have on disk with the scientist’s name. If you run the program
multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.




This program works on exact matches to the name, so upper and lower case matter.
Given that some names do start with lower case (Vincent van Gogh) the number of
variations gets large and outside the scope of this exercise.
"""

import json
import sys

def get_birthdays(file_to_read):
    with open(file_to_read) as birthday_list_file:
       return(json.load(birthday_list_file))

def print_names(birthday_dictionary):
    print("\n\n We know the birthdays of:")
    [print(name) for name in birthday_dictionary]
    
def tell_birthdays(birthday_dictionary):
        name = input(" Who's birthday do you want to look up? ")
        date = birthday_dictionary.get(name, "not found")
        if date == "not found":
            print("\n\nWe don't have {}'s birthday".format(name))
        else:
            print("\n\n{}'s birthday was {}".format(name, date))

def add_name(bdate_dictionary, file):
    name = input("Who do you want to add? ")
    if name in bdate_dictionary:
        print("We already have " + name)
    else:
        date = input("What is the birthdate? ")
        bdate_dictionary[name] = date
        with open(file, 'w') as new_file:
            json.dump(bdate_dictionary, new_file)
    return()


if __name__ == '__main__':

    if len(sys.argv) == 2:
        file_name = str(sys.argv[1])
    else:
        file_name = 'birthdays.json'

    birthdays = get_birthdays(file_name)
    
    while True:
        next_action = input("\n What do you want to do now? (list, tell, add, quit) ")
        if next_action == "list":
            print_names(birthdays)
        elif next_action == "tell":
            tell_birthdays(birthdays)
        elif next_action == "add":
            add_name(birthdays, file_name)
        else:
            break
