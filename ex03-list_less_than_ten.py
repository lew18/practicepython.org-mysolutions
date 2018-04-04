
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# initial part
for i in range(5):
    print(str(a[i]), end=" ")
print()

for i in a[0:7]:
    print(str(i), end = " ")
print()

# extra #1
b = a[0:5]
print(b)

# extra #2
print(a[0:5])

# extra #2b
print(' '.join([str(i) for i in a[0:5]]))

# extra #3
max = int(input("please enter limit: "))

i = 0
while i < len(a) and a[i] < max:
    i+=1
print(' '.join([str(j) for j in a[0:i]]))
