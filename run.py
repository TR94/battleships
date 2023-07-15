from random import randint
import random


def validate_size(data):
    # Validates the board size data input
    try:
        int(data)
        if int(data) > 9:
            raise ValueError(f"Maximum board size 9, you wrote {data}")
        if int(data) < 4:
            raise ValueError(f"Minimum board size 4, you wrote {data}")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False

    return True


def validate_ships(size, num_ships):
    # Validates the number of ships data input
    try:
        if int(num_ships) > (int(size)-3)*4:
            raise ValueError(f"Too many ships, you wrote {num_ships}")
            print("Please choose a smaller number")
        if int(num_ships) < 1:
            raise ValueError(f"Too few ships, you wrote {num_ships}")
            print("Please choose at least 1 ship")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False

    return True


def validate_guess(guess, size):
    # Validates the player guess input
    guess_limit = (int(size) - 1)

    try:
        int(guess)
        if int(guess) > (int(size)-1):
            raise ValueError(f"Your guess of '{guess}' was off the board")
            print(f"Please choose a number between 0 and ({guess_limit})")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False

    return True


class Board:
    """
    Class to hold the details relevant to setting a game board.
    Will hold the lists of grid, ship positions, guesses made and score.
    Methods to process inputs and store data relevant to this class.
    """
    def __init__(self, name, size, num_ships, is_computer=False):
        self.name = name
        self.size = size
        self.num_ships = num_ships
        self.is_computer = is_computer
        self.grid = []
        self.ships = []
        self.guesses = []
        self.score = 0

    def make_ship(self):
        """
        Takes the number of ships inputted from the player and generates
        random numbers to locate the ship(s)
        """
        row = random.randint(0, (int(self.size)-1))
        col = random.randint(0, (int(self.size)-1))

        return [row, col]

    def generate_ships(self):
        """
        Takes the number of ships inputted from the player and random generated
        ship co-ords and appends them to the ships list in the Board class
        """
        while len(self.ships) < (int(self.num_ships)):
            row, col = self.make_ship()
            ship_made = (str(row)+", "+str(col))

            if self.does_ship_exist(ship_made) is False:
                self.ships.append(ship_made)

            if self.is_computer is False:
                self.grid[row][col] = " @ "

    def does_ship_exist(self, ship_made):
        # Checks if the ship made already exists in ship list
        if ship_made in self.ships:
            return True
        else:
            return False

    def build_board(self):
        # Builds board based on class variables
        for row in range(0, int(self.size)):
            self.grid.append([" * "] * int(self.size))

        self.generate_ships()

    def render_board(self):
        # Render board to the terminal taking in ship position, misses and hits
        print(f"{self.name}'s board \n")

        for i in self.grid:
            for j in i:
                print(j, end=" ")
            print("\n")

    def player_guess(self):
        """
        Prompts for player guess and feeds into validation
        """
        guess_limit = int(self.size) - 1
        print(f"Row = left to right (0 - {guess_limit})")
        print(f"Column = top to bottom (0 - {guess_limit})")
        print("Top left corner is 0, 0\n")

        while True:
            guess_row = input("Input row guess: \n")

            if validate_guess(guess_row, self.size):
                break

        while True:
            guess_col = input("Input column guess: \n")
            print()

            if validate_guess(guess_col, self.size):
                break

        return [guess_row, guess_col]

    def check_player_shot(self):
        """
        Takes player guess, checks it hasn't already been guessed and
        compares against computer ships
        Declares hit or miss
        """
        guess_row, guess_col = self.player_guess()
        player_guess = guess_row + ", " + guess_col

        # Checks the guess hasn't been made already
        while player_guess in self.guesses:
            print(f"{player_guess} has already been guessed, try again \n")
            guess_row, guess_col = self.player_guess()
            player_guess = guess_row + ", " + guess_col

        else:
            self.guesses.append(player_guess)

        # Checks if the guess is a hit or not and updates board
        hit = 0
        print("Player result: ")

        for ship in comp.ships:
            if ship == player_guess:
                hit = 1

        if hit == 1:
            print("*** HIT ***\n")
            comp.grid[int(guess_row)][int(guess_col)] = " X "
            self.score += 1

        else:
            print("*** MISS ***\n")
            comp.grid[int(guess_row)][int(guess_col)] = " O "

    def computer_guess(self):
        # Generate random computer guess for each round
        row = random.randint(0, (int(self.size)-1))
        col = random.randint(0, (int(self.size)-1))

        return [col, row]

    def check_computer_shot(self):
        """
        Takes computer guess, checks it hasn't already been guessed and
        compares against player ships
        Declares hit or miss
        """
        guess_row, guess_col = self.computer_guess()
        computer_guess = str(guess_row) + ", " + str(guess_col)

        # Checks the guess hasn't been made already
        while computer_guess in self.guesses:
            guess_row, guess_col = self.computer_guess()
            computer_guess = str(guess_row) + ", " + str(guess_col)
        else:
            self.guesses.append(computer_guess)

        # Checks if the guess is a hit or not and updates board
        hit = 0
        print("Computer result: ")

        for ship in player.ships:
            if ship == computer_guess:
                hit = 1

        if hit == 1:
            print("*** HIT ***\n")
            player.grid[int(guess_row)][int(guess_col)] = " X "
            self.score += 1

        else:
            print("*** MISS ***\n")
            player.grid[int(guess_row)][int(guess_col)] = " O "


def main():
    # Get parameters from player and feed into validation
    print("Welcome to Battleships online game")
    name = input("Please enter your name: \n")
    print()

    while True:
        print("Board size available from 4-9")
        size = input("Please enter the desired board size: \n")
        if validate_size(size):
            break

    while True:
        print()
        num_ships = input("Please enter the desired number of battleships: \n")
        print()
        if validate_ships(size, num_ships):
            break

    # Builds class instances and runs methods to build and print board
    global player
    player = Board(name, size, num_ships)
    player.build_board()
    player.render_board()

    global comp
    comp = Board("Computer", size, num_ships, is_computer=True)
    comp.build_board()
    comp.render_board()

    # Runs first round
    player.check_player_shot()
    comp.check_computer_shot()
    print("Scores after this round:")
    print(f"Player sunk {player.score} of {player.num_ships} ships\n")
    print(f"Computer sunk {comp.score} of {comp.num_ships} ships\n")

    # Runs sequential rounds until all ships are sunk
    while comp.score < int(player.num_ships) and \
            player.score < int(player.num_ships):
        play = input("Press any key to continue or 'q' to quit\n")
        if play == "q":
            print("Game ended")
            quit()

        else:
            print("-"*20)
            print()
            player.render_board()
            comp.render_board()

            player.check_player_shot()
            comp.check_computer_shot()
            print("Scores this round: ")
            print(f"Player sunk {player.score} of {player.num_ships} ships\n")
            print(f"Computer sunk {comp.score} of {comp.num_ships} ships\n")
    else:
        if comp.score >= int(player.num_ships):
            print("***  Computer wins!!!  ***\n")
        else:
            print(f"***  {player.name} wins!!  ***\n")


main()
