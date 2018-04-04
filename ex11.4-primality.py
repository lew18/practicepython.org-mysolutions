def divisors(number, find_divisors=True, check_for_prime=True):

    if not find_divisors and not check_for_prime:
        print("Nothing to do, returning.")
        return
    elif number < 0 or int(number) != number:
        print("must enter a positive integer")
        return
    elif number == 0:
        print("0 is not prime and has only 1 as its divisor")
        return

    # first, get the divisors that are less than the square root of number
    # second, the only divisors that are > the square root have exactly one corresponding divisor
    # that is in the list of divisors that are < the square root.
    divisors = [i for i in range(1, int(number**0.5) + 1) if number % i == 0]
    divisors = divisors + [int(number / i) for i in divisors[::-1]]

    # remove duplicate, this only happens if the number is the square of another number
    # also, the duplicate is always in the center of the list
    if divisors[int(len(divisors) / 2 - 1)] == divisors[int(len(divisors) / 2)]:
        divisors.pop(int(len(divisors) / 2))

    # print the results
    if check_for_prime:
        if len(divisors) <=2 :
            print("%d is prime. " % number)
        else:
            print("%d is not prime. " % number)

    if find_divisors:
        print("%d has %d divisors: " % (number, len(divisors)), end = " ")
        print(' '.join([str(elem) for elem in divisors]))


number = float(input("Please choose a positive integer: "))
divisors(number)

