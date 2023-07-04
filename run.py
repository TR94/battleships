print ("Welcome to Battleships online game")

# funcion needed to validate inputs

name = "Ty"
size = 7
num_ships = 4

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

    #def player_board(self):
        # return f"Your name: {self.name}, board size: {self.size}, number of battleships: {self.num_ships}"

    def computer_board():
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

blank_board = []
for i in range(size):
    blank_board.append([])
    for x in range(1, (size+1)):
        blank_board[i].append(" * ")

print("Computer board")
print()
Board.computer_board()
print()