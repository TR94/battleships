from random import randint
import random

def validate_size(data):
    # Validates the board size data input
    try:
        int(data)
        if int(data) > 9:
            raise ValueError(f"Board size cannot be larger than 9, you wrote {data}")
        if int(data) < 4:
            raise ValueError(f"Board size cannot be smaller than 4, you wrote {data}")

    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n") 
        return False
    
    return True

def validate_ships(size, num_ships):
    # Validates the number of ships data input
    try:
        if int(num_ships) > (int(size)-3)*4:
            raise ValueError(f"Too many ships, you wrote {num_ships}. Please choose a smaller number")
        if int(num_ships) < 1:
            raise ValueError(f"Too few ships, you wrote {num_ships}. Please choose at least 1 ship")
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n") 
        return False

    return True

def validate_guess(guess, size):
    # Validates the player guess input
    try:
        int(guess)
        if int(guess)> (int(size)-1):
            raise ValueError(f"Your guess was off the board, you wrote {guess} please choose a number between 0 and ({size}-1)")
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
        self.score = 0

    def make_ship(self):
        """
        Takes the number of ships inputted from the player and generates
        random numbers to locate the ship(s)
        """
        row =  random.randint(0, (int(self.size)-1))
        col = random.randint(0, (int(self.size)-1))
        
        return [row, col]

    def add_ships(self):
        """
        Takes the number of ships inputted from the player and random generated ship co-ords 
        and appends them to the ships list in the Board class
        """
        for i in range (0, int(self.num_ships)):
            row, col = self.make_ship()
            ship_made = (str(row)+", "+str(col))

            #how to limit this to num_ships only?? if it has to re-run mid method it'll create too many
            for ship in self.ships:
                if ship != ship_made:
                    self.ships.append(ship_made)
                else:
                    self.add_ships()

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

    def player_guess(self):
        """
        Prompts for player guess and feeds into validation
        """
        #check this as doesn't prompt a new guess at the moment
        #check computer one as well 
        print("Row = left to right.") 
        print("Column = top to bottom.") 
        print("Top left corner is 0, 0\n")

        while True:
            guess_row = input("Input row guess: ")

            if validate_guess(guess_row, self.size):
                break

        while True:
            guess_col = input("Input column guess: ")
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
        guessed = 0
        hit = 0

        guess_row, guess_col = self.player_guess()
        player_guess = guess_row + ", " + guess_col

        #checks the guess hasn't been made already
        for guess in self.guesses:
            if player_guess == guess:
                guessed = 1
        
        if guessed == 1:
            print(f"{player_guess} has already been guessed, try again \n")
            self.check_player_shot()
        else:
            self.guesses.append(player_guess)
        
        #checks if the guess is a hit or not and updates board
        for ship in computer.ships:
            if ship == player_guess:
                hit = 1

        print("Player result: ")

        if hit == 1:
            print("*** HIT ***\n")
            computer.grid[int(guess_row)][int(guess_col)] = " X "
            self.score +=1

        else:
            print("*** MISS ***\n")
            computer.grid[int(guess_row)][int(guess_col)] = " O "


    def computer_guess(self):
        # Generate random computer move for each round
        row =  random.randint(0, (int(self.size)-1))
        col = random.randint(0, (int(self.size)-1))

        return [col, row]


    def check_computer_shot(self):
            """
            Takes computer guess, checks it hasn't already been guessed and 
            compares against player ships
            Declares hit or miss
            """
            guessed = 0
            hit = 0

            guess_row, guess_col = self.computer_guess()
            computer_guess = str(guess_row) + ", " + str(guess_col)

            #checks the guess hasn't been made already
            for guess in self.guesses:
                if computer_guess == guess:
                    guessed = 1
            
            if guessed == 1:
                self.check_computer_shot()
        
            else:
                self.guesses.append(computer_guess)
            
            #checks if the guess is a hit or not and updates board
            print("Computer result: ")
            
            for ship in player.ships:
                if ship == computer_guess:
                    hit = 1

            if hit == 1:
                print("*** HIT ***\n")
                player.grid[int(guess_row)][int(guess_col)] = " X "
                self.score +=1

            else:
                print("*** MISS ***\n")
                player.grid[int(guess_row)][int(guess_col)] = " O "

def main():
    # Get parameters from player and feed into validation
    print("Welcome to Battleships online game")
    name = input("Please enter your name: ")
    print()

    while True:
        print("Board size available from 4-9")
        size = input("Please enter the desired board size: ")
        if validate_size(size):
            break

    while True:
        print()
        num_ships = input("Please enter the desired number of battleships: ")
        print()
        if validate_ships(size, num_ships):
            break

    global player
    player = Board(name, size, num_ships)
    player.build_board()
    player.render_board()

    global computer 
    computer = Board("Computer", size, num_ships, is_computer=True)
    computer.build_board()
    computer.render_board()
    
    player.check_player_shot()
    computer.check_computer_shot()
    print("Scores after this round:")
    print(f"Player sunk {player.score} out of {player.num_ships} battleships\n")
    print(f"Computer sunk {computer.score} of {computer.num_ships} battleships\n")

    while computer.score or player.score < int(player.num_ships):

        play = input("Press any key to continue or 'q' to quit\n")
        if play == "q":
            print("Game ended")
            quit()
            
        else:
            print ("-"*20)
            print()
            player.render_board()
            computer.render_board()

            player.check_player_shot()
            computer.check_computer_shot()
            print(f"Player sunk {player.score} out of {player.num_ships} battleships\n")
            print(f"Computer sunk {computer.score} of {computer.num_ships} battleships\n")
    else:
        if computer.score == int(player.num_ships):
            print("***  Computer wins!!!  ***\n")
        else:
            print(f"***  {player.name} wins!!  ***\n")
        
main()

