import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.friends_page import FriendsPage
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.my_books_page import MyBooksPage
from logic.search_page import SearchPage


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login_flow()
        self.home_page = HomePage(self.driver)

    def test_search_a_book_by_author(self):
        print("Test searching books by author -")
        name_of_the_author = "Stephen King"
        self.home_page.search_for_a_book(name_of_the_author)
        search_page = SearchPage(self.driver)
        search_page.search_for_author_name()
        self.assertEqual(search_page.search_for_author_name(), name_of_the_author, "Not the same!")

    def test_find_book_in_my_books_list(self):
        print("Test finding book in my books list -")
        self.home_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        name_of_the_book = "Return of the King"
        self.assertIn(name_of_the_book, my_books_page.choose_one_of_my_books_by_title(name_of_the_book),
                      "Not the same!")

    def test_changing_rating_of_a_book(self):
        print("Test changing rating of a book -")
        self.home_page.search_for_a_book("The Alchemist")
        search_page = SearchPage(self.driver)
        search_page.first_result_in_search()
        before_change = search_page.check_current_rating_of_the_book_open()
        search_page.change_rating_of_the_book()
        after_change = search_page.check_current_rating_of_the_book_open()
        self.assertNotEqual(before_change, after_change, "Error! Rating did not change.")

    def test_changing_order_in_my_books(self):
        print("Test changing order in my books -")
        self.home_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        order_previous = my_books_page.return_first_book_of_the_list()
        my_books_page.change_order_in_my_books()
        order_next = my_books_page.return_first_book_of_the_list()
        self.assertNotEqual(order_previous, order_next, "Error! Still equal.")


if __name__ == '__main__':
    unittest.main()
