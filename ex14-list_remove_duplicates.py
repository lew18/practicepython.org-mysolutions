"""
https://www.practicepython.org

Exercise 14: List Remove Duplicates
2 chilis

Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.

Extras:
- Write two different functions to do this - one using a loop and constructing
  a list, and another using sets.
- Go back and do Exercise 5 using sets, and write the solution for that in a different function.

"""

def remove_common_items(list1):
    answer = [ ]
    for item in list1:
        if item not in answer:
            answer.append(item)
    return answer


def rci2(list1):
    return [list1[idx] for idx in range(len(list1)) if list1[idx] not in list1[idx+1:]]

def rci3(list1, list2):
    return set(list1 + list2)


a = [1, 1, 2, 3, 5, 8, 8, 4, 21, 34, 5, 7, 6, 8, "sdfg", "rstl"]
b = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "sdfg", "zyxw"]

common_list = remove_common_items(a + b)
print(common_list)

common_list = rci2(a + b)
print(common_list)

common_list = rci3(a, b)
print(common_list)

