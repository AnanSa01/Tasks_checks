import logging

from infra.logging_basicConfig import LoggingSetup
import time
import unittest

from infra.browser_wrapper import BrowserWrapper
from logic.friends_page import FriendsPage
from logic.home_page import HomePage
from logic.login_page import LoginPage
from logic.my_books_page import MyBooksPage
from logic.search_page import SearchPage


class MyTestCase(unittest.TestCase):

    # this setUp for opening a browser and doing a login in flow before the test begins.
    def setUp(self):
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])
        logging.info(f'Opening a {self.browser.config["browser"]} web driver.')
        self.login_page = LoginPage(self.driver)
        logging.info("Sending driver to LoginPage")
        self.login_page.valid_login_flow()
        logging.info("Signing in with login flow function")
        self.home_page = HomePage(self.driver)
        logging.info("Switching driver to HomePage")

        # this tearDown function to clean up saved activities and prepare the website for next tests.

    def tearDown(self):
        self.driver.quit()
        logging.info(f'{self.browser.config["browser"]} web driver is closed.\n')

        # This test is to ensure that the user can add multiple books to the list and being saved in the website.
    def test_add_multiple_books_at_once(self):
        print("Test adding multiple books at once -")
        logging.info("*TEST* adding multiple books at once -")
        name_of_series_of_books = "Harry Potter"  # Change the name of the series books here
        logging.info(f"The name of the series of books for the search: {name_of_series_of_books}")
        self.home_page.search_for_a_book(name_of_series_of_books)
        logging.info("Using function (search for a book)")
        search_page = SearchPage(self.driver)
        logging.info("Switching Driver to SearchPage")
        how_many_books_to_add = 3  # Change number of the books added here
        logging.info(f"The number of books to add: {how_many_books_to_add}")
        search_page.add_multiple_books_at_once(how_many_books_to_add)
        logging.info("Using function (add multiple books at once)")
        search_page.click_on_my_books_button()
        logging.info("Click on my books button in BaseAppPage")
        my_books_page = MyBooksPage(self.driver)
        logging.info("Switching driver to MyBooksPage")
        my_books_page.click_on_want_to_read_list()
        logging.info("Click on want to read list")
        self.assertEqual(my_books_page.return_how_many_books_in_my_to_read_list(), how_many_books_to_add, "Error!")
        logging.info("assertEqual if returned value books in the list equal to books input.")


if __name__ == '__main__':
    unittest.main()

    #def test_add_a_new_shelf(self):
    #     self.home_page.click_on_my_books_button()
    #     my_books_page = MyBooksPage(self.driver)
    #     name_of_the_list = "This list for test"
    #     my_books_page.add_new_shelf_functionality(name_of_the_list)
    #     time.sleep(5)
    #     my_books_page.click_on_edit_book_shelves_button()
    #     time.sleep(5)
    #     my_books_page.click_on_edit_book_shelves_button()
    #     time.sleep(5)
    #     my_books_page.click_on_edit_book_shelves_button()
    #     # self.assertEqual(my_books_page.catch_all_lists_in_shelves(),name_of_the_list)
    #     # time.sleep(5)

    # def test_add_book_to_read_list(self):
    #     self.home_page.search_for_a_book("The Republic")
    #     search_page = SearchPage(self.driver)
    #     search_page.first_result_in_search()
    #     search_page.open_more_option_to_book_lists()
    #     search_page.add_book_to_read_list()
    #     search_page.click_done_button_after_adding_to_list()
