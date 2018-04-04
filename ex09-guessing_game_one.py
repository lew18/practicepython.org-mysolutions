import random

guesses = 0
done = "no"
while done != "exit":
    target = random.randint(1, 9)
    guess = 0
    while guess != target:
        guess = int(input("enter your guess between 1 and 9, inclusive: "))
        guesses += 1
        if guess < target:
            print("too low! ")
        elif guess > target:
            print("too high! ")
        else:
            print("You got it")

    done = input("type 'exit' to quit ")

print("You made %d guesses" % guesses)

