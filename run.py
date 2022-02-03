"""
This is a simple game to find a word in a grid among random characters.
#
Import google spreadsheet library, Credentials and other libraries
"""
import random
import gspread
from google.oauth2.service_account import Credentials

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


import_list = ImportSheet("words")
word = import_list.get_word()
print(word.get("name"))
