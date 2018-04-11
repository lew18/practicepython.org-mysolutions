"""
https://www.practicepython.org

Exercise 16: Reverse Word OrderPassword Generator
4 chilis

Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random, generating
a new password every time the user asks for a new password. Include your
run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak
passwords, pick a word or two from a list.

"""

import random
import string


def generate_password(length = 4):
    choices = [string.punctuation,
               string.digits,
               string.ascii_lowercase,
               string.ascii_uppercase]
    password = []
    
    # first, include one of each type
    for group in choices:
        password.append(group[random.randint(0, len(group) - 1)])

    # next, fill out the password to the desired length
    for i in range(length - len(choices)):
        group = random.randint(0, len(choices)-1)
        index = random.randint(0, len(choices[group])-1)
        password.append(choices[group][index])

    # shuffle the characters
    for i in range(7):
        for original_position in range(len(password)):
            password.insert(random.randint(0, len(password) - 1),
                            password.pop(original_position))
        
    # assemble into one text string
    return ''.join([str(i) for i in password])


length = 15
new_password = generate_password(length)
print(new_password)

# I"m being lazy, solution to exercise 31 shows how to pick a random word.

# one solution put all of the characters into one long string then does
# p =  "".join(random.sample(s, 8))

# another uses return ''.join(random.choice(chars) for _ in range(size))
# along with string.ascii_letters, string.digits, and string.punctuation
# so I copied part of that, originally listed out the digits and a string of symbols
# also, notice the _
#
# problem with these solutions is they don't force presence
# of at least one of each type of the four classifications.
