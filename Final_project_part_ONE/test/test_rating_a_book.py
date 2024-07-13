import logging
import time
import unittest

from infra.logging_basicConfig import LoggingSetup
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
        self.search_page.rating_the_book(self.rating_of_the_book)
        logging.info("In tearDown - pressing same rating to remove it")
        self.driver.quit()
        logging.info(f'{self.browser.config["browser"]} web driver is closed.\n')

        # This test is to ensure that the user can rate a book and being saved in the website.
    def test_rating_a_book(self):
        print("Test rating a book -")
        logging.info("*TEST* rating a book -")
        name_of_the_book = "Return of the King"  # Change name of the book searched here
        logging.info(f"Name of the book for the search: {name_of_the_book}")
        self.rating_of_the_book = 5  # Change rating of the book here
        logging.info(f"Giving rating {self.rating_of_the_book} for the book: {name_of_the_book}")
        self.home_page.search_for_a_book(name_of_the_book)
        logging.info("Using function (search for a book)")
        self.search_page = SearchPage(self.driver)
        logging.info("Switching driver to SearchPage")
        self.search_page.first_result_in_search()
        logging.info("Using function (first result in search)")
        self.search_page.rating_the_book(self.rating_of_the_book)
        logging.info("Using function (rating the book)")
        self.assertEqual(self.search_page.check_current_rating_of_the_book_open(), self.rating_of_the_book)
        logging.info("assertEqual if rating displayed equal input rating.")


if __name__ == '__main__':
    unittest.main()
