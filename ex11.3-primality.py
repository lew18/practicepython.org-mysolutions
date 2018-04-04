def divisors(number, print_divisors=True, print_prime=True):

    if not print_divisors and not print_prime:
        print("Nothing to do, returning.")
        return
    elif number == 0:
        print("0 is not prime and has only 1 as its divisor")
        return

    # initialize
    answer = [ ]
    if (int(number**0.5))**2 == number:
        candidates = list(range(1, int(number**0.5)))
    else:
        candidates = list(range(1, int(number**0.5) + 1))

    # find the answer
    answer = [i for i in candidates if number % i == 0]
    answer = answer + sorted([int(number / i) for i in answer])

    if (int(number**0.5))**2 == number:
        answer.insert(int(len(answer)/2), int(number**0.5))

    # print the results
    if print_prime:
        if len(answer) <=2 :
            print("%d is prime. " % number)
        else:
            print("%d is not prime. " % number)

    if print_divisors:
        if len(answer) > 2 :
            print("%d has %d divisors: " % (number, len(answer)), end = ' ')
            print(answer)
        elif not print_prime:
            print("%d is prime. " % number)


start = int(input("Please choose a number: "))
end = int(input("Please choose a number: "))

for number in range(start, end + 1):
    divisors(number, True, False)
