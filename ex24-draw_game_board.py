"""
https://www.practicepython.org

Exercise 24: Draw a Game Board
2 chilis

This exercise is Part 1 of 4 of the Tic Tac Toe exercise series.
The other exercises are: Part 2, Part 3, and Part 4.

Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- --- 
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- ---  
|   |   |   | 
 --- --- --- 
This one is 3x3 (like in tic tac toe). Obviously, they come in many
other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for
them to the screen using Python’s print statement.

Remember that in Python 3, printing to the screen is accomplished by

  print("Thing to show on screen")
Hint: this requires some use of functions, as were discussed previously
on this blog and elsewhere on the Internet, like this TutorialsPoint link.

"""

# I had for loops, Nichele's example taught the "* size" inside the print statement

def print_boarder(size):
    print(' ---' * size)
    
def print_row(size):
    print('|   ' * size + '|')
    
def draw_simple_board(size):
    print("size is " + str(size))
    print_boarder(size)     # print the top border
    for rows in range(size):
        print_row(size)
        print_boarder(size)    

if __name__ == '__main__':

    size = int(input("what size game board do you want? "))
    draw_simple_board(size)


print("\nmy second, with help from Michele's solution and user's solution")

a = '---'.join(' ' * (size + 1))
b = '   '.join('|' * (size + 1))
print('\n'.join(((a, b) * size)) + '\n' + a)
#    1         234    4       32           1


print("\nuser's solution from solutions page")

# below is a 'user' solution, which I played with
# to make the above solution
# this is hard coded to 3x3
a = '---'.join('    ')
b = '   '.join('||||')
print('\n'.join((a, b, a, b, a, b, a)))


