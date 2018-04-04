""" 
exercise 31, guess a random word from sowpos.webarchive
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
    answer = [' ']* len(word)
    misses = [ ]
    mistakes = 0
    while ' ' in answer and mistakes < 7:
        print("\n answer is " + str(answer))
        print("mistakes so far " + str(misses))
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
                misses.append(letter)
                mistakes += 1
            
    if mistakes < 7:
        print('You guessed ' + word + ' with only ' + str(mistakes) + ' wrong guesses')
    else:
        print('The word is ' + word)

if __name__ == '__main__':
    
    word_list = get_word_list('sowpods.webarchive')
    word = word_list[random.randint(0, len(word_list) - 1)]

    play_hangman(word)
