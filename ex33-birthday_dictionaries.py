"""
https://www.practicepython.org

Exercise 33: Birthday Dictionaries
1 chili

This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are:
Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend’s birthdays are, and be able to
find that information based on their name. Create a dictionary (in your file) of names
and birthdays. When you run your program it should ask the user to enter a name, and return
the birthday of that person back to them. The interaction should look something like this:

>>> Welcome to the birthday dictionary. We know the birthdays of:
Albert Einstein
Benjamin Franklin
Ada Lovelace
>>> Who's birthday do you want to look up?
Benjamin Franklin
>>> Benjamin Franklin's birthday is 01/17/1706.
Happy coding!


# Michele's sample solutions used
#           if name in birthdays
# instead of .get(), which makes sense given the list comprehension works

"""

def get_birthdays(file = 'birthdays.txt'):
    birthdays = { }
    with open(file) as birthday_list_file:
        entry = birthday_list_file.readline().split(':')
        while len(entry) == 2:
            birthdays[str(entry[0])] = str(entry[1])
            entry = birthday_list_file.readline().split(':')
    return(birthdays)

def tell_birthdays(birthday_dictionary):
    while True:
        print(">>> Welcome to the birthday dictionary. We know the birthdays of:")
        [print(name) for name in birthday_dictionary]
        name = input(">>> Who's birthday do you want to look up? (or exit) ")
        if name.lower() == "exit":
            break
        
        date = birthday_dictionary.get(name, "not found")
        if date == "not found":
            print("\n\nWe don't have {}'s birthday".format(name))
        else:
            print("\n\n{}'s birthday is {}".format(name, date))

if __name__ == '__main__':
    birthdays = get_birthdays()
    tell_birthdays(birthdays)
