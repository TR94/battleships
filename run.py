print ("Welcome to Battleships online game")
name = input("Please input player name: ")
size = input("Please input the desired size of the game board: ")
num_ships = input("Please input the number of ships for the game: ")

player = Board(name, size, num_ships, "player")

class Board:
    """
    Class to hold the details relevant to setting a game board.
    This is used for the computer and game board.
    Will hold the list of guesses made and ship positions.
    Function to print the board for each round based on the information
    held in the class.
    """
    def __init__(self, name, size, num_ships, type):
        self.name = name
        self.size = size
        self.num_ships = num_ships
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(type):
        print()

    def player_board(player):
        return (f"Your name: {self.name}, board size: {self.size}, number of battleships: {self.num_ships}")



print(player_board)