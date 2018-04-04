
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


