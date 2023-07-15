# Battleships - Python based game

This game mimics the classic Battleships game and allows players to interact through the terminal to play against a computer. The player can choose the board size and number of ships for the game and inputs their row/column guess on each round. The game continues until either the computer or the player sinks all of the opponents ships. 

This programme has been made to complete the third project within the Code Institute Full Stack Developer course and focuses on the use of the Python language. It is run on a Code Institute template that allows the terminal to be run in a webpage for viewing. 

Link to live project: [This is an external link to Heroku](https://battleships-123-fa5d91b20ea3.herokuapp.com/)

# User Experience
The target audience for this site are fans of the classic Battleships game. This programme will allow them to play the game against a randomised computer output with some customisable features such as board size and number of ships. 

The user goals for new and returning users are the same:
- As a user, I want to play the classic Battleships game in an online setting
- As a user, I want the game to keep score so I know who is winning 
- As a user, I want the game to be fair so I don’t feel cheated 

# Development Planes
The 5 development planes have been considered to ensure the game is developed in a structure manner. Working through each plane in turn ensures the key foundations are considered and agreed before progressing too far. Working methodically in this way should result in the initial release being much closer to the final desired output.  

## Strategy
This programme is purely for fans of the Battleships game and therefore has no commercial drivers. With this in mind the only strategic requirements for this programme are to ensure the user has an authentic Battleships experience which:
- is against a fair opponent 
- is interactive and provides feedback on the game play 
- follows the rules accurately 

## Scope
Defining the scope at this early stage allows the development work to stay focused, it agrees what is on and off the table for the initial release. 

Based on the user experience and strategy above, the content requirements are:
- Player can choose the board size for the game
- Player can choose the number of ships within the game 
- An input area for the player to interact with
- A game board that tracks the hits and misses throughout the rounds
- A score tracker 

## Structure
The structure of the Python code has been considered as a flowchart to draft out how the programme will work. At this stage it highlights how to game will flow and allows consideration for the inputs, outputs and validation required. This doesn't cover the details of classes, methods and functions but does help tp understand the logic flow required. See below for the flowchart.

![Battleships game flow chart](/assets/readMe_images/Battleships_Flowchart.png)

## Skeleton
Wire-framing at this stage allows the page(s) to be designed and altered freely without committing anything to code. For this project, the game is being played in the terminal and therefore the structural design is very limited. 
Below are the wireframes for the start of the game and each round. 

![Battleships Wireframe](/assets/readMe_images/Battleships_wireframe.png)

At the start of the game the player needs to input some information and then the first round of boards will be printed. During each round the player will make their guess, computer will randomise a guess and the results will be displayed with updated boards.

## Surface:
With the game being played in the terminal, there are very little visual design features that can be incorporated into the game. For the boards there are several indications which are needed:
- "*"  individual grid location
- "@"  ship, visual location of the ship, only used on the player board 
- "X"  hit, ship that has been hit 
- "O"  miss, grid location that didn’t hit a ship

Colour, font, image and icons are not available to style within the Python terminal. 

# Features: 
## Game start
The game starts with a welcome message and the chance for the player to input the following details:
- Player name
- Board size
- Number of ships 

These inputs are validated within the code meaning the player will be prompted for a second input if the first is not acceptable. The limits for the inputs are explained at the point of data entry. 

![Battleships game start](/assets/readMe_images/game_start.png)

Input validation:
- The player name input is free text, there is no validation.
- The board size has a limit between 4-9. A number outside of the range will give the player feedback and a chance to try again. A string rather than an integer will also trigger an error. 
- The number of ships has similar validation logic to "board size" above. 

## Game boards - start
Once the player has input the parameters for the game, the boards are printed. The randomised ships are printed on the player board showing their location however they are not printed on the computer board. The player board is customised with the player's name from the input at the start of the game. 

![Battleships board start](/assets/readMe_images/game_rd1.png)

## Player guess 
With the randomised ships logged and the boards printed the game can begin. The player has the chance to input their guess in the form of a row guess and column guess. This corresponds to the board with instructions explaining how to guess the co-ordinate they want. 

![Battleships player guess](/assets/readMe_images/game_input.png)

Input validation:
- The inputs must be an integer and within the size of the board. Anything else will return an error.
- As the game continues through subsequent rounds, all guesses are stored and if a player accidently makes the same guess twice an error message will be displayed along with another chance to make a guess.

## Round results
The results for the round are declared based on the player input, randomised computer guess and ship positions. The result is either a hit or a miss. The scores are also displayed with a hit gaining a point. The message will display how many battleships are left to hit for the player and the computer. 

![Battleships round results](/assets/readMe_images/game_results.png)

## Quit game
At the end of each round, the player has the opportunity to quit the game. Inputting 'q' will quit the game whilst any other key will continue. 

![Battleships quit game](/assets/readMe_images/game_quit.png)

## Next round
Once the player has confirmed to continue the game, the boards will be reprinted showing the hits and misses from previous rounds. The game will loop back to the player guess and the game will continue.

![Battelships next round](/assets/readMe_images/game_rd2.png)

# Technologies used:
## Coding languages used: 
The only coding laugauge used in this project was Python3.

## External resources: 
Balsamiq:
Simple wireframing software used to mock up how the user interface will look

Lucid Chart:
Simple flow chart online software used to draft out how the Python programme will need to work

Git-Hub / GitPod:
Git-hub is used to store the project files and is used to host the site. GitPod was used as the IDE to code the website.

Heroku:
Heroku is used to deploy the programme in the form of an app. This is supported by the Code Institute template that allows a python terminal to be run using a web page. 

# Accessibility: 
Accessibility isn't a consideration for backend Python programming, it would be addressed during the front end interaction development if required. 

# Testing
The testing phase allows the code to be stressed before it is released. Carrying out thorough testing before release reduces problems with the code ensuring it is robust and delivers the expected user experience. 

## User Goals
The user goals were set at the start of development during the Strategy phase. These are reviewed against the finished code to ensure it achieves the desired outcomes:
- Player can choose the board size for the game:
    - Input at the start of the game allows a board size between 4 and 9.
    - Validation within the code ensures the correct input is given.
- Player can choose the number of ships within the game:
    - Input at the start of the game allows the number of ships to be chosen.
    - Validation within the code ensures a sensible input is accepted. There isn't any specific guidance to the player on this but the validation. will return feedback on a smaller or larger number.
- An input area for the player to interact with:
    - For each round the player chooses the row and column they want to guess
    - Validation within the code ensure this guess is within the confines of the board and hasn't been guessed in a previous round.
    - The player has the option to continue or quit the game after each round. 
- A game board that tracks the hits and misses throughout the rounds:
    - After each round the boards are printed showing hits and misses.
- A score tracker:
    - After each round the results are printed to show a hit or miss for the player and the computer. 
    - The number of battleships left to sink is fedback after each round.

## Manual Testing
### Functionality testing:
#### Page loading:
- Expected: Page should load in the terminal with no errors
- Testing:
- Result:
- Fix:

#### Start game inputs:
- Expected: Inputs for "name", "board size" and "number of ships" are carried into the game
- Testing: type "python3 run.py" into the terminal 
- Result: No errors reported
- Fix: N/A

- Expected: "board size" input is validated within the given range of 4-9
    - Testing: Input 10
    - Result: Error raised stating maximum board size and input is too large. Prompted to try again. 
    - Fix: N/A

    - Testing: Input 3
    - Result: Error raised stating maximum board size and input is too large. Prompted to try again. 
    - Fix: N/A

    - Testing: Input "cat"
    - Result: Error raised stating needs to be an integer 
    - Fix: N/A

- Expected: "number of ships" input is validated within a sensible range
    - Testing: Input 0
    - Result: Error raised stating too few ships, prompted to try again.
    - Fix: N/A

    - Testing: Input 20 based on board size of 4
    - Result: Error raised stating too many ships, prompted to try again.
    - Fix: N/A

    - Testing: Input "cat"
    - Result: Error raised stating needs to be an integer
    - Fix: N/A

    - Testing: Input 4
    - Result: Game boards are printed and game progresses
    - Fix: N/A

#### First round board
- Expected: Player and computer boards are printed. Player board shows ships and computer board doesn't show ships
- Testing: After number of battleships is entered, boards are printed
- Result: Boards are printed as expected including player name, correctly sized and with the correct number of randomly positioned ships. Computer board doesn't show ships.
- Fix: N/A

- Expected: Player board shows the correct number of ships as inputted at the start of the game
- Testing: After number of battleships is entered, boards are printed
- Result: Player board has correct number of randomly positioned ships. Computer board doesn't show ships.
- Fix: N/A

#### Guess input
- Expected: Instructions are given on how to located a guess on the board
- Testing: Visual
- Result: Instructions are present and correct. Not necessarily clear what the limits are for the board size
- Fix: Add into the instructions a literal that shows the guess limits.

- Expected: Inputs for row and column are validated to be within the game board
    - Testing: Input 5
    - Result: Error stated that input is off the board and prompted to try again
    - Fix: N/A

    - Testing: Input "cat"
    - Result: Error raised stating needs to be an integer
    - Fix: N/A

- Expected: Result of the round is communicated 
- Testing: Input row 3, input col 3.
- Result: Player and computer result communicated with miss
- Fix: N/A

- Expected: Inputted guess is printed correctly onto the computer board and indicates a hit or miss correctly
- Testing: Input row 3, input col 3
- Result: Displayed corrrectly as a miss "O" on the computer board
- Fix: N/A

- Expected: Inputted guess is printed correctly onto the computer board and indicates a hit or miss correctly
- Testing: Input row 2, input col 3
- Result: Displayed corrrectly as a hit "X" on the computer board
- Fix: N/A

#### Game continue or quit
- Expected: Instructions are provided on how to continue or quit the game
- Testing: Visual
- Result: Instructions are clear
- Fix: N/A

- Expected: Submitting "q" ends the game
- Testing: Input "q"
- Result: Game quits are expected 
- Fix: N/A

- Expected: Submitting any key (other than "q" continues the game)
    - Testing: Input "r" 
    - Result: Game continues to next round
    - Fix: N/A

    - Testing: Press enter key (i.e. blank input) 
    - Result: Game continues to next round
    - Fix: N/A

#### Next round 
- Expected: Boards are updated correctly and print for next round
- Testing: As above
- Result: Boards are printed correctly with the hit/miss from previous round
- Fix: N/A

- Expected: A repeated guess from a previous round is rejected and asks to try again 
- Testing: Input 3, 3 - has already been input once 
- Result: Error raised stating this has already been guessed. Prompted to guess agian
- Fix: N/A

- Expected: Score is updated when a hit occurs with feedback to the player
- Testing: Played until a hit occured
- Result: Score updated with "Computer sunk 1 out of 4 ships"
- Fix: N/A

#### Winner
- Expected: The game ends when either the player's or computer's ships are sunk and declares a winner
- Testing: Played game until all ships were sunk 
- Result: Game didn't end
- Fix: While loop in main() function was incorrect. The "or" was changed to "and" to correct the logic. Game now end correctly with a winner.

### Responsiveness 
Responsiveness within the webpage isn't a consideration for this backend programme. 

### Code Validation
The code has been run through the Code Institute Python Linter. The results of this led to formatting changes which:
- removed whitespaces 
- removed blank lines 
- aligned indents where required 
- highlighted lines that were over 79 characters

To deal with lines of code that were too long, a backslash "\" was inserted to carry the code onto the next line. 

There are now zero errors shown when running the code through the Python Linter. 

# Bugs
Random ship placement:

The random generation of ship locations was not working correctly which resulted in all the ships having the same [0, 0] co-ordinate. 

![Random generate ships bug](/assets/readMe_images/Random_generate_ships_bug.png)

Upon inspection the size variable was not being handled correctly within a range.

random.randint(0, ((self.size-1))

This was giving a range between 0 and a string which meant the random integer could only ever be 0. This was easily resolved by converting the size variable into an integer: 

random.randint(0, (int(self.size)-1))


# Deployment
To deploy a backend programme such as this one, Heroku has been used. A pure python programme is run in the terminal however using the Code Institute template this programme can be run in a mock terminal through a web based browser. 

The following steps were taken to deploy using Heroku:
- Due to a quirk with the mock terminal, each input requires a "\n" for it to work 
- A list of requirements is required to document the dependencies for the programme. This is created using the command "pip3 freeze > requirements.txt". Heroku will use these when building the app. 
- Within Heroku, a new app is created with a unqiue name. 
- The following settings are used:
    - Config vars: KEY = PORT, VALUE = 8000.
- The following build packs are used (in this order):
    - Python
    - Node JS
- Within deploy, the app is connected to the GitHub repository for Battleships and manually deployed using the required branch. 

This provides a web app that allows the Python code to be run on a web browser. 

# Credits 
[refer to feedback from last assignment on this]

## Acknowledgements:
Thank you to the tutor support at Code Institute for their guidance on various coding problems on this project.

