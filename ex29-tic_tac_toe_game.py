"""
move=[int(value)-1 for value in raw_input('player %d (%s), make your move [row,col]: ' % (whos_turn,icon(whos_turn))).split(',')]
One of Michele's sample answers had the above line for getting the players move, list comprehension again...
also good to see another way to do input:     raw_input(string with variables)
another sample answer showed:    gameboard = [(['.']*3) for i in range(3)]
curiously [([" ", " ", " "] * 3)]   doesn't work

reminder that three quotes start and end a block of comments
"""

unclaimed_location = " "

def play_tictactoe():
    game_piece = ["X", "O"]
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
            print("| " + game_board[row][column], end = " ")
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
        if "no" in winner:
            message_string = "Tie game"
        elif winner == 'X':
            message_string = "winner is player 1"
            wins[0] += 1
        else:
            message_string = "winner is player 2"
            wins[1] += 1
        print_game_board(game_board, message_string)
        if input("continue playing (y/n) ") not in ['y', 'Y', 'yes', 'Yes', 'YES']:
            continue_playing = False

    print("Player 1 won " + str(wins[0]) + " game(s), Player 2 won " + str(wins[1]) + " game(s)")
