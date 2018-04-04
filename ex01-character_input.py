
from datetime import date

today = date.today()
name = str(input("what is your name? "))
age = int(input("how old are you? "))
if (str(input("Have you had your birthday this year? ")) == "y"):
    print(name + " will be 100 years old in " + str(today.year + 100 - age))
else:
    print("%s will be 100 years old in %4d." % (name, today.year + 99 - age))

