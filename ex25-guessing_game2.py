# Michele used a while loop
# this one cried out to me to use recursion
# she also used --->    if "no" in ANSWER.lower() and "lower" in ANSWER.lower():
# which makes better input than my original, and good to have as history, so I've added it to mine.

def guess(lower_bound, upper_bound):
    next_guess = int((lower_bound + upper_bound) / 2)
    answer = input("is the number %d? (y, h for higher, l for lower_bound " % next_guess)
    if "yes" in answer.lower():
        print("the number is " + str(next_guess))
        return(1)
    elif "no" in answer.lower() and "higher" in answer.lower():
        if next_guess + 1 == upper_bound:
            print("the number is " + str(upper_bound))
            return(1)
        return(1 + guess(next_guess, upper_bound))
    else:
        return(1 + guess(lower_bound, next_guess))

if __name__ == '__main__':
    lower_bound = int(input("what is the lower bound? "))
    upper_bound = int(input("what is the upper bound? "))
    guesses = guess(lower_bound, upper_bound)
    print("took %d guesses." % guesses)

