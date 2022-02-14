# WordPuzzles
WordPuzzles is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

This is simple game based on classic Word Search Puzzles, more information about the game can be found on [wikipedia](https://en.wikipedia.org/wiki/Word_search). In this game, each puzzle only have one hidden word and clues related to the word will be given to the player.

Click [here](https://kk-wordpuzzle.herokuapp.com) to access live site.

*Screenshot - Mockup on WordPuzzles, generated from [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php)*

![Screenshot on Mockup](readme/images/mockup.png)
___

## Objectives

In this version of game, player is ask to solve puzzles by finding the hidden word in a 6x6 two dimensional grid. The hidden word is placed randomly in the grid and the other cells are filled with random alphabet.

The target audients will be players that wish to test their skills to find the hidden word.

### Application Goals
* Develop a game to test player puzzle solving skills
* To be used to develop and improve user problem solving skills 
* Introduce new words to user's vocabulary

### User Goals
* Use to develop problem solving skills
* Learning new words
___
## Game Design

### Initial Design
Based on the objectives, a game is to be developed to test the player's problem solving skills by searching a word hidden in a grid among with random alphabets.

A process flow chart was created to show the basic processes and logics of the game.

*Process Flow Chart - Initial Design*

![Process Flow Chart](readme/images/process-flow-chart.png)

### *Main Processes*
The following are the main processes to run the game.
* Display description and game instruction
* Display leader board for top 5 ranking
* Ask player to play game
* Select a random word for each puzzle
* Create puzzle grid and answer grid with random base values
* The selected word need to be inserted randomly for each puzzle
* Display puzzle grid with clues about the word
* Ask player to enter answer
* Validation on each answer and return result to player
* Allow 3 attempts to solve each puzzle
* Give further clue for each attempt
* Option to play another puzzle at the end of cureent puzzle
* Display final score
* Display and update leader board if score is within top 5
___
## How to Play
* Instruction is given to the player at the begining of the game.
* For each puzzle, a clue about the hidden word is display on the screen.
* Base on the clue, player need to find the word in the puzzle grid.
* Solve the puzzle and enter the answer.
* If the answer is correct then option is given to solve another puzzle.
* If answer incorrect then player can try again with another answer.
* Only 3 attempts allow for each puzzle. Extra clue will be given to each attempt..
* The answer always show at the end of each puzzle and where the hidden word is on the grid.
* At the end of each puzzle, score will be displayed with option to play another puzzle.
___
## Features
At the beginning of the game, a validation process will be carried out to check the existence of the import spreadsheet. The game will terminate and exit the program with an error message if it can't find the file. When access to the spreadsheet is available then the player will be greeted with a short description and instruction about the game.

![Screenshot on Description](readme/screenshots/description.png)

Then follow by a leader board with the top 5 ranking.

The game will pause at this point and wait for the player’s input response to continue or exit the game.

![Screenshot on Leader Board](readme/screenshots/leaderboard.png)

The player's response will be validated and only accept "Y" or "N". Case is not senstive as the letter will be converted to uppercase. For invalid entry, a messagi with "Invalid Entry" will display and ask to enter "y/n".

If the response is "N" then the game will be terminated with a message saying "You have exit the game".

A puzzle grid with the hidden word will be presented when the player decided to continue to play the game.

![Screenshot on Puzzle Grid](readme/screenshots/puzzle-grid.png)

The following processes will be carried out to create each puzzle:

* Load the words from an external spreadsheet into a list of dictionaries. This action only perform once at the beginning of the game
    * Validation will be check against worksheet
    * Exit program with error message when worksheetdoes not exist
* Create 2 puzzle grids with base values
    * A 6x6 puzzle grid populated with random alphabet
    * A 6x6 answer grid populated with “-“
* Select a word randomly from the list of dictionaries 
    * There is a validation on the length of the word before it can be inserted into the grid. This to ensure the word is not longer than the grid size. If validation failed then it will try another word from the list. It will attempt for 100 times before exit the game with an error message.
* Perform below criteria to insert the word identically into both the puzzle and answer grid
    * Randomly select the direction to place the word horizontally or vertically
    * Randomly spell the word normally or backward
    * Randomly find a starting position to place the word in the grid
* For the first puzzle, display a messages about the hidden word in the puzzle grid and allow 3 attempts to solve the puzzle
* For all puzzles, display a clue about the word (type and length of word)
    * Currently, the list contains words with 4 or 5 letters and it could be a name of an Animal, a Bird or a Fruit

At this point, the game will pause and ask player to enter an answer

Player can enter anything at this point but a basic validation on length will be carried out before comparing the answer. Also all answers will be converted to upper case.

The validation and checking the answer are as follows:
* A message will display to indicate the answer word is too short when the length is shorter than the puzzle word.
* A message will display to indicate the answer word is too long when the length is longer than the puzzle word.
* When the length is matched then the answer word will compare with the puzzle word. The result either correct or incorrect.
* When the answer is matched to the puzzle word then a congratulation message will display. Follow by displaying the answer grid to confirm where the hidden word was.
* When the answer is incorrect then it will display an incorrect message and perform the following processes:
    * Display original clue
    * Display an additional clue with the first letter of the word
    * Display the puzzle grid again
    * Display a message with 2 attempts left to solve the puzzle
    * Ask the player to enter another answer
    * The validation and checking will repeat against the new answer
    * If the answer still incorrect then the process repeats with second letter of the word as an additional clue and indicate there is 1 more attempt left. Player ask to enter another answer.
    * The validation and checking will repeat against the final answer
    * If the answer still incorrect then it will show the answer is wrong and display the puzzle word with the answer grid showing where the word was hidden.
* A score tally will display at the end of each puzzle
* Also, an option is available to play another puzzle

The following are examples as described above:

### *Example - First answer was too short*
![Screenshot on Answer Too Short](readme/screenshots/answer-short.png)
### *Example - Second answer was too long*
![Screenshot on Answer Too Long](readme/screenshots/answer-long.png)
### *Example - Final answer was incorrect*
![Screenshot on Answer Incorrect](readme/screenshots/answer-incorrect.png)
### *Example - A correct answer*
![Screenshot on Answer Correct](readme/screenshots/answer-correct.png)


