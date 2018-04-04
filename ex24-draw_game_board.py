# I had for loops, her example taught the* size inside the print statement

def print_boarder(size):
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

    size = int(float(input("what size game board do you want? ")))
    draw_simple_board(size)
