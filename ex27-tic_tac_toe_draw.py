"""
https://www.practicepython.org

Exercise 27: Tic Tac Toe Draw
2 chilis

This exercise is Part 3 of 4 of the Tic Tac Toe exercise series. The other exercises are:
Part 1, Part 2, and Part 4.

In a previous exercise we explored the idea of using a list of lists as a “data structure”
to store information about a tic tac toe game. In a tic tac toe game, the “game server”
needs to know where the Xs and Os are in the board, to know whether player 1 or player 2
(or whoever is X and O won).

There has also been an exercise about drawing the actual tic tac toe gameboard using text
characters.

The next logical step is to deal with handling user input. When a player (say player 1,
who is X) wants to place an X on the screen, they can’t just click on a terminal. So we
are going to approximate this clicking simply by asking the user for a coordinate of
where they want to place their piece.

As a reminder, our tic tac toe game is really a list of lists. The game starts out with
an empty game board like this:

game = [[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]

The computer asks Player 1 (X) what their move is (in the format row,col), and say they
type 1,3. Then the game would print out

game = [[0, 0, X],
	[0, 0, 0],
	[0, 0, 0]]

And ask Player 2 for their move, printing an O in that place.

Things to note:
- For this exercise, assume that player 1 (the first player to move) will always be X and
  player 2 (the second player) will always be O.
- Notice how in the example I gave coordinates for where I want to move starting from
  (1, 1) instead of (0, 0). To people who don’t program, starting to count at 0 is a
  strange concept, so it is better for the user experience if the row counts and column
  counts start at 1. This is not required, but whichever way you choose to implement this,
  it should be explained to the player.
- Ask the user to enter coordinates in the form “row,col” - a number, then a comma, then
  a number. Then you can use your Python skills to figure out which row and column they
  want their piece to be in.
- Don’t worry about checking whether someone won the game, but if a player tries to put
  a piece in a game position where there already is another piece, do not allow the piece
  to go there.

Bonus:
- For the “standard” exercise, don’t worry about “ending” the game - no need to keep
  track of how many squares are full. In a bonus version, keep track of how many squares
  are full and automatically stop asking for moves when there are no more valid moves.

"""
# move=[int(value)-1 for value in raw_input('player %d (%s), make your move [row,col]: ' % (whos_turn,icon(whos_turn))).split(',')]
# One of Michele's sample answers had the above line for getting the players move, list comprehension again...
# also good to see another way to do input:     raw_input(string with variables)
# another sample answer showed:    gameboard = [(['.']*3) for i in range(3)]
# curiously [([" ", " ", " "] * 3)]   doesn't work


unclaimed_location = "   "
player1_game_piece = ' X '
player2_game_piece = ' 0 '

def play_tictactoe():
    game_piece = [player1_game_piece, player2_game_piece]
    game_board = [[unclaimed_location, unclaimed_location, unclaimed_location],
                  [unclaimed_location, unclaimed_location, unclaimed_location],
                  [unclaimed_location, unclaimed_location, unclaimed_location]]
    number_unclaimed_locations = 9

    while "no one won" in find_winner(game_board) and number_unclaimed_locations > 0:
        player = (number_unclaimed_locations + 1) % 2 + 1        # this is a hack to get which player based on 
                                                                 # number of turns left
        print_game_board(game_board, "")
        position = input("player " + str(player) + " enter row, column ")
        for char in position:
            if char not in ["1", "2", "3", " ", ","]:
                position = "4 4"    # hack to show bad input
                break
        if ',' in position:
            coordinates = position.split(',')
        else:
            coordinates = position.split(' ')
        if len(coordinates) == 2:
            row = int(coordinates[0].strip(',')) - 1
            column = int(coordinates[1]) - 1
            if row > 2 or row < 0 or column > 2 or column < 0:
                print("invalid location, try again")
            elif game_board[row][column] != unclaimed_location:
                print("that spot is already taken, choose another")
            else:
                game_board[row][column] = game_piece[player - 1]
                number_unclaimed_locations -= 1
        else:
            print("invalid location, try again")
    return(game_board)

def find_winner(game_board):
    for triplet in range(3):
        if game_board[triplet][0] != unclaimed_location and \
           game_board[triplet][0] == game_board[triplet][1] == game_board[triplet][2]:
            # row is a win
            return(game_board[triplet][0])
        elif game_board[0][triplet] != unclaimed_location and \
             game_board[0][triplet] == game_board[1][triplet] == game_board[2][triplet]:
            # column is a win
            return(game_board[0][triplet])

    if game_board[1][1] != unclaimed_location and \
       (game_board[0][0] == game_board[1][1] == game_board[2][2] or \
        game_board[2][0] == game_board[1][1] == game_board[0][2]):
        # diagonal is a win
        return(game_board[1][1])
            
    return("no one won")

def print_game_board(game_board, message):
    print(message)
    print('-------------')     # print the top border
    for row in range(3):
        for column in range(3):
            print('|' + game_board[row][column], end = "")
        print("|")
        print('-------------')     # print the top border
    
if __name__ == '__main__':

    game_board = (play_tictactoe())
    winner = find_winner(game_board)
    
    if winner == player1_game_piece:
        message_string = "winner is player 1"
    elif winner == player2_game_piece:
        message_string = "winner is player 2"
    else:
        message_string = 'no one won'

    print_game_board(game_board, message_string)
