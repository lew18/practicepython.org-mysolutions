# one of Michele's sample solutions used sys.argv:
# len(sys.argv)
# a = sys.argv[1]
# b = sys.argv[2]
# c = sys.argv[3]

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
        x = random.randint(0, 10000)        
        y = random.randint(0, 10000)        
        z = random.randint(0, 10000)        
        print("max of %d, %d, %d is %d" % (x, y, z, max(x, y, z)))
