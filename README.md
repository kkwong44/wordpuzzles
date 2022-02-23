# WordPuzzles
WordPuzzles is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

This is simple game based on classic Word Search Puzzles, more information about the game can be found on [Wikipedia](https://en.wikipedia.org/wiki/Word_search). In this game, each puzzle only has one hidden word and clues related to the word will be given to the player.

Click [here](https://kk-wordpuzzle.herokuapp.com) to access live site.

*Screenshot - Mockup on WordPuzzles App, generated from [Multi Device Website Mockup Generator](https://techsini.com/multi-mockup/index.php)*

![Screenshot on Mockup](readme/images/mockup.png)

*Mock Terminal - Simulation on WordPuzzles, recorded with Xbox Game Bar*

![Simulation on Mockup](readme/images/mockup-simulation.gif)
___

## Objectives

In this version of game, player is asking to solve puzzles by finding the hidden word in a 6x6 two dimensional grid. The hidden word is placed randomly in the grid and the other cells are filled with random alphabet.

The target audients will be players that wish to test their skills to find the hidden word.

### Application Goals
* Develop a game to test player puzzle solving skills
* To be used to develop and improve user problem solving skills 
* Introduce new words to user's vocabulary

### User Goals
* Use to develop problem solving skills
* Learning new words
___
## How to Play
* Instruction will be given to the player at the beginning of the game.
* The aim of the game is to find a hidden word in a puzzle grid.
* For each puzzle, a clue about the hidden word is display on the screen.
* Base on the clue, player need to find the word in the puzzle grid.
* Solve the puzzle by entering the answer.
* If the answer is correct then option is given to solve another puzzle.
* If answer incorrectly then player can try again with another answer.
* Only 3 attempts allow for each puzzle. Extra clue will be given to each attempt.
* The answer always shows at the end of each puzzle and display where the hidden word is on the grid.
* At the end of each puzzle, score will be displayed with option to play another puzzle.
* A new puzzle will be displayed when player choose to continue otherwise the game end.
* Total score will be displayed when the game end and a new leader board will also be displayed if the score is rank top 5.
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
* Ask player to play game or entering into simulation by the tester with a special word
* Select a random word for each puzzle
* Create puzzle grid and answer grid with random base values
* The selected word needs to be inserted randomly for each puzzle
* Display puzzle grid with clues about the word
* Ask player to enter an answer or answer automatically in simulation mode
* Validation on each answer and return result to player
* Allow 3 attempts to solve each puzzle
* Give further clue for each attempt
* Option to play another puzzle at the end of current puzzle
* Display final score
* Display and update leader board if score is within top 5
___

## Program Requirements

This project was developed from a template created by Code Institute which allows python programs to run in a mock terminal.

From the design, this project is going to use a Google Drive and Google Sheet named “words” to store data for the game.
* A worksheet named “words” is used to store a list of words with its attributes. The process to populate this sheet is done by either manually type it in or copy and paste from external sources. This program only requires read access to this worksheet.
* A worksheet named “leaderboard” is used to store the top 5 ranking scores. Initially, all scores are set to zero and it will be updated by the game. For this reason, the program requires both read and write access to this worksheet.

In order to use Google Drive and Google Sheets, authentication and credentials set up are needed before it can be accessed by the program. The following is a summary of procedure to activate the APIs:
* Go to the Google Cloud Platform webpage and login to an account
* Create a new project
* Select library under APIs and services
* Select and enable Google Drive API
* Create credentials and download credential json file to be used in the project
* Go back to the library, select and enable Google Sheet API
* Upload the credential jason file into the project repository and ensure the file is not share publicly
* Use the client email from the credential jason file to share the Google Sheet

To use Google Sheet API, 2 dependencies are needed to install into the project.
* Authentication to access the Google Cloud Project
* gspread library to access the spreadsheet

The command to install these packages is "pip3 install gspread google-auth"

After the packages have been installed then it needs to be imported into the python program file with an IAM configuration. The following is the section of the code required to access the spreadsheet.

The following section of code was used and it is originated from Code Institute Love Sandwich project.

>import gspread
>
>from google.oauth2.service_account import Credentials
>
>SCOPE = [
>    "https://www.googleapis.com/auth/spreadsheets",
>    "https://www.googleapis.com/auth/drive.file",
>    "https://www.googleapis.com/auth/drive"
>   ]
>
>CREDS = Credentials.from_service_account_file('creds.json')
>
>SCOPED_CREDS = CREDS.with_scopes(SCOPE)
>
>GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

The following libraries or modules are also needed to run the program.
* random (number generator module)
* sys (module for System-specific parameters and function)
* numpy (library for scientific computing with Python)
* colorama (for producing colored terminal text)

The reasons to use these libraries and modules are to perform specific tasks as listed below.
* random method is use from the random library
* The exit() method is use from the sys library to exit program cleanly
* gspread is use to access Google Sheet
* google.oauth2.service_account is use for Credentials
* numpy is use for setting up the base values for the grids and update worksheet
* colorama is use to make colour text on terminal
___

## Features
At the beginning of the game, a validation process will be carried out to check the existence of the import spreadsheet. The game will terminate and exit the program with an error message if it can't find the file. When access to the spreadsheet is available then the player will be greeted with a short description and instruction about the game.

*Example on Description and Instruction*

![Screenshot on Description](readme/screenshots/description.png)

Then follow by displaying the leader board with the top 5 ranking.

The information on the leader board is also held in an external worksheet called "leaderboard". This information is imported and load it into a list of dictionaries.
* Validation will be check against this worksheet
* Exit program with error message when worksheet does not exist

The game will pause at this point and wait for the player’s input response to continue or exit the game.

*Example on Leader Board*

![Screenshot on Leader Board](readme/screenshots/leaderboard.png)

The player's response will be validated and only accept "Y" or "N". Case is not sensitive as the letter will be converted to uppercase. For invalid entry, a message with "Invalid Entry" will display and ask to enter "y/n".

* Player can continue the game by entering “Y”

* If the response is "N" then the game will be terminated with a message saying "You have exit the game".

* There is no suggestion in the game to run simulation but at this point, tester can run the game in a simulation mode by entering the word “simulation”. This will give tester an option to run 100 puzzles automatically.

    *Example on entering into simulation mode*

    ![Screenshot on Simulation Mode](readme/screenshots/simulation1.png)

    *Example when simulation end*

    ![Screenshot on Simulation Run](readme/screenshots/simulation2.png)

A puzzle grid with the hidden word will be presented when the player decided to continue to play the game.

*Example when player continue to play*

![Screenshot on Puzzle Grid](readme/screenshots/puzzle-grid.png)

The following processes will be carried out to create each puzzle:

* Import and load the words from an external worksheet "words" into a list of dictionaries. This action only performs once at the beginning of the game
    * Validation will be check against this worksheet
    * Exit program with error message when worksheet does not exist
* Create 2 puzzle grids with base values
    * A 6x6 puzzle grid populated with random alphabet
    * A 6x6 answer grid populated with “-“
* Select a word randomly from the list of dictionaries 
    * There is a validation on the length of the word before it can be inserted into the grid. This to ensure the word length is no longer than the grid size. If validation failed then it will try another word from the list. It will attempt for 100 times before exit the game with an error message.
* Perform below criteria to insert the word identically into both the puzzle and answer grid
    * Randomly select the direction to place the word horizontally or vertically
    * Randomly spell the word normally or backward
    * Randomly find a starting position to place the word in the grid
* For the first puzzle, display messages about the hidden word in the puzzle grid and allow 3 attempts to solve the puzzle
* For all puzzles, display a clue about the word (type and length of word)
    * Currently, the list contains words with 4 or 5 letters and it could be a name of an Animal, a Bird or a Fruit

At this point, the game will pause and ask player to enter an answer. In simulation mode, a random answer based on the puzzle word will be generated so it can automatically answer this question with either a correct or an incorrect answer.

Player can enter anything at this point but a basic validation on length will be carried out before comparing the answer. Also, all answers will be converted to upper case.

The validation and checking the answer are as follows:
* A message will display to indicate the answer word is too short when the length is shorter than the puzzle word.

    *Example - First answer was too short*

    ![Screenshot on Answer Too Short](readme/screenshots/answer-short.png)
* A message will display to indicate the answer word is too long when the length is longer than the puzzle word.

    *Example - Second answer was too long*

    ![Screenshot on Answer Too Long](readme/screenshots/answer-long.png)
* When the length is matched then the answer word will compare with the puzzle word. The result either correct or incorrect.

    *Example - Final answer was incorrect*

    ![Screenshot on Answer Incorrect](readme/screenshots/answer-incorrect.png)
* When the answer is matched to the puzzle word then a congratulation message will display. Follow by displaying the answer grid to confirm where the hidden word was.

    *Example - A correct answer*

    ![Screenshot on Answer Correct](readme/screenshots/answer-correct.png)
* When the answer is incorrect then it will display an incorrect message and perform the following processes *(messages as shown in previous screenshots)*:
    * Display original clue
    * Display an additional clue with the first letter of the word
    * Display the puzzle grid again
    * Display a message with 2 attempts left to solve the puzzle
    * Ask the player to enter another answer
    * The validation and checking will repeat against the new answer
    * If the answer still incorrect then the process repeats with second letter of the word as an additional clue and indicate there is 1 more attempt left. Player ask to enter another answer.
    * The validation and checking will repeat against the final answer
    * If the answer still incorrect then it will show the answer is wrong and display the puzzle word with the answer grid showing where the word was hidden.
* A score tally will display at the end of each puzzle.
* Also, an option is available to play another puzzle.
* The processes will repeat and create a new puzzle grid if the player choose to play again. Otherwise, the game will end with a message.

When the player wishes to end the game, the score in this session will compare the scores in the leader board before displaying a message to thank the player for playing the game.

*Example - Exit Game*

![Screenshot on Exit Game](readme/screenshots/end-game.png)

If the score is within top 5 then a congratulation message will be displayed with the leader board and indicate the position you have achieved. This mean the leader board will be adjusted to cater the new entry and remove the lowerest score on the table.

The ranking calculation is based on the following:
* Total number of solved puzzles and the success rate of the game
* Success rate is a percentage which calculated by (number of solved puzzle / Total number of puzzles played) * 100

The external worksheet will be updated with the new leader board scores.
* Validation on worksheet "leaderboard" will be checked
* Exit program with error message when worksheet does not exist

*Example - Rank Top 5*

![Screenshot on Rank Top 5](readme/screenshots/top5.png)
___
## Future Features
The following features can be developed in the future to add values to the game and user experiences.
* Add player login details.
* Modify leader board to include player’s name
* Increase grid size and ability to change size based on the word length
* Build an extensive list of words with length beyond 5 letters
* Add extra hidden words in puzzle
___
## Data Model
The data model for this project is based on classes.

*A class “ImportSheet” is used to access the spreadsheet*
* Method to read and import data from worksheet to list
* Method to display imported list to terminal as a table
* Method to update worksheet

*A class “Grid” is used for the basic grid.*
* Method to create Puzzle and Answer grid.
* Method to display Puzzle and Answer grid.

*A class “ModifyGrid” is used to modify the basic grid.*
* Method to insert hidden word in both puzzle and answer grids,
* Method to get answer from player
* Method to give hints

*A class “Game” is used for the game*
* Method to initialize the game
* Method to display the leader board
* Method to play puzzle
* Method to check score against leader board

*A class “Question”for questions*
* Method to response question
* Method for tester to entering into simulation mode

*Main function “main” to run the game*
* Run game from start till player end the game
* Ask player to play game
* Check player answers and act accordingly
* Tally player’s score
* Check player’ score against leader board
* Update leader board appropriately at the end of the game
___
## Validator Testing
PEP8 linter online checker was used to check the python code and it has passed the test.

![PEP8 Report](readme/testing/pep8-report.png)
___
## Testing
The following tests were manually executed to test the functionalities of the game.

One of the tests is a simulation to run 100 puzzles by itself.

All built in exception handlings were tested and passed.

The test results are as expected and passed on both manual and simulation testing.

*Test Report*

![Test Report 1](readme/testing/test-report-1.png)
![Test Report 2](readme/testing/test-report-2.png)
![Test Report 3](readme/testing/test-report-3.png)
![Test Report 4](readme/testing/test-report-4.png)
___
## Bugs
**Bugs Identified and Resolved**

*Bug Fixed on Google Sheet Request Access Limitation*

* Initially, the puzzle word was randomly selected from the external spreadsheet directly for each puzzle. This is fine until a load test was carried out by selecting a random word in quick successions. It was noticed from the load test that Google Sheet has a limitation on number of request access for each minute. This cause the test failed and the program aborted with error messages.

* To eliminate this potential problem, the process for getting a random word has changed from the spreadsheet. The solution is to import the list of words from the worksheet into a list of dictionaries at the beginning of the game. This means the program can now selecting a random word from memory rather than from an external source.

* When implementing the above solution, it was found the process was working fine until load test was carried out. Again, it was the limitation on access to Google Sheet. This bug was identified due to the fact this process was executed inside the initialisation for each puzzle. This means the program is trying to import the list from the worksheet for each puzzle. The solution for this problem is to relocate this action outside the initialisation stage.

*Bug Fixed on Leader Board Calculation*

* During development it was found there is a bug with the leader board that it updates the result incorrectly. Basically, the logic for calculating the best score was wrong. Initially, the best score was calculated by adding the number of puzzles solved and the success rate together but the logic did not take into account for 100% success rate. The logic is to convert the percentage to (0 to 1) meaning 1 is 100% before adding to the number of puzzles solved. So effectively the number of puzzles solved will increase by 1 when the success rate is 100% which causing the wrong results on the leader board. This problem was fixed by changing the logic in the calculation.

**Unfix Bugs**

There are no known bugs to be fixed.
___
## Deployment
This project has been deployed in Heroku and use a mock terminal to run the program.
### Tools
* GitHub is a code hosting platform for version control and collaboration
* Gitpod is a ready-to-code developer environment
* Heroku for building, deploying, and managing apps

### Development processes

* All the development works are carried out in Gitpod
* Create a repository in Github through Gitpod
* Start the project from a template written by Code Institute. The full template can be copied from [here](https://github.com/Code-Institute-Org/python-essentials-template)

    **Repeat the following until project completion**

* Developing your site, save your project in your Gitpod workspaces
* Use git add command to add files to local repository
* Use git commit command to commit the changes to local repository

### Deployment to Github Pages

* Use git push to upload local repository content (Gitpod) to a remote repository (Github)
* The deployed app only use the latest code that has been pushed to Github

### Deployment to Heroku

In order to run this program in Heroku, the dependencies on this project also need to be deployed. This is done by submitting the following command to create the requirement.txt file.
* pip3 freeze > requirements.txt

The requirements.txt will includes dependencies for Google authentication, gspread, numpy, sys, PyPi modules and colorama.

It was noticed that this command did not include the colorama and the following was manually added to the list in the file.
* colorama==0.4.4

This file needs to be pushed to github before Heroku can use this file to include the dependencies for the program.

The following are the steps to deploy the project to Heroku.
1. Go to Heroku account and click "Create a new app".
2. After choosing the app name and setting the region, press "Create app".
3. Go to "Settings" and navigate to Config Vars.
4. Add a Config Var with a key word of called CREDS and use the contents from credential json file as the value.
5. Add another Config Var with a key word of called PORT and a value of 8000.
6. Navigate to Buildpacks in the Settings and add buildpacks for Python and NodeJS. Must add these buildpacks in this order.
7. Go to "Deploy" tab section. Scroll down and set Deployment Method to GitHub.
8. Select the repository to be deployed and connect it to Heroku.
9. Check "main" is selected for the branch in the deploy section and select "Enable Automatic Deploys".
10. Click "Open App" at the top when its finished deploy the app. A new tab page will open with your application.

The deployed app can be found [here](https://kk-wordpuzzle.herokuapp.com).

***You can use GitHub Desktop to clone and fork repositories that exist on GitHub.***

Click [here](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop) for more information on Cloning and forking repositories from GitHub Desktop.
___
## Tools
The tools used to carry out the development and deployment on this project are:
* Gitpod and Github
* Google Drive and Google Spreadsheet
* Python modules and external libraries such as Numpy
* Chrome Dev Tools
* Webpage Screenshots - Chrome app extension (FireShot)
* [Lucid Chart](https://www.lucidchart.com/) for creating flow chart
* [PEP8 online checker](http://pep8online.com/) for code validation
* [Heroku](https://id.heroku.com/login) for building, deploying, and managing apps
* [Xbox Game Bar](https://www.microsoft.com/en-us/p/xbox-game-bar/9nzkpstsnw4p?activetab=pivot:overviewtab) was used to records the screen
* [ezgif.com](https://ezgif.com/) was used to convert mp4 to a gif
___
## Credits
* [Template](https://github.com/Code-Institute-Org/python-essentials-template) created by [Code Institute](https://codeinstitute.net/) for running mock terminal in deployment
* [WORDMOM](https://www.wordmom.com/) website for List of words
* [Wikipedia](https://en.wikipedia.org/wiki/Word_search) on wordsearch
* [W3Schools](https://www.w3schools.com/python/default.asp) for research, examples and techniques in Python programming
* [gspread](https://docs.gspread.org/en/latest/user-guide.html) examples and usage
* [numpy](https://numpy.org/) examples and usage
* [colorama](https://pypi.org/project/colorama/) examples and usage
___
## Acknowledgment
I would like to thank the following to support the development of this site.

* Learning Support - Code Institute
* Mentoring Support - Daisy McGirr