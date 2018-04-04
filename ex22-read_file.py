# her solution used .readline() and a while loop to read a line at a time, which if only
# one word / name per line is reasonable.

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
        for word, count in dict.items():
            print('"' + word + '"' + ' appears ' + str(count) + ' time', end='')
            if count > 1:
                print('s')
            else:
                print('')


if __name__ == '__main__':
    count_words()
