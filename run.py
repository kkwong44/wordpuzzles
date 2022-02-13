"""
This is a simple game to find a word in a grid among random characters.
#
Import google spreadsheet library, Credentials and other libraries
"""
import random
import sys
import gspread
from google.oauth2.service_account import Credentials
import numpy as np
from colorama import Fore, Style
from colorama import init
init()

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('words')


class ImportSheet():
    """
    Access to import list from worksheet words
    """
    def __init__(self, sheet):
        self.sheet = sheet

    def get_word(self):
        """
        Get a word from worksheet
        """
        word_prop = {}
        sheet = SHEET.worksheet(self.sheet)
        total_words = sheet.acell("D1").value
        row_id = random.randint(1, int(total_words))
        row_values = sheet.row_values(row_id)
        word_prop.update({"type": row_values[0]})
        word_prop.update({"length": row_values[1]})
        word_prop.update({"name": row_values[2]})

        return word_prop

    def all_into_dict(self):
        """
        Import all values from worksheet into dictionary
        """
        sheet = SHEET.worksheet(self.sheet)
        words_in_dict = sheet.get_all_records()

        return words_in_dict

    def display_dict(self, dicts, ranking):
        """
        Display dictionary on terminal
        """
        print(Fore.MAGENTA, Style.BRIGHT + "  " + self.sheet.capitalize())
        print()
        for dictionary in dicts:
            line = ""
            for key, value in dictionary.items():
                if key == "success_rate":
                    rate = "{:.1%}"
                    line += "   " + str(key) + ": " + str(rate.format(value))
                else:
                    line += "   " + str(key) + ": " + str(value)
                if key == "rank" and value == ranking:
                    highlight = True
                if key == "rank" and value != ranking:
                    highlight = False
            if highlight is True:
                print(Fore.CYAN + line)
            else:
                print(Fore.MAGENTA + line)
        print(Fore.WHITE)

    def update_sheet(self, leaderboard):
        """
        Update values in leaderboard worksheet
        """
        sheet = SHEET.worksheet(self.sheet)
        if self.sheet.upper() == "LEADERBOARD":
            newlist = []
            for i in range(5):
                vaules = []
                scores = leaderboard[i]
                vaules.append(scores.get("score"))
                vaules.append(scores.get("success_rate"))
                newlist.append(vaules)
            array = np.array(newlist)
            sheet.update('B2', array.tolist())


class Grid:
    """
    Define and build square grids for puzzle and answer
    """
    def __init__(self, length, filler):
        # Grid size
        self.length = length
        self.filler = filler
        self.any_grid = []

    def create_grid(self):
        """
        Create and initialise all items with zero string.
        Fill all items with random characters from input string
        """
        base_grid = np.zeros((self.length, self.length), dtype='U10')

        for x_cord in range(self.length):
            for y_cord in range(self.length):
                base_grid[x_cord, y_cord] = random.choice(self.filler)

        return base_grid

    def display(self, input_grid):
        """
        Unpack lists to display grid in a bare format
        """
        self.any_grid = input_grid
        for x_cord in range(self.length):
            row = "          "
            for y_cord in range(self.length):
                row += self.any_grid[x_cord, y_cord] + " "
            print(Fore.WHITE + row)
        print(Fore.GREEN)


class ModifyGrid:
    """
    Randomly decide the direction to insert the word.
    It can be Left-right, Right-Left, Up-Down or Down_Up
    """
    def __init__(self, puzzle_grid, answer_grid, add_word):
        self.puzzle_grid = puzzle_grid
        self.answer_grid = answer_grid
        self.add_word = add_word

    def insert_word(self):
        """
        Work out the direction and randomly choose a position to insert
        the word. The position must fit the entire word and it need to
        be the same for both puzzle and answer grids.
        """
        gridsize = len(self.puzzle_grid)
        word = self.add_word.get("name")
        wsize = len(word)
        downward = random.randint(0, 1)
        reverse = random.randint(0, 1)
        # Compute random position and direction
        if reverse == 1:
            word = word[::-1]
        x_cord = random.randint(0, gridsize - 1)
        try:
            y_cord = random.randint(0, gridsize - wsize)
        except (ValueError, TypeError):
            return True
        else:
            # Insert word into grid horizontally or vertically
            for letter in word:
                if downward == 0:
                    self.puzzle_grid[x_cord, y_cord] = letter
                    self.answer_grid[x_cord, y_cord] = letter
                else:
                    self.puzzle_grid[y_cord, x_cord] = letter
                    self.answer_grid[y_cord, x_cord] = letter
                y_cord += 1
            return self.puzzle_grid, self.answer_grid

    def hints(self, attempt):
        """
        Provide hints to the answer
        """
        word = self.add_word.get("name")
        hint = word[:attempt + 1]
        print('    Hint: The word begins with "' + hint + '"\n')

    def get_answer(self, grid):
        """
        Ask and check player's answer. Three attempts are allow for each game.
        """
        word = self.add_word.get("name")
        wtype = self.add_word.get("type")
        wsize = len(word)
        score = 0
        for attempt in range(3):
            # Get answer from player
            answer = input(Fore.WHITE + "> Enter your answer here:\n").upper()
            if answer == word:
                print(Fore.GREEN)
                print(f'    Well Done! You have found the word "{word}".\n')
                score = 1
                return score
            # Use appropriate message for incorect answer
            if wsize > len(answer) and attempt < 2:
                print(Fore.WHITE)
                print(f'> Your answer "{answer}" is too short.\n')
                # print(f' "{wtype}" with ({wsize}) letters.\n')
            elif wsize < len(answer):
                print(Fore.WHITE)
                print(f'> Your answer "{answer}" is too long.\n')
                # print(f' "{wtype}" with ({wsize}) letters.\n')
            else:
                print(Fore.WHITE)
                print(f'> Wrong Answer: "{answer}" is not the word. \n')
            # Message to indicate number of attemps left in the game
            if attempt == 0:
                print(Fore.GREEN + f'    "{wtype}" with ({wsize}) letter.\n')
                self.hints(attempt)
                grid.display(self.puzzle_grid)
                print(Fore.WHITE + f'> You have {2-attempt} attempts left.')
            elif attempt == 1:
                print(Fore.GREEN + f'    "{wtype}" with ({wsize}) letter.\n')
                self.hints(attempt)
                grid.display(self.puzzle_grid)
                print(Fore.WHITE + f'> You have {2-attempt} attempt left.')
            else:
                print(Fore.GREEN + f'    ANSWER: The word is "{word}"\n')
        return score


class Game:
    """
    Puzzle game to find a word in a 2 dimensions grid
    """
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.answer_grid = None
        self.puzzle_grid = None
        self.grid = None
        self.import_list = ImportSheet("words")
        self.word_dict = self.import_list.all_into_dict()
        self.import_scores = ImportSheet("leaderboard")
        print(Fore.YELLOW, Style.BRIGHT)
        print("  =================================================== ")
        print(" !                                                   !")
        print(" ! WordPuzzles is a word search puzzle.              !")
        print(" !                                                   !")
        print(" ! The game is to find the hidden word in the table. !")
        print(" !                                                   !")
        print(" ! Type of word and length will be given in each     !")
        print(" ! puzzle and it can be read horizonally, vertically !")
        print(" ! and can spelled backward.                         !")
        print(" !                                                   !")
        print(" ! You have 3 attempts to solve each puzzle.         !")
        print(" !                                                   !")
        print(" ! Enter your answer when you found the word.        !")
        print(" !                                                   !")
        print("  =================================================== ")
        print()

    def initialise(self):
        """
        Initialise grids for each game
        """
        # Create base grids
        self.grid = Grid(self.grid_size, "-")
        self.answer_grid = self.grid.create_grid()
        self.grid.filler = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.puzzle_grid = self.grid.create_grid()

    def display_leaderboard(self, ranking):
        """
        Display Leaderboard
        """
        scores_dict = self.import_scores.all_into_dict()
        self.import_scores.display_dict(scores_dict, ranking)

    def play_puzzle(self):
        """
        Create puzzel game for player to play
        """
        score = 0
        row_id = random.randint(1, len(self.word_dict)-1)
        word_prop = self.word_dict[row_id]
        word = word_prop.get("name")
        wtype = word_prop.get("type")
        wsize = len(word)
        # Insert word to grid
        new_grids = ModifyGrid(self.puzzle_grid, self.answer_grid, word_prop)
        valid_len = True
        try_next = 0
        # Try another word when failed the length test
        # and exit program after 100 attempts
        while valid_len is True:
            valid_len = new_grids.insert_word()
            try_next += 1
            if try_next == 100:
                print(Fore.RED + "> Program Error - Invalid Word Length.")
                sys.exit()
        str1 = f'\n   Can you find "{wtype}" with ({wsize}) '
        str2 = "letter in the table?\n"
        print(Fore.GREEN + str1 + str2)
        self.grid.display(self.puzzle_grid)
        # Ask and check answer
        score = new_grids.get_answer(self.grid)
        self.grid.display(self.answer_grid)
        return score

    def check_leaderboard(self, score, solved, puzzles):
        """
        Check score against leaderboard. Start with rank 5 to rank 1.
        Update worksheet when score is rank top 5
        """
        ranking = 0
        scores_dict = self.import_scores.all_into_dict()
        for i in range(4, -1, -1):
            last_rank = scores_dict[i]
            next_rank = scores_dict[i-1]
            last_score = last_rank.get("score") + \
                (last_rank.get("success_rate") / 10)
            if i == 0:
                next_score = 99999
            else:
                next_score = next_rank.get("score") + \
                    (next_rank.get("success_rate") / 10)
            if score == last_score:
                ranking = i + 1
            elif score > last_score:
                if score > next_score:
                    ranking = i + 1
                    last_rank["score"] = next_rank.get("score")
                    last_rank["success_rate"] = next_rank.get("success_rate")
                else:
                    ranking = i + 1
                    last_rank["score"] = int(score)
                    rate = round(score - int(score), 4) * 10
                    last_rank["success_rate"] = rate
        print(Fore.YELLOW + Style.BRIGHT)
        print(f"   You scored {solved} out of {puzzles}\n")
        if ranking > 0:
            print(f"   Congratulations! Your score is rank top {ranking}.\n")
            self.import_scores.update_sheet(scores_dict)
        return ranking


class Question:
    """
    Validate user answer from input question
    """
    def __init__(self, question):
        self.question = question

    def answer(self):
        """
        Ask question and return answer
        """
        answer = ""
        while answer not in ("Y", "N"):
            if answer == "":
                answer = input(self.question).upper()
            if answer not in ("Y", "N"):
                print("> Invalid Entery!")
                answer = input("> Please enter (y/n).\n").upper()
        return answer


def main():
    """
    Main section to run program
    """
    game = Game(6)
    game.display_leaderboard(None)
    print(Fore.WHITE)
    question = Question("> Are you ready to play (y/n)?\n")
    answer = question.answer()
    if answer == "Y":
        print(Fore.GREEN + "\n   Below is a puzzle with a hidden word.")
        print("   You have 3 attemps to solve the puzzle.")
        solved = 0
        puzzles = 0
        while True:
            game.initialise()
            score = game.play_puzzle()
            solved += score
            puzzles += 1
            rate = round((solved / puzzles) / 10, 4)
            final_score = solved + rate
            msg = f"    You have solved {solved} out of {puzzles}"
            print(Fore.GREEN + msg)
            print(Fore.WHITE)
            question = Question("> Want to play another puzzle (y/n)?\n")
            answer = question.answer().upper()
            # print()
            if answer == "N":
                rank = game.check_leaderboard(final_score, solved, puzzles)
                if rank > 0:
                    game.display_leaderboard(rank)
                print(Fore.WHITE + "> Thank you for playing!")
                print(Style.RESET_ALL)
                break
    else:
        print("> You have exited the game.")
        print(Style.RESET_ALL)


# Python program to execute function main()
# directly or execute when imported
if __name__ == "__main__":
    main()
