
def remove_common_items(list1):

    answer = [ ]

    for item in list1:
        if item not in answer:
            answer.append(item)

    return(answer)


def rci2(list1):

    return([list1[idx] for idx in range(len(list1)) if list1[idx] not in list1[idx+1:]])

def rci3(list1):
    return(list(set(list1[:])))


a = [1, 1, 2, 3, 5, 8, 8, 4, 21, 34, 5, 7, 6, 8, "sdfg", "sdfg"]
b = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "sdfg", "sdfg"]

common_list = remove_common_items(a)
print(common_list)

common_list = rci2(b)
print(common_list)

common_list = rci3(a+b)
print(common_list)


