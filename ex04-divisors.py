"""
https://www.practicepython.org

Exercise 4: Divisors
2 chilis

Create a program that asks the user for a number and then prints out a list
of all the divisors of that number. (If you don’t know what a divisor is,
it is a number that divides evenly into another number. For example, 13 is
a divisor of 26 because 26 / 13 has no remainder.)

"""

# this does not return negative divisors
def find_divisors(number):
    divisors = [ 1, number ]         # 1 and number itself are always divisors

    # find any other divisors
    for i in list(range(2, int(number**0.5) + 1)):
        if number % i == 0:
            divisors.append(i)
            divisors.append(int(number / i))

    # remove duplicate, only happens if number is a square
    if divisors[-2] == divisors[-1]:
        divisors.pop()

    return(divisors)


# ignore error checking the input
number = int(input("Please choose an integer greater than 0: "))
print(find_divisors(number))

