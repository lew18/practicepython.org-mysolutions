def straight_search(elem_to_find, list_to_search):
    for elem in list_to_search:
        if elem_to_find == elem:
            return(True)
    return(False)

def binary_search(elem_to_find, list_to_search):
    found = False
    more_to_search = True
    start_of_range = 0
    end_of_range = len(list_to_search) - 1

    while found == False and more_to_search:
        idx = int((start_of_range + end_of_range) / 2)
        if list_to_search[idx] == elem_to_find:
            found = True
        elif start_of_range >= end_of_range:
            more_to_search = False
        elif elem_to_find > list_to_search[idx]:
            if idx == start_of_range:
                start_of_range += 1
                # start_of_range = end_of_range does the same thing at this point
            else:
                start_of_range = idx
        elif elem_to_find < list_to_search[idx]:
            end_of_range = idx

    return(found)



if __name__ == "__main__":
    # generate the list
    lts = sorted([-15, -5, 4, 6, 9, 13, 22, 56, 345, 456, 777, 778, 122, -7])

    # generate the number to search
    number = int(input("Please choose a integer: "))

    # now see if the number is in the list using all three methods

    print(straight_search(number, lts))
    print(binary_search(number, lts))


