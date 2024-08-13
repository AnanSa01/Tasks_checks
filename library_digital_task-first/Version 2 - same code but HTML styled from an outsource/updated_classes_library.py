from flask import json


# ADD Class of book , and edit the year that it won't be more than the current year (2024)
# In genre you can't type numbers and (!@#@!$) , it must be charachters only.
class UpdatedMyLibrary:
    @staticmethod
    def load_books():
        try:
            with open("books_data.json", "r") as file:
                books = json.load(file)
        except FileNotFoundError:
            books = []
        return books

    @staticmethod
    def save_books(books):
        with open("books_data.json", "w") as file:
            json.dump(books, file, indent=3)
