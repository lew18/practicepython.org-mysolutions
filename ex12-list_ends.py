"""
https://www.practicepython.org

Exercise 12: List Ends
1 chili

Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
and makes a new list of only the first and last elements of the given list. For
practice, write this code inside a function.

"""
def first_last(start_list):
    return [start_list[i] for i in [0, len(start_list) - 1] if len(start_list) > 0]

def first_last_v2(start_list):
    if len(start_list) > 0:
        return [start_list[0], start_list[-1] ]
    return[]

a = [ 1, 2, 3, 4, 5 ]
print(first_last(a))
print(first_last_v2(a))

b = [5]
print(first_last(b))
print(first_last_v2(b))

c = []
print(first_last(c))
print(first_last_v2(c))
