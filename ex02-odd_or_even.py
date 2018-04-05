"""
https://www.practicepython.org

Exercise 2: Odd or Even
1 chile
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and
   one number to divide by (check). If check divides evenly into num,
   tell that to the user. If not, print a different appropriate message.

"""

number = int(input("Enter an integer: "))

if (number % 4) == 0:
    print(str(number) + " is evenly divisible by 4.")
elif ((number %2) == 0):
    print(str(number) + " is even.")
else:
    print(str(number) + " is odd.")

divisor = int(input("Enter a second integer: "))
if number % divisor:
    print("%d is not a divisor of %d." % (divisor, number))
else:
    print("%d is a divisor of %d." % (divisor, number))
