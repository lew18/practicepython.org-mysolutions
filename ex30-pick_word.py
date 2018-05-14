"""
https://www.practicepython.org

Exercise 30: Pick word
2 chilis

This exercise is Part 1 of 3 of the Hangman exercise series. The
other exercises are: Part 2 and Part 3.

In this exercise, the task is to write a function that picks a
random word from a list of words from the SOWPODS dictionary.
Download this file and save it in the same directory as your
Python code. This file is Peter Norvig’s compilation of the
dictionary of words used in professional Scrabble tournaments.
Each line in the file contains a single word.

Hint: use the Python random library for picking a random word.

One of Michele's samples has
words = list(word_file)
which is pretty sweet, but it doesn't strip out the /n

and random_word_index could be one line instead of 2
"""

import random

if __name__ == '__main__':
    word_list = []
    with open('sowpods.txt', 'r') as word_file:
        word = word_file.readline().strip()
        while word:
            word_list.append(word)
            word = word_file.readline().strip()

    random_word_index = random.randint(0, len(word_list))
    print('random word is ' + word_list[random_word_index])
