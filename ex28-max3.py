"""
https://www.practicepython.org

Exercise 28: Max of 3
1 chili

Implement a function that takes as input three variables, and returns
the largest of the three. Do this without using the Python max() function!

The goal of this exercise is to think about some internals that Python
normally takes care of for us. All you need is some variables and if statements!

"""

import random

def max(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

if __name__ == "__main__":
    for i in range(10):
        x = random.randint(0, 10)        
        y = random.randint(0, 10)        
        z = random.randint(0, 10)        
        print("max of %4d, %4d, %4d is %4d" % (x, y, z, max(x, y, z)))
