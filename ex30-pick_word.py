""" 
exercise 30, pick a random word from sowpos.webarchive
One of Michele's samples has
words = list(word_file)
which is pretty sweet, but it doesn't strip out the /n

and random_word_index could be one line instead of 2
"""

import random

if __name__ == '__main__':
    word_list = []
    with open('sowpods.webarchive', 'r') as word_file:
        word = word_file.readline().strip()
        while word:
            word_list.append(word)
            word = word_file.readline().strip()

    random_word_index = random.randint(0, len(word_list))
    print('random word is ' + word_list[random_word_index])
