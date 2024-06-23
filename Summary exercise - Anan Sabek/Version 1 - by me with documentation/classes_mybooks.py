from flask import json


class MyLibrary:
    @staticmethod
    def load_books():
        try:
            with open("checkinputs.json", "r") as file:
                books = json.load(file)
        except FileNotFoundError:
            books = []
        return books

#one of the main ideas of oop programs is to use the same coding by calling it and with no need to write the same...
#... code more than once
#in this function we are using the load creating a file in json format and put it in read mode with "r" and load all...
#the content of the file inside a list called books
#we are using try and catch, because if we called and loaded a file in read mode and there is no content inside the...
# the file it will not compile and the program would stop - so we did a catch that if this happened just create a new...
#list and put it in books
#and in the end return books
#we can also open the file with: file = open("checkinputs.json", "r") but in this way we should also close file in...
#...the end with file.close , but in this is way in closes automatically and prevent corruption of file

    @staticmethod
    def save_books(books):
        with open("checkinputs.json", "w") as file:
            json.dump(books, file, indent=3)

#and this function for saving books - watch that we calling it with "w" not "a" meaning "write" and not "append"..
#... because after we loaded all the file inside books using function load_books() in this way we made sure that...
#... we are saving every single book in a dict and all of them in one list called books, this way we always make...
#...sure that we are adding the book in order and also it make it easier for us to work with the books as a list...
#in the other functions
# indent=3 makes it easier for us to read the file which makes it move three spaces between each data input