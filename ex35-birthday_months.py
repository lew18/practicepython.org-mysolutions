
"""
https://www.practicepython.org
MichelePratusevich

Exercise 35: Birthday Months
2 chilis

This exercise is Part 3 of 4 of the birthday data exercise series. The other exercises are:
Part 1, Part 2, and Part 4.

In the previous exercise we saved information about famous scientists’ names and birthdays
to disk. In this exercise, load that JSON file from disk, extract the months of all the
birthdays, and count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}


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

    # the above works, but output clunky because monthly data should be in calendar order.
    # plus, don't have a month for Fibonacci, don't want to include his data

    months = Counter([item.split()[0] for item in birthdays.values()])
    for k, v in months.items():
        if k == "January":
            print(k, v)
    
    for k, v in months.items():
        if k == "February":
            print(k, v)
    
    for k, v in months.items():
        if k == "March":
            print(k, v)
    
    for k, v in months.items():
        if k == "April":
            print(k, v)
    
    for k, v in months.items():
        if k == "May":
            print(k, v)
    
    for k, v in months.items():
        if k == "June":
            print(k, v)
    
    for k, v in months.items():
        if k == "July":
            print(k, v)
    
    for k, v in months.items():
        if k == "August":
            print(k, v)
    
    for k, v in months.items():
        if k == "September":
            print(k, v)
    
    for k, v in months.items():
        if k == "October":
            print(k, v)
    
    for k, v in months.items():
        if k == "November":
            print(k, v)
    
    for k, v in months.items():
        if k == "December":
            print(k, v)
