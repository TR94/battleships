from random import randint
import random

def validate_size(data):
    """
    Validates the board size data input
    """
    try:
        int(data)
        if int(data) > 9:
            raise ValueError(f"Board size cannot be larger than 9, you wrote {data}") 

    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n") 
        return False
    
    return True

def validate_ships(size, num_ships):
    """
    Validates the number of ships data input
    """
    try:
        int(num_ships)
        if int(num_ships) > (int(size)-3)*4:
            raise ValueError(f"Too many ships, you wrote {num_ships} please choose a smaller number")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n") 
        return False

    return True

def validate_guess(guess):
    """
    Validates the player guess input
    """
    try:
        int(guess)
        if int(guess)> int(size):
            raise ValueError(f"Your guess was off the board, you wrote {size} please choose a number between 0 and {size}")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n") 
        return False

    return True

class Board:
    """
    Class to hold the details relevant to setting a game board.
    This is used for the computer and game board.
    Will hold the list of guesses made and ship positions.
    Function to print the board for each round based on the information
    held in the class.
    """
    def __init__(self, name, size, num_ships, is_computer=False):
        self.name = name
        self.size = size
        self.num_ships = num_ships
        self.is_computer = is_computer
        self.grid = []
        self.ships = []
        self.guesses = []

    def make_ship(self):
        """
        Takes the number of ships inputted from the player and generates
        random numbers to locate the ship(s)
        """
        row =  random.randint(0, (int(self.size)-1))
        col = random.randint(0, (int(self.size)-1))

        return [col, row]

    def add_ships(self):
        """
        Takes the number of ships inputted from the player and random generated ship co-ords 
        and appends them to the ships list in the Board class
        """
        for i in range (0, int(self.num_ships)):
            row, col = self.make_ship()
            self.ships.append(str(row)+", "+str(col))
            if self.is_computer == False:
                self.grid[row][col] = " @ "

    def build_board(self):
    # Builds board based on class variables
        for row in range(0, int(self.size)):
            self.grid.append([" * "]* int(self.size))

        self.add_ships()

    def render_board(self):
    # Render board to the terminal taking in ship position, misses and hits
        print(f"{self.name}'s board \n")

        for i in self.grid:
            for j in i:
                print(j, end = " ")
            print("\n")
        
        #remove this print later...
        print("SHIPS")
        for ship in self.ships:
            print(ship)
        print()

#should these two functions be in the board class?...
def player_guess():
    """
    Prompts for player guess and feeds into validation
    """

    while True:
        guess_row = input("Input row guess: ")

        if validate_guess(guess_row):
            break

    while True:
        guess_col = input("Input column guess: ")

        if validate_guess(guess_col):
            break

    return [guess_row, guess_col]

def check_shot():
    """
    Takes player guess, checks it hasn't already been guessed and 
    compares against computer ships
    Declares hit or miss
    """

    guess_row, guess_col = player_guess()
    print(guess_row)
    print(guess_col)


def computer_guess():
    """
    Generate random computer move for each round
    """

def main():
    """
    Get parameters from player and feed into validation
    """
    print("Welcome to Battleships online game")
    name = input("Please enter your name: ")

    while True:
        size = input("Please enter the desired board size: ")
        if validate_size(size):
            break

    while True:
        num_ships = input("Please enter the desired number of battleships: ")
        if validate_ships(size, num_ships):
            break

    player = Board(name, size, num_ships)
    player.build_board()
    player.render_board()

    computer = Board("Computer", size, num_ships, is_computer=True)
    computer.build_board()
    computer.render_board()

    check_shot()





main()

# guess()