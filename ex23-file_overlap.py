"""
https://www.practicepython.org

Exercise 23: File Overlap
2 chilis

Given two .txt files that have lists of numbers in them, find the numbers
that are overlapping. One .txt file has a list of all prime numbers under
1000, and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can’t be divided by any
other number. And yes, happy numbers are a real thing in mathematics -
you can look it up on Wikipedia. The explanation is easier with an example,
which I will describe below.)

"""


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

"""
Michele's second solution:

def filetolistofints(filename):
	list_to_return = []
	with open(filename) as f:
		line = f.readline()
		while line:
			list_to_return.append(int(line))
			line = f.readline()
	return list_to_return

primeslist = filetolistofints('primenumbers.txt')
happieslist = filetolistofints('happynumbers.txt')

overlaplist = [elem for elem in primeslist if elem in happieslist]
print(overlaplist)
"""
