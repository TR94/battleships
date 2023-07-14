# Battleships - Python based game

This game mimics the classic Battleships game and allows players to interact through the terminal to play against a computer. The player can choose the board size and number of ships for the game and inputs their row/column guess on each round. The game continues until either the computer or the player sinks all of the opponents ships. 

This programme has been made to complete the third project within the Code Institute Full Stack Developer course and focuses on the use of the Python language. It is run on a Code Institute template that allows the terminal to be run in a webpage for viewing. 

Link to live project: ...Heroku

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
* - individual grid location
@ - ship, visual location of the ship, only used on the player board 
X - hit, ship that has been hit 
O - miss, grid location that didn’t hit a ship

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

![Battleships quit game]()

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
Accessibility wasn’t considered for backend Python programming 

# Testing
[Refer to feedback from last assignment]

## User Goals
The user goals were set-up at the start of development during the Strategy phase and reviewed again during the Skeleton phase. The content requirements have been reviewed against the finished website: 

## Manual Testing
### Functionality testing:

### Responsiveness 

### Code Validation

PEP8 

# Bugs
Random ship placement:
The random generation of ship locations was not working correctly which resulted in all the ships having the same [0, 0] co-ordinate. 

![Random generate ships bug](/assets/readMe_images/Random_generate_ships_bug.png)

Upon inspection the size variable was not being handled correctly within a range.

random.randint(0, ((self.size-1))

This was giving a range between 0 and a string which meant the random integer could only ever be 0. This was easily resolved by converting the size variable into an integer: 

random.randint(0, (int(self.size)-1))


# Deployment



# Credits 

[refer to feedback from last assignment on this]

## Acknowledgements: