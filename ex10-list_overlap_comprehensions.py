"""
https://www.practicepython.org

Exercise 10: List Overlap Comprehensions
2 chilis

This week’s exercise is going to be revisiting an old exercise (see Exercise 5),
except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on
two lists of different sizes. Write this in one line of Python using at least one
list comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one
line of Python, but a few readers pointed out that this was impossible to do
without using sets that I had not yet discussed on the blog, so you can either
choose to use the original directive and read about the set command in Python
3.3, or try to implement this on your own and use at least one list
comprehension in the solution.

Extra:

- Randomly generate two lists to test this
"""

import random

def find_common_items(list1, list2):
    answer = [ ]

    for item in list1:
        if item in list2 and item not in answer:
            answer.append(item)

    return(answer)


def find2(list1, list2):
    return([list1[idx] for idx in range(len(list1)) if list1[idx] in list2 and list1[idx] not in list1[idx+1:]])


a = [1, 1, 2, 3, 5, 8, 8, 4, 21, 34, 5, 7, 6, 8, "sdfg", "sdfg"]
b = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "sdfg", "sdfg"]

common_list = find_common_items(a, b)
print(common_list)

common_list = find2(a, b)
print(common_list)

print([a[idx] for idx in range(len(a)) if a[idx] in b and a[idx] not in a[idx+1:]])

count = random.randint(1, 25)
c = random.sample(range(100), count)
count = random.randint(1, 25)
d = random.sample(range(100), count)

print('c is ' + str(c))
print('d is ' + str(d))
e = find2(c, d)
print('e is ' + str(e))
