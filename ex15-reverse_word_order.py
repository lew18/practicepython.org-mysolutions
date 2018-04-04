def rs(input_string):

    s1 = input_string.split()
    answer = [s1[i] for i in range(len(s1) - 1, -1, -1)]
    print(' '.join([str(i) for i in answer[:]]))

a = str(input("input a string of words:" ))
rs(a)

