from flask import Flask, render_template, request, redirect, url_for
from updated_classes_library import UpdatedMyLibrary

app = Flask(__name__)


@app.route("/search", methods=["GET", "POST"])
def search():
    searchinput = request.form.get("searchfor").lower()
    books = UpdatedMyLibrary.load_books()
    check_search = []

    for book in books:
        if (book["Title"].lower() == searchinput or book["Author"].lower() == searchinput or book["Year"] == searchinput
                or book["Genre"].lower() == searchinput):
            check_search.append(book)

    return render_template("searchresults.html", check_search=check_search)


@app.route("/removingbooks/<book_title>", methods=["GET", "POST"])
def removingbooks(book_title):

    books = UpdatedMyLibrary.load_books()

    for book in books:
        if book.get("Title") == book_title:
            books.remove(book)
            break

    UpdatedMyLibrary.save_books(books)

    return redirect(url_for("library"))


@app.route("/editingbooks/<book_title>", methods=["GET", "POST"])
def editingbooks(book_title):

    books = UpdatedMyLibrary.load_books()

    if request.method == "POST":
        for book in books:
            if book.get("Title") == book_title:
                book["Title"] = request.form.get("title")
                book["Author"] = request.form.get("author")
                book["Year"] = request.form.get("year")
                book["Genre"] = request.form.get("genre")

        UpdatedMyLibrary.save_books(books)

        return redirect(url_for("library"))

    for book in books:
        if book.get("Title") == book_title:
            return render_template("editingbooks.html", book=book)


@app.route("/library", methods=["GET", "POST"])
def library():
    books = UpdatedMyLibrary.load_books()

    return render_template("library.html", books=books)


@app.route("/addingbooks", methods=["POST", "GET"])
def addingbooks():
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")
    genre = request.form.get("genre")

    book = {"Title": title, "Author": author, "Year": year, "Genre": genre}

    books = UpdatedMyLibrary.load_books()

    books.append(book)

    for book in books:
        if (book.get("Title") is None or book.get("Title") == "" or book.get("Author") == "" or book.get("Year") == ""
                or book.get("Genre") == ""):
            books.remove(book)
        else:
            book["Title"] = book["Title"].title()
            book["Author"] = book["Author"].title()
            book["Genre"] = book["Genre"].title()

    UpdatedMyLibrary.save_books(books)

    return render_template("addingbooks.html")


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
