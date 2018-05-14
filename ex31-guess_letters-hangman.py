""" 
https://www.practicepython.org

Exercise 31: Guess Letters
2 chilis

This exercise is Part2 of 3 of the Hangman exercise series. The other exercises
are: Part 1 and Part 3.

Let’s continue building Hangman. In the game of Hangman, a clue word is given
by the program that the player has to guess, letter by letter. The player guesses
one letter at a time until the entire word has been guessed. (In the actual game,
the player can only guess 6 letters incorrectly before losing).

Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
write the logic that asks a player to guess a letter and displays letters in
the clue word that were guessed correctly. For now, let the player guess an
infinite number of times until they get the entire word. As a bonus, keep track
of the letters the player guessed and display a different message if the player
tries to guess that letter again. Remember to stop the game when all the letters
have been guessed correctly! Don’t worry about choosing a word randomly or
keeping track of the number of guesses the player has remaining - we will deal
with those in a future exercise.

An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on, until the player gets the word.


first line of Michele's file is #! /usr/bin/python3
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

def play_hangman(word):
    char_list = list(word)
    answer = ['_'] * len(word)
    mistakes = [ ]
    while '_' in answer and len(mistakes) < 7:
        print("\n answer is " + ''.join(answer) + " (" + str(len(word)) + " letters)")
        print("mistakes so far " + ''.join(mistakes))
        letter = input('Guess a letter ').upper()
        if letter in answer or letter in mistakes:
            print("you already guessed " + letter)
        else:
            found = False
            for i in range(len(char_list)):
                if char_list[i] == letter:
                    answer[i] = letter
                    found = True
            if not found:
                mistakes.append(letter)
            
    if len(mistakes) < 7:
        print('You guessed ' + word + ' with ' + str(len(mistakes)) + ' wrong guesses')
    else:
        print('The word is ' + word)

if __name__ == '__main__':
    
    word_list = get_word_list('sowpods.txt')
    word = word_list[random.randint(0, len(word_list) - 1)]

    play_hangman(word)
