
go_on = 1
while go_on == 1:
    p1=""
    while p1 not in [ "r", "p", "s" ]:
        p1 = input(" Player 1, enter your move, r, p, s: ")
    p2=""
    while p2 not in [ "r", "p", "s" ]:
        p2 = input(" Player 2, enter your move, r, p, s: ")

    if p1 == p2:
        print("players tied")
    elif (p1=="r" and p2=="s") or (p1=="s" and p2=="p") or (p1=="p" and p2=="r"):
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")

    if input(" Play again? ") not in ["Y", "y"]:
        go_on = 0


