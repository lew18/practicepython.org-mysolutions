""" 
https://www.practicepython.org

Exercise 32: Hangman
2 chilis

This exercise is Part 3 of 3 of the Hangman exercise series. The other exercises are: Part 1 and Part 2.

You can start your Python journey anywhere, but to finish this exercise you will have to have finished
Parts 1 and 2 or use the solutions (Part 1 and Part 2).

In this exercise, we will finish building Hangman. In the game of Hangman, the player only has 6
incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.

In Part 1, we loaded a random word list and picked a word from it. In Part 2, we wrote the logic for
guessing the letter and displaying that information to the user. In this exercise, we have to put it
all together and add logic for handling guesses.

Copy your code from Parts 1 and 2 into a new file as a starting point. Now add the following features:

Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t
penalize them - let them guess again.
Optional additions:

When the player wins or loses, let them start a new game.
Rather than telling the user "You have 4 incorrect guesses left", display some picture art for the
Hangman. This is challenging - do the other parts of the exercise first!
Your solution will be a lot cleaner if you make use of functions to help you!

she also has this     print("You have {} guesses left".format(6 - num_guesses))
"""

import random

def get_word_list(file_to_read):
    word_list = [ ]
    with open(file_to_read, 'r') as word_file:
        word = word_file.readline().strip()
        while word:
            word_list.append(word)
            word = word_file.readline().strip()
    return(word_list)

def display_gallows(misses):
    print("  ____")
    print("  |  |")
    if misses > 0:
        print("  |  o")
    else:
        print("  |   ")
    if misses >= 4:
        print("  | -|- ")
    elif misses == 3:
        print("  | -|  ")
    elif misses == 2:
        print("  |  |  ")
    else:
        print("  |   ")
    if misses == 5:
        print("  | / ")
    elif misses == 6:
        print("  | / \\ ")
    else:
        print("  |   ")
    print("__|____")
    

def play_hangman(word):
    char_list = list(word)
    answer = ['_']* len(word)
    misses = set()
    while '_' in answer and len(misses) < 6:
        display_gallows(len(misses))
        print("\nanswer is " + "".join(answer) + " (" + str(len(answer)) + " letters)")
        if len(misses):
           print(str(len(misses)) + " mistakes so far " + str(misses) + ", max # of mistakes is 6")
        letter = input('Guess a letter ').upper()
        if letter in answer or letter in misses:
            print("you already guessed " + letter)
        else:
            found = False
            for i in range(len(char_list)):
                if char_list[i] == letter:
                    answer[i] = letter
                    found = True
            if not found:
                misses.add(letter)
            
    if len(misses) < 6:
        print('\nYou won, you figured out ' + word)
    else:
        display_gallows(len(misses))
        print('\nThe word was ' + word + ", better luck next time.")

if __name__ == '__main__':
    
    word_list = get_word_list('sowpods.txt')
    word = word_list[random.randint(0, len(word_list) - 1)]

    play_hangman(word)
