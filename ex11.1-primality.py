def divisors(number, print_divisors=True, print_prime=True):

    if not print_divisors and not print_prime:
        print("Nothing to do, returning.")
        return

    # initialize
    answer = [ ]
    i=0
    if (int(number**0.5))**2 == number:
        candidates = list(range(1, int(number**0.5)))
    else:
        candidates = list(range(1, int(number**0.5) + 1))

    # find the answers
    for i in candidates:
        if number % i == 0:
            answer.append(i)
            answer.append(int(number / i))

    answer2 = [i for i in candidates if number % i == 0]
    print(answer2)
    answer2 = answer2 + sorted([int(number / i) for i in answer2 if number % i == 0])
    print(answer2)

    if (int(number**0.5))**2 == number:
        answer2.insert(int(len(answer2)/2), int(number**0.5))
    print(answer2)

    # if i is the sq rt of number, add i to the list
    if (i+1) == number**0.5:
        answer.append(i+1)

    # print the results
    if print_prime:
        if len(answer) <=2 :
            print("%d is prime. " % number)
        else:
            print("%d is not prime. " % number)

    if print_divisors:
        if len(answer) > 2 :
            print("%d has %d divisors: " % (number, len(answer)))
            answer.sort()
            print(answer)
        elif not print_prime:
            print("%d is prime. " % number)


number = int(input("Please choose a number: "))
divisors(number)

#number = int(input("Please choose a number: "))
#divisors(number, False)

#number = int(input("Please choose a number: "))
#divisors(number, True, False)

#number = int(input("Please choose a number: "))
#divisors(number, False, False)

