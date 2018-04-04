import random

def generate_target():
    return(int(random.triangular() * 10000))

def compare(guess, target):
    if guess > 9999:
        print("guess must be 4 digits or less, try again.")
        return False

    cows = 0
    bulls = 0

    g = []
    t = []
    answer = ["n"] * 4

    g.append( int((guess % 10000) / 1000))
    g.append( int((guess %  1000) /  100))
    g.append( int((guess %   100) /   10))
    g.append( int((guess %    10) /    1))

    t.append( int((target % 10000) / 1000))
    t.append( int((target %  1000) /  100))
    t.append( int((target %   100) /   10))
    t.append( int((target %    10) /    1))

    for i in range(0, 4):
        if g[i] == t[i]:
            answer[i] = "c"
            cows += 1
    for i in range(0, 4):
        for j in range(0, 4):
            if answer[j] == "n" and g[i] == t[j]:
                answer[j] = "b"
                bulls += 1

    if cows == 4:
        return True
    else:
        print("cows: %d, bulls: %d " % (cows, bulls))
        return False

if __name__ == "__main__":
    target = generate_target()

    print("target is %d" % target)
    guess_count = 1
    guess = int(input("What's your first guess? "))
    while False == compare(guess, target):
        guess_count += 1
        guess = int(input("What's your next guess? "))

    print("Took %d guesses to guess %4d." % (guess_count, target))

