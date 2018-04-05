"""
https://www.practicepython.org

Exercise 1: Character Input
1 chile
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they
will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and
   printing out that many copies of the previous message. (Hint: order of
   operations exists in Python)
2. Print out that many copies of the previous message on separate lines.
   (Hint: the string "\n is the same as pressing the ENTER button)

"""

from datetime import date

today = date.today()
name = input("what is your name? ")
age = int(input("how old are you? "))
if (str(input("Have you had your birthday this year? ")) == "y"):
    message = (name + " will be 100 years old in " + str(today.year + 100 - age))
else:
    # yes, this is strange. The primary purpose is to learn python, so experiment some
    message = ("%s will be 100 years old in %4d." % (name, today.year + 99 - age))

message_count = int(input("How many times do you want to see the message? "))
while message_count > 0:
    print(message)
    message_count -= 1
