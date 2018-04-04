import random

def generate_board():
    return([[ random.randint(0, 2), random.randint(0, 2), random.randint(0, 2) ],
            [ random.randint(0, 2), random.randint(0, 2), random.randint(0, 2) ],
            [ random.randint(0, 2), random.randint(0, 2), random.randint(0, 2) ]])

def find_winner(game_board):
    for triplet in range(len(game_board)):
        if game_board[triplet][0] != 0 and \
           game_board[triplet][0] == game_board[triplet][1] == game_board[triplet][2]:
            # check if row is a win
            return(str(game_board[triplet][0]))
        elif game_board[0][triplet] != 0 and \
             game_board[0][triplet] == game_board[1][triplet] == game_board[2][triplet]:
            # check if column is a win
            return(str(game_board[0][triplet]))

    # check if diagonal is a win
    if game_board[1][1] != 0 and \
       (game_board[0][0] == game_board[1][1] == game_board[2][2] or \
        game_board[2][0] == game_board[1][1] == game_board[0][2]):
        return(str(game_board[1][1]))
            
    return("no one won")


def print_game_board(game_board, message):
    print(message)
    for rows in range(len(game_board)):
        print(game_board[rows])

def print_boarder(size):
    # I had for loops, Michele's example taught the* size inside the print statement
    print(' ---' * size)
    
def print_row(size):
    print('|   ' * (size + 1))
    
def draw_simple_board(size):
    print("size is " + str(size))
    print_boarder(size)     # print the top border
    for rows in range(size):
        print_row(size)
        print_boarder(size)    

if __name__ == '__main__':

#    size = int(float(input("what size game board do you want? ")))
#    draw_simple_board(size)

    check = int(input("how many games to check? "))
    for i in range(check):
        game_board = (generate_board())
        winner = find_winner(game_board)
        if "no" in winner:
            message_string = "Tie game"
        else:
            message_string = "winner is player " + winner
        print_game_board(game_board, message_string)
