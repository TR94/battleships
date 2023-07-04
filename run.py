print ("Welcome to Battleships online game")


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

    def player_board(self):
        return f"Your name: {self.name}, board size: {self.size}, number of battleships: {self.num_ships}"

player = Board("Ty", 5, 3)
print(player.player_board())

