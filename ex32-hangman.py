""" 
exercise 31, guess a random word from sowpos.webarchive
Michele used sets instead of lists
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
    misses = [ ]
    while '_' in answer and len(misses) < 6:
        display_gallows(len(misses))
        print("\n answer is " + "".join(answer))
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
            
    if len(misses) < 6:
        print('You guessed ' + word + ' with only ' + str(len(misses)) + ' wrong guesses')
    else:
        display_gallows(len(misses))
        print('The word is ' + word + ", better luck next time.")

if __name__ == '__main__':
    
    word_list = get_word_list('sowpods.webarchive')
    word = word_list[random.randint(0, len(word_list) - 1)]

    play_hangman(word)
