"""
https://www.practicepython.org

Exercise 3: List Less Than Ten
2 chiles

Take a list, say for example this one:

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:
1. Instead of printing the elements one by one, make a new list that has
   all the elements less than 5 from this list in it and print out this new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements from
   the original list a that are smaller than that number given by the user.

"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# initial part
for i in range(len(a)):
    if a[i] < 5:
        print(str(a[i]))


# extra #1
b =[]

for i in range(len(a)):
    if a[i] < 5:
        b.append(a[i])
print(b)

# extra #2
# yes, I could do 5 again, but that's _really_ boring
# basically copied this idea from a much later exercise
print([a[i] for i in range(len(a)) if a[i] < 18])

# extra #3
max = int(input("please enter limit: "))

b = []
for i in range(len(a)):
    if a[i] < max:
        b.append(a[i])
print(b)
