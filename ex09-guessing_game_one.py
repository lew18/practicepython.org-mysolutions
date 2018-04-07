"""
https://www.practicepython.org

Exercise 9: Guessing Game One
3 chilis

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:
- Keep the game going until the user types "exit"
- Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""

import random

guesses = guess = 0
target = random.randint(1, 9)

while guess != target and guess != 'exit':
    print("enter your guess between 1 and 9, inclusive:")
    guess = input("(type 'exit' to exit)  ")
    if guess != 'exit':
        guess = int(guess)
        guesses += 1
        if guess < target:
            print("too low ")
        elif guess > target:
            print("too high ")
        else:
            print("That's it. ")
            print("You made %d guesses" % guesses)
            guesses = guess = 0
            target = random.randint(1, 9)

