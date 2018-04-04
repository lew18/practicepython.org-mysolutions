# her solution created a second list of happy numbers and the compared the two lists
# and used a function to create each list by sending the file name to the function and returning the list
# and then can use list comprehension

def file_overlap():
    # read in the primes and save as a list of ints
    primes = []
    with open('primes.txt', 'r') as primes_file:
        next_prime = primes_file.readline()
        while next_prime:
            primes.append(int(next_prime))
            next_prime = primes_file.readline()

    # read in the happy numbers and compare each value to the prime list
    with open('happy.txt', 'r') as happy_file:
        next_happy = happy_file.readline()
        while next_happy:
            if int(next_happy.strip("\n")) in primes:
                print(next_happy.strip("\n") + " is in both lists")
            next_happy = happy_file.readline()

if __name__ == '__main__':
    file_overlap()
