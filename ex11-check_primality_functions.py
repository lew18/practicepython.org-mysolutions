"""
https://www.practicepython.org

Exercise 11: Check Primality Functions
3 chilis

Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you. Take this
opportunity to practice using functions, described below.
"""

number = int(input("Please choose a positive integer: "))

prime = True
for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        prime = False
        break
    i += 1

if prime:
    print("%d is a prime number" % number)
else:
    print("%d is not a prime number" % number)


# this is slightly modified version that someone else submitted
# in this solution, True means composite, i.e. not prime
ans = sum([ True if number % factor == 0 else False for factor in ( [2] + list(range(3,int(number**0.5 + 1),2)) ) ])
print(ans)
