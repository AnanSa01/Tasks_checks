from flask import json


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
