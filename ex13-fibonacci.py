"""
https://www.practicepython.org

Exercise 13: Fibonacci
2 chilis

Write a program that asks the user how many Fibonnaci numbers to generate
and then generates them. Take this opportunity to think about how you can
use functions. Make sure to ask the user to enter the number of numbers in
the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of
numbers where the next number in the sequence is the sum of the previous
two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

"""

def fibn():

    count = int(input("How many Fibonacci numbers do you want? (Enter a number > 1): "))
    if count <= 1:
        fibn_list = "Fiboacci sequence always has at least 2 digits."
    else:
        fibn_list = [1, 1]
        for i in range(2, count):
            fibn_list.append(fibn_list[-2] + fibn_list[-1])
    return fibn_list


ans = fibn()
print(ans)
