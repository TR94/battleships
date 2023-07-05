from random import randint

print ("Welcome to Battleships online game")

# funcion needed to validate inputs

name = "Ty"
size = 5
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
        print(f"{self.name}'s board")
        for i in range(self.size):
            blank_board.append([])
            for x in range(1, (self.size+1)):
                blank_board[i].append(" * ")
        for i in blank_board:
            for j in i:
                print(j, end = " ")
            print() 

    # Print player board
    def build_player_board():
        player = Board(name, size, num_ships)
        print(player.build_board())

    # Print computer board
    def build_computer_board():
        computer = Board("Computer", size, num_ships)
        print(computer.build_board())

def main ():
    Board.build_computer_board()
    Board.build_player_board()

main()

def random_int(size):
    return randint(0, size-1)

# action to print board from class 