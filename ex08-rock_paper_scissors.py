"""
https://www.practicepython.org

Exercise 8: Rock Paper Scissors
3 chilis

Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to the winner,
and ask if the players want to start a new game)

Remember the rules:

- Rock beats scissors
- Scissors beats paper
- Paper beats rock
"""

go_on = True
while go_on:
    p1=""
    while p1 not in [ "rock", "paper", "scissors" ]:
        p1 = input(" Player 1, enter your choice: rock, paper, or scissors: ")
        
    p2=""
    while p2 not in [ "rock", "paper", "scissors" ]:
        p2 = input(" Player 2, enter your choice: rock, paper, or scissors: ")

    if p1 == p2:
        print("players tied")
    elif (p1=="rock" and p2=="scissors") or   \
         (p1=="scissors" and p2=="paper") or  \
         (p1=="paper" and p2=="rock"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    if input(" Play again? (y/n) ") not in ["Y", "y"]:
        go_on = False

