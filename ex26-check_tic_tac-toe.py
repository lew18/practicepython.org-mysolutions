"""
https://www.practicepython.org

Exercise 26: Tic Tac Toe
2 chilis

This exercise is Part 2 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 1, Part 3, and Part 4.

As you may have guessed, we are trying to build up to a full tic-tac-toe
board. However, this is significantly more than half an hour of coding, so
we’re doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of
Tic Tac Toe, not worrying about how the moves were made.

If a game of Tic Tac Toe is represented as a list of lists, like so:

game = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]
where a 0 means an empty square, a 1 means that player 1 put their token
in that space, and a 2 means that player 2 put their token in that space.

Your task this week: given a 3 by 3 list of lists that represents a
Tic Tac Toe game board, tell me whether anyone has won, and tell me which
player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a
column, or a diagonal. Don’t worry about the case where TWO people have
won - assume that in every board there will only be one winner.

"""

# solutions on solutions page used sets for rows and columns, so if len = 1, had a winner
# those solutions also used numpy to transpose columns to rows
import random

def generate_board():
    return([[ random.randint(0, 2), random.randint(0, 2), random.randint(0, 2) ],
            [ random.randint(0, 2), random.randint(0, 2), random.randint(0, 2) ],
            [ random.randint(0, 2), random.randint(0, 2), random.randint(0, 2) ]])

def find_winner(game_board):
    for triplet in range(len(game_board)):
        if game_board[triplet][0] != 0 and \
           game_board[triplet][0] == game_board[triplet][1] == game_board[triplet][2]:
            # row is a win
            return(str(game_board[triplet][0]))
        elif game_board[0][triplet] != 0 and \
             game_board[0][triplet] == game_board[1][triplet] == game_board[2][triplet]:
            # column is a win
            return(str(game_board[0][triplet]))

    if game_board[1][1] != 0 and \
       (game_board[0][0] == game_board[1][1] == game_board[2][2] or \
        game_board[2][0] == game_board[1][1] == game_board[0][2]):
        # diagonal is a win
        return(str(game_board[1][1]))
            
    return("no one won")


def print_game_board(game_board, message):
    print(message)
    for rows in range(len(game_board)):
        print(game_board[rows])

if __name__ == '__main__':

#    size = int(float(input("what size game board do you want? ")))
#    draw_simple_board(size)

    check = int(input("how many games to check? "))
    for i in range(check):
        game_board = (generate_board())
        winner = find_winner(game_board)
        if "no" in winner:
            message_string = "Nobody won"
        else:
            message_string = "winner is player " + winner
        print_game_board(game_board, message_string)
