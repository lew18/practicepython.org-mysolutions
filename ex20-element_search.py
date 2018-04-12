"""
https://www.practicepython.org

Exercise 20: Element Search
1 chili

Write a function that takes an ordered list of numbers (a list where
the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list
and returns (then prints) an appropriate boolean.

Extras:

Use binary search.

"""

def straight_search(elem_to_find, list_to_search):
    for elem in list_to_search:
        if elem_to_find == elem:
            return(True)
    return(False)

def binary_search(elem_to_find, list_to_search):
    start_of_range = 0
    end_of_range = len(list_to_search)

    while start_of_range < end_of_range:
        idx = int((start_of_range + end_of_range) / 2)
        if list_to_search[idx] == elem_to_find:
            return(True)
        elif elem_to_find < list_to_search[idx]:
            end_of_range = idx
        elif elem_to_find > list_to_search[idx]:
            if idx == start_of_range:
                start_of_range += 1
            else:
                start_of_range = idx
    return(False)


def one_line_search(elem_to_find, list_to_search):
    return elem_to_find in list_to_search


if __name__ == "__main__":
    # generate the list
    lts = sorted([-15, -5, 4, 6, 9, 13, 22, 56, 345, 456, 777, 778, 122, -7])

    # generate the number to search
    number = int(input("Please choose a integer: "))

    # now see if the number is in the list using all three methods

    print(straight_search(number, lts))
    print(binary_search(number, lts))
    print(one_line_search(number, lts))
