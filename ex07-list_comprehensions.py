"""
https://www.practicepython.org

Exercise 7: List Comprehensions
2 chilis

Let’s say I give you a list saved in a variable:

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].

Write one line of Python that takes this list a and makes a
new list that has only the even elements of this list in it.
"""


a = [i**2 for i in range(1, 11)]

even_numbers = [number for number in a if number % 2 == 0]

print(even_numbers)
