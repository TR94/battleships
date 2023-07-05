from random import randint

print ("Welcome to Battleships online game")

# funcion needed to validate inputs

name = "Ty"
size = 3
num_ships = 3

class Board:
    """
    Class to hold the details relevant to setting a game board.
    This is used for the computer and game board.
    Will hold the list of guesses made and ship positions.
    Function to print the board for each round based on the information
    held in the class.
    """
    def __init__(self, name, size, num_ships):
        self.name = name
        self.size = size
        self.num_ships = num_ships

    # setting up blank board based on size input from player
    def build_board(self):
        blank_board = []
        for i in range(self.size):
            blank_board.append([])
            for x in range(1, (self.size+1)):
                blank_board[i].append(" * ")
        return blank_board

    # Print computer board
    def build_computer_board():
        computer_board = build_board()
        for i in blank_board:
            for j in i:
                print(j, end = " ")
            print() 


def main ():
    player = Board(name, size, num_ships)
    print(player.player_board())
    computer = Board("Computer", size, num_ships)
    print(computer.computer_board())

# main()

# setting up blank board 
"""
blank_board = []
for i in range(size):
    blank_board.append([])
    for x in range(1, (size+1)):
        blank_board[i].append(" * ")
return(blank_board)
"""

"""
print("Computer board")
print()
Board.computer_board()
print()
"""

def random_int(size):
    return randint(0, size-1)

# action to print board from class 
player = Board(name, size, num_ships)
player.build_board()
computer = Board("Computer", size, num_ships)
computer.build_computer_board