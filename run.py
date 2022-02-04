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


testing()
