
"""
practice exercises from Michele Pratusevich on https://www.practicepython.org

"""

def get_birthdays(file = 'birthdays.txt'):
    birthdays = { }
    with open(file) as birthday_list_file:
        entry = birthday_list_file.readline().split(':')
        while len(entry) == 2:
            birthdays[str(entry[0])] = str(entry[1])
            entry = birthday_list_file.readline().split(':')
    return(birthdays)

# Michele's sample solutions used
#           if name in birthdays
# instead of .get(), which makes sense given the list comprehension works
def tell_birthdays(birthday_dictionary):
    while True:
        print(">>> Welcome to the birthday dictionary. We know the birthdays of:")
        [print(name) for name in birthday_dictionary]
        name = input(">>> Who's birthday do you want to look up? ")
        if name.lower() in ("exit", "done", "quit"):
            return()
        date = birthday_dictionary.get(name, "not found")
        if date == "not found":
            date = birthday_dictionary.get(name.title(), "not found")
            if date == "not found":
                print("\n\nWe don't have {}'s birthday".format(name))
            else:
                print("\n\n{}'s birthday is {}".format(name.title(), date))
        else:
            print("\n\n{}'s birthday is {}".format(name, date))

if __name__ == '__main__':
    birthdays = get_birthdays()
    tell_birthdays(birthdays)
