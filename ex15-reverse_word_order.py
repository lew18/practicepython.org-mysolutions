"""
https://www.practicepython.org

Exercise 15: Reverse Word Order
3 chilis

Write a program (using functions!) that asks the user for a
long string containing multiple words. Print back to the user
the same string, except with the words in backwards order.
For example, say I type the string:

  My name is Michele

Then I would see the string:

  Michele is name My

shown back to me.
"""
def rs(input_string):
    answer = [input_string[i] for i in range(len(input_string) - 1, -1, -1)]
    print(' '.join([str(i) for i in answer]))

a = input("input a string of words: " )
a = a.split()
rs(a)

# or
print(' '.join([str(i) for i in a[::-1]]))

print(' '.join(a[::-1]))
