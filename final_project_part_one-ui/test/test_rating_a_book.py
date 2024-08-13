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

    def setUp(self):
        """
        this setUp for opening a browser and doing a login in flow before the test begins.
        """
        self.browser = BrowserWrapper()
        self.driver = self.browser.get_driver(self.browser.config["base_url"])
        logging.info(f'Opening a {self.browser.config["browser"]} web driver.')
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login_flow()
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        """
        this tearDown function to clean up saved activities and prepare the website for next tests.
        """
        self.search_page.clear_rating_of_the_book(self.rating_of_the_book)
        self.driver.quit()
        logging.info(f'---------- End of test. {self.browser.config["browser"]} web driver is closed. ----------\n')

    def test_rating_a_book(self):
        """
        this function tests rating a book in the website and ensures that the website saves it.
        -----
        test case   #: 008
        requirement #: 004
        """
        logging.info("---------- Initialize Test: rating a book ----------")
        name_of_the_book = "Return of the King"  # Change name of the book searched here
        self.rating_of_the_book = 5  # Change rating of the book here
        logging.info(f"Giving rating {self.rating_of_the_book} for the book: {name_of_the_book}")
        self.home_page.search_for_a_book(name_of_the_book)
        self.search_page = SearchPage(self.driver)
        self.search_page.first_result_in_search()
        self.search_page.rating_the_book(self.rating_of_the_book)
        self.assertEqual(self.search_page.check_current_rating_of_the_book_open(), self.rating_of_the_book)
        logging.info("assertEqual if rating displayed equal input rating.")


if __name__ == '__main__':
    unittest.main()
