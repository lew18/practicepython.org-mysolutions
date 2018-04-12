"""
https://www.practicepython.org

Exercise 22: Read from a File
1 chili

Given a .txt file that has a list of a bunch of names, count how many of each
name there are in the file, and print out the results to the screen. I have a
.txt file for you, if you want to use it!

Extra:

- Instead of using the .txt file from above (or instead of, if you want the challenge),
  take this .txt file, and count how many of each “category” of each image there are.
  This text file is actually a list of files corresponding to the SUN database scene
  recognition database, and lists the file directory hierarchy for the images. Once you
  take a look at the first line or two of the file, it will be clear which part
  represents the scene category. To do this, you’re going to have to remember a bit
  about string parsing in Python 3. I talked a little bit about it in this post.

"""
# Michele's solution used .readline() and a while loop to read a line at a time, which if only
# one word / name per line is reasonable.

def print_dictionary(dictionary):
    for word, count in dictionary.items():
        print('"' + word + '"' + ' appears ' + str(count) + ' time', end='')
        if count > 1:
            print('s')
        else:
            print('')

def count_words():
    ftr = 'last.txt'
    with open(ftr, 'r') as file_to_read:
        dict = { }
        words_read = file_to_read.read()
        for word in words_read.split():
            word = word.lower()
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1

    # now print out the dictionary
    print_dictionary(dict)

def count_words_extra():
    fptr = 'Training_01.webarchive'
    #fptr = 'T2.txt'
    with open(fptr, 'r') as file_to_read:
        dict = {}
        for line in file_to_read.readlines():
            word = line.split('/')[2]
            if word in dict:
                dict[word] += 1
            else:
                dict[word] = 1

    # now print out the dictionary
    print_dictionary(dict)

if __name__ == '__main__':
    #count_words()
    count_words_extra()
