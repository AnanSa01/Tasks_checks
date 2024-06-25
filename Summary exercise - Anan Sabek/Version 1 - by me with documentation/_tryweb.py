#Hello, if could you please read the notes from bottom upwards, start under the main.

import json
from flask import Flask, render_template, request, redirect, url_for
from classes_mybooks import MyLibrary

app = Flask(__name__)


@app.route("/search", methods=["GET", "POST"])
def search():
    #this function search for input from user and search it in all four catagories title, author, year and genre

    searchinput = request.form.get("searchfor").lower()
    #with this line we take an input from home page in a search bar, and saved alreay in small letters using lower() so...
    #...we could make sure that the input matches even if the user entered the same word in small letters when...
    #...in json file exist the same word but with capital letters

    print(searchinput)
    #I put this to check myself in console output to make sure im taking in an input from home and also saving it in...
    #small letters

    books = MyLibrary.load_books()
    #like before using class MyLibrary with function load_books() to load all the data from json file into a list of books

    check_search = []
    #building a list to put in it all the books we find in this for loop, because we may find more than one, and we...
    #in a list to send to the search html to show it on the page

    for book in books:
        if (book["Title"].lower() == searchinput or book["Author"].lower() == searchinput or book["Year"] == searchinput
                or book["Genre"].lower() == searchinput):
            check_search.append(book)

    #like we say before we check all fields in all individual dictionaries using or, and if we find one of them we...
    #...  appended it in the check_search list and go back in the loop to check for other variations

    return render_template("search_try.html", check_search=check_search)


#we send this list back to search html page to show it to the user

@app.route("/removingbooks/<book_title>", methods=["GET", "POST"])
def removingbooks(book_title):
    #this function for removing books from library - we can call it from library page, which sends the book title for...
    #... this function and it removes from memory in the json file which removes it from the library page

    books = MyLibrary.load_books()
    #like before using class MyLibrary with function load_books() to load all the data from json file into a list of books

    for book in books:
        if book.get("Title") == book_title:
            books.remove(book)
            break

    MyLibrary.save_books(books)

    return redirect(url_for("library"))


#this function after recieving book title from library, there is no need to check if it is with capital or small...
#...letters we can only reach this function from the books showing in library, and all the books in library is...
#... already checked and changed to capital letters, and here also we check directly from the json files which ...
#...also saved in capital letters
#using for loops we go through the books list that we called it earlier, and check if the book title  we recieved...
#...is equal to the specific book title.
#if true we remove the whole book from the list and using break we get out of the loop and save it back in memory...
#... using json load
#return we use redirect to refresh right away the library back that we didn't leave and wait for other orders


@app.route("/editingbooks/<book_title>", methods=["GET", "POST"])
def editingbooks(book_title):
    #this function for editing books that is already in memory, we can call this function from library page
    #with the argument of the book_title - more on that in the library html page
    #I decided to call this function with the title and not with any other function like id_book: because i wanted to...
    #...solve the problem with the tool i had and to work with my parameters without adding any other parameter
    #but it could also could work with adding premeter like book id or book number

    books = MyLibrary.load_books()
    #like before using class MyLibrary with function load_books() to load all the data from json file into a list of books

    if request.method == "POST":
        for book in books:
            if book.get("Title") == book_title:
                book["Title"] = request.form.get("title")
                book["Author"] = request.form.get("author")
                book["Year"] = request.form.get("year")
                book["Genre"] = request.form.get("genre")

        MyLibrary.save_books(books)

        return redirect(url_for("library"))
    #here we have to path ways, the first is if the request is method is "POST" that means we are editing a book from...
    #...memory - first step: by using a for loop we go through our json file to find a BOOK TITLE with the same name as ...
    #... the parameter we got calling editingbooks() function. after we find the dictonary using [if] we show the details..
    #..of the book and wait for entering new data using request.form.get - after the user prerssing submit the program...
    #... the class MyLibrary with the function save_books and with the arguemnt books to be saved in the class
    #at the editing after finishing submiting using redirect the program takes the user right away to the library

    for book in books:
        if book.get("Title") == book_title:
            return render_template("editingbooks_try.html", book=book)


#this is the second passway - meaning as long as the user didn't call return redirect(url_for("library")), the program..
#..stays in the page of editingbooks_try html with the data of the book we want to edit showing on screen, we do that...
#...by calling that html page of editing with dictionary of the same book we want to edit.


@app.route("/library", methods=["GET", "POST"])
def library():
    #this is the function of showing the content of the library - with option of removing book or editing it
    #we will explain more on this in the html page
    books = MyLibrary.load_books()
    #like before using class MyLibrary with function load_books() to load all the data from json file into a list of books

    return render_template("library_try.html", books=books)


#calls html page library_try with arugment of books list to display it on the page


@app.route("/addingbooks", methods=["POST", "GET"])
def addingbooks():
    #This is the first function - adding new books to the library
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")
    genre = request.form.get("genre")

    #this is the first steps using form.get to save inputs (details on a new book) from the user in a variable
    #from where we get the input? from the html page that calls the function addingbooks using <form action>
    #and the method here is of course POST because we are posting on the website and putting data

    book = {"Title": title, "Author": author, "Year": year, "Genre": genre}

    #and put the input in a dict called book with each key explaining what the value is

    books = MyLibrary.load_books()

    #this book list calls the class MyLibrary with the function load_books() to open the json file with all its content
    #we will explain on this more in the class page

    books.append(book)

    #after caliing the books list from the code line before we append the book dict at the end of the new list of books

    for book in books:
        if (book.get("Title") is None or book.get("Title") == "" or book.get("Author") == "" or book.get("Year") == ""
                or book.get("Genre") == ""):
            books.remove(book)
        else:
            book["Title"] = book["Title"].title()
            book["Author"] = book["Author"].title()
            book["Genre"] = book["Genre"].title()

    #in this for we are doing two things - first step to check if the user entered incomplete data in one of the...
    #4 fields, if he did NOT complete all fields, the book wil be removed from books list using books.remove()
    #if the [if] didn't work, that means the user did input full and accepted details so we into else
    #in else we make sure that the string inputs from the users is saved in the memory as with capital letters using...
    #... title() which make the book data more orderly and arranged
    #and for the year, I made the input be a number so the user can't input anything else, and for books written...
    #...in B.C. means more than 2024 years ago, like the book The Art Of War that I added, I made the user put minus...
    #... next to the year, and in the HTML page using if statement asked if the year is minus to print it...
    #...in positive and next to it the word B.C. else print regular the year alone
    #we make in a for loop not just the recent input, because if the programer added new book straight from the ...
    #... json file in this case we make sure that is also saved in a captial letter like it should be

    MyLibrary.save_books(books)
    #we save it back in the json file using class MyLibrary and function save_books
    #so we will have in this file a list of dictionaries, which will make it easier for us to operate on it later
    #and this actually our memory that will be saved even if we disconnected from the website

    return render_template("addingbooks_try.html")


#after submitting the page stays in the adding books with new writing field, so that the user can added multiple...
#... books with comfort with no need to press each time [add new book button] to come back here and add books


@app.route("/")
def home():
    return render_template("home_try.html")


#just calls home page


if __name__ == "__main__":
    app.run(debug=True)

#Hello Tzahi, I want to tell you that in this version every code written here is by me, in Python and HTML,
#I learned in the holiday basic HTML for a couple of hours, and all the main, classes and html pages I searched for it
#and wrote it with understanding each line. and wrote some functions by myself and one of them ...
#...actually worked in the first try.

#I wrote the functions from the bottom upwards, meaning after I finished working on each function the next one I added..
#.. it above the previous one.

#I thought of other functions to add but I didn't have the time to work on it because of Eid al-Adha feast and also ...
#... because we need to work on the QA project for next week
