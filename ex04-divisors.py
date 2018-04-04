def divisors(number):
    # initialize
    answer = [ ]
    i=0
    candidates = list(range(1, int(number**0.5)))

    # find the answers
    for i in candidates:
        if number % i == 0:
            answer.append(i)
            answer.append(int(number / i))

    # if i is the sq rt of number, add i to the list
    if (i+1) == number**0.5:
        answer.append(i+1)

    # print the results
    if len(answer) <=2:
        print("%d is prime! " % number)
    else:
        print("%d has %d divisors: " % (number, len(answer)))
        answer.sort()
        print(answer)


number = int(input("Please choose a number: "))
divisors(number)

