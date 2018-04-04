def fibn():

    count = int(input("How many Fibonacci numbers do you want? "))

    b1 = b2 = 1
    print("Fibonacci sequence to %d entries is %d, %d" % (count, b2, b1), end="")

    for i in range(2, count):
        new = b1 + b2
        b2 = b1
        b1 = new
        print(", %d" % b1, end="")

    print()

fibn()
