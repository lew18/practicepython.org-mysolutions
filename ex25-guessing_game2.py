"""
https://www.practicepython.org

Exercise 25: Guessing Game Two
3 chilis

In a previous exercise, we’ve written a program that “knows” a number and
asks a user to guess it.

This time, we’re going to do exactly the opposite. You, the user, will
have in your head a number between 0 and 100. The program will guess a
number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses
it took to get your number.

As the writer of this program, you will have to choose how your program will
strategically guess. A naive strategy can be to simply start the guessing at 1,
and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an
optimal guessing strategy. An alternate strategy might be to guess 50 (right
in the middle of the range), and then increase / decrease by 1 as needed. After
you’ve written the program, try to find the optimal strategy! (We’ll talk about
what is the optimal one next week with the solution.)

"""

# just felt the need to do this recursively the first time.
def guess(lower_bound, upper_bound):
    computer_guess = int((lower_bound + upper_bound) / 2)
    answer = input("is the number %d? (yes, higher, lower) " % computer_guess)
    if answer == 'yes':
        print("the number is " + str(computer_guess))
        return(1)
    elif answer == 'higher':
        if computer_guess + 2 == upper_bound:
            print("the number is " + str(computer_guess + 1))
            return(1)
        elif computer_guess + 1 == upper_bound:
            print("You cheated, I've already guessed " + str(upper_bound))
            return(1)
        return(1 + guess(computer_guess, upper_bound))
    elif answer == 'lower':
        if lower_bound + 2 == computer_guess:
            print("the number is " + str(computer_guess - 1))
            return(1)
        elif lower_bound + 1 == computer_guess:
            print("You cheated, I've already guessed " + str(lower_bound))
            return(1)
        return(1 + guess(lower_bound, computer_guess))
    else:
        print("only 'yes', 'higher' and 'lower' recognized")
        return(guess(lower_bound, upper_bound))

# this time with a while loop
def guess2(lower_bound, upper_bound):
    answer = 'bad input'
    guesses = 0
    while answer != 'yes':
        print(lower_bound, upper_bound)
        computer_guess = int((lower_bound + upper_bound) / 2)
        answer = input("is the number %d? (yes, higher, lower) " % computer_guess)
        guesses += 1
        if answer == 'yes':
            print("the number is " + str(computer_guess))
        elif answer == 'higher':
            if computer_guess + 2 == upper_bound:
                print("the number is " + str(computer_guess + 1))
                answer = 'yes'
            elif computer_guess + 1 == upper_bound:
                print("You cheated, I've already guessed " + str(upper_bound))
                answer = 'yes'
            else:
                lower_bound = computer_guess
        elif answer == 'lower':
            if lower_bound + 2 == computer_guess:
                print("the number is " + str(computer_guess - 1))
                answer = 'yes'
            elif lower_bound + 1 == computer_guess:
                print("You cheated, I've already guessed " + str(lower_bound))
                answer = 'yes'
            else:
                upper_bound = computer_guess
        else:
            print("only 'yes', 'higher' and 'lower' are valid input")
            guesses -= 1
    return(guesses)

if __name__ == '__main__':
    lower_bound = int(input("what is the lower exclusive bound? "))
    upper_bound = int(input("what is the upper exclusive bound? "))
    guesses = guess(lower_bound, upper_bound)
    print("took %d guesses." % guesses)

