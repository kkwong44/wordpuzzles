"""
This is a simple game to find a word in a grid among random characters.
#
Import google spreadsheet library, Credentials and other libraries
"""
import random
import gspread
from google.oauth2.service_account import Credentials
import numpy as np

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
            row = ""
            for y_cord in range(self.length):
                row += self.any_grid[x_cord, y_cord] + " "
            print(row)
        print("\n")


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
        word = self.add_word[0]
        wordsize = len(word)
        downward = random.randint(0, 1)
        reverse = random.randint(0, 1)
        # Compute random position and direction
        if reverse == 1:
            word = word[::-1]
        x_cord = random.randint(0, gridsize - 1)
        y_cord = random.randint(0, gridsize - wordsize)
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

    def get_answer(self):
        """
        Ask and check player's answer. Three attempts are allow for each game.
        """
        word = self.add_word[0]
        wordsize = len(word)
        for attempt in range(3):
            if attempt == 0:
                print(f"Can you find my {wordsize} letters word in the table?")
                print("It can be horizonal, vertical and spelled backwards.\n")

            answer = input("Enter your answer here: ").upper()
            if answer == word:
                print("Well Done! You've found my word.\n")
                break
            elif attempt == 0:
                print(f"\n'{answer}' is not the word that I'm looking for.")
                print(f"You got {2-attempt} attempts left.\n")
            elif attempt == 1:
                print(f"\n'{answer}' is not the word that I'm looking for.")
                print(f"You got {2-attempt} attempt left.\n")
            else:
                print(f"\n'{answer}' is not the word that I'm looking for.")
                print(f"The word is '{word}'\n")


def main():
    """
    Main section to run program
    """
    # Test section used - to get random word from sheet
    import_list = ImportSheet("words")
    word = import_list.get_word()
    print(word.get("name"))


def testing():
    """
    Testing for development
    """
    # Test section to create base grid for puzzel and answer
    grid_size = 6
    grid = Grid(grid_size, "-")
    answer_grid = grid.create_grid()
    print(answer_grid)
    grid.filler = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    puzzle_grid = grid.create_grid()
    print(puzzle_grid)
    # Test section to print grid
    grid.display(answer_grid)
    grid.display(puzzle_grid)
    # Test section to insert word to grid
    word = ["TEST"]
    new_grids = ModifyGrid(puzzle_grid, answer_grid, word)
    new_grids.insert_word()
    print(new_grids.puzzle_grid)
    print(new_grids.answer_grid)
    grid.display(answer_grid)
    grid.display(puzzle_grid)
    # Test section to ask and check answer
    new_grids.get_answer()
    grid.display(answer_grid)


testing()
