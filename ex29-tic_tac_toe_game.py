"""
https://www.practicepython.org

Exercise 29: Tic Tac Toe Game
3 chilis

This exercise is Part of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 1, Part 2, and Part 3.

In 3 previous exercises, we built up a few components needed to
build a Tic Tac Toe game in Python:

Draw the Tic Tac Toe game board
Checking whether a game board has a winner
Handle a player move from user input
The next step is to put all these three components together to make a
two-player Tic Tac Toe game! Your challenge in this exercise is to use
the functions from those previous exercises all together in the same
program to make a two-player game that you can play with a friend. There
are a lot of choices you will have to make when completing this exercise,
so you can go as far or as little as you want with it.

Here are a few things to keep in mind:
- You should keep track of who won - if there is a winner, show a
  congratulatory message on the screen.
- If there are no more moves left, don’t ask for the next player’s move!

As a bonus, you can ask the players if they want to play again and
keep a running tally of who won more - Player 1 or Player 2.

"""

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
        position = input("player " + str(player) + " enter row  column ")
        for char in position:
            if char not in ["1", "2", "3", " ", ","]:
                position = "2 2 2"    # hack to show bad input
                break
        if ',' in position:
            coordinates = position.split(',')
        else:
            coordinates = position.split(' ')
        if len(coordinates) == 2:
            row = int(coordinates[0].strip(',')) - 1
            column = int(coordinates[1]) - 1
            if game_board[row][column] != unclaimed_location:
                print("that spot is already taken, choose another")
            else:
                game_board[row][column] = game_piece[player - 1]
                number_unclaimed_locations -= 1
        else:
            print("invalid location, try again")
    return(game_board)

def find_winner(game_board):
    for triplet in range(len(game_board)):
        if game_board[triplet][0] != unclaimed_location and \
           game_board[triplet][0] == game_board[triplet][1] == game_board[triplet][2]:
            # check if row is a win
            return(game_board[triplet][0])
        elif game_board[0][triplet] != unclaimed_location and \
             game_board[0][triplet] == game_board[1][triplet] == game_board[2][triplet]:
            # check if column is a win
            return(game_board[0][triplet])

    # check if diagonal is a win
    if game_board[1][1] != unclaimed_location and \
       (game_board[0][0] == game_board[1][1] == game_board[2][2] or \
        game_board[2][0] == game_board[1][1] == game_board[0][2]):
        return(game_board[1][1])
            
    return("no one won")

def print_game_board(game_board, message):
    print(message)
    print_border(len(game_board))     # print the top border
    for row in range(len(game_board[0])):
        for column in range(len(game_board)):
            print("|" + game_board[row][column], end = "")
        print("|")
        print_border(len(game_board))     # print the top border

def print_border(size):
    # I had for loops, Michele's example taught the* size inside the print statement
    print(' ---' * size)
    
if __name__ == '__main__':

    wins = [0, 0]
    continue_playing= True
    while continue_playing:
        game_board = (play_tictactoe())
        winner = find_winner(game_board)
        if winner == player1_game_piece:
            message_string = "winner is player 1"
            wins[0] += 1
        elif winner == player2_game_piece:
            message_string = "winner is player 2"
            wins[1] += 1
        else:
            message_string = "Tie game"

        print_game_board(game_board, message_string)
        if input("continue playing (y/n) ") not in ['y', 'Y', 'yes', 'Yes', 'YES']:
            continue_playing = False

    print("Player 1 won " + str(wins[0]) + " game(s), Player 2 won " + str(wins[1]) + " game(s)")
