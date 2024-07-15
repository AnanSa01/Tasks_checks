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
        time.sleep(10)
        self.home_page = HomePage(self.driver)

    def tearDown(self):
        """
        this tearDown just for closing the browser after finishing testing.
        """
        self.driver.quit()
        logging.info(f'---------- End of test. {self.browser.config["browser"]} web driver is closed. ----------\n')

    def test_search_a_book_by_author(self):
        """
        this function tests searching and finding book by its author not title.
        -----
        test case   #: 009
        requirement #: 005
        """
        logging.info("---------- Initialize Test: searching books by author ----------")
        author_name = "Stephen King"  # Change name of the author searched here
        logging.info(f"The name of the author for the search: {author_name}")
        self.home_page.search_for_a_book(author_name)
        search_page = SearchPage(self.driver)
        self.assertEqual(search_page.search_for_author_name(), author_name.title(), "Error! No match.")
        logging.info("assertEqual if author name displayed in search is equal input author name.")

    def test_find_book_in_my_books_list(self):
        """
        this function tests finding a book in my books list.
        -----
        test case   #: 010
        requirement #: 006
        """
        logging.info("---------- Initialize Test: finding book in my books list ----------")
        self.home_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        name_of_the_book = "Return of the King"  # Change name of the book searched here
        logging.info(f"The name of the book for the search: {name_of_the_book}")
        self.assertIn(name_of_the_book, my_books_page.choose_one_of_my_books_by_title(name_of_the_book),
                      "The two titles in the result is not the same.")
        logging.info("assertIn if book input is in book displayed in search")

    def test_changing_rating_of_a_book(self):
        """
        this function tests changing rating of a book already rated and ensures the website saves the new data.
        -----
        test case   #: 011
        requirement #: 004
        """
        logging.info("---------- Initialize Test: changing rating of a book ----------")
        name_of_the_book = "The Alchemist"  # Change name of the book searched here
        logging.info(f"The name of the book for the search: {name_of_the_book}")
        self.home_page.search_for_a_book(name_of_the_book)
        search_page = SearchPage(self.driver)
        search_page.first_result_in_search()
        before_change = search_page.check_current_rating_of_the_book_open()
        search_page.change_rating_of_the_book()
        after_change = search_page.check_current_rating_of_the_book_open()
        self.assertNotEqual(before_change, after_change, "Error! Rating did not change.")
        logging.info("assertNotEqual to ensure the rating before and after HAS changed.")

    def test_changing_order_in_my_books(self):
        """
        this function tests changing order displayed in user's books list.
        -----
        test case   #: 012
        requirement #: 006
        """
        logging.info("---------- Initialize Test: changing rating of a book ----------")
        self.home_page.click_on_my_books_button()
        my_books_page = MyBooksPage(self.driver)
        order_previous = my_books_page.return_first_book_of_the_list()
        my_books_page.change_order_in_my_books()
        order_next = my_books_page.return_first_book_of_the_list()
        self.assertNotEqual(order_previous, order_next, "Error! Order did not change.")
        logging.info("assertNotEqual to ensure the order before and after HAS changed.")

    def test_add_a_friend_and_then_delete_request(self):
        """
        this function tests adding a user as a friend and deleting the request.
        -----
        test case   #: 013
        requirement #: 007
        """
        logging.info("---------- Initialize Test: adding a friend and then deleting the request ----------")
        self.home_page.click_on_friends_button()
        friends_page = FriendsPage(self.driver)
        search_friend_name = "Tzahi"  # Change name of the person searched here
        logging.info(f"The name of a friend for the search: {search_friend_name}")
        friends_page.search_for_a_person_flow(search_friend_name)
        friends_page.add_as_a_friend_first_person()
        friends_page.click_on_pictures_button()
        friends_page.click_on_unfollow_button()
        friends_page.click_on_unfollow_confirm_button()
        self.assertEqual(friends_page.return_follow_button_state(), "Follow", "Error! still following.")
        logging.info("assertEqual if Follow button is displayed.")


if __name__ == '__main__':
    unittest.main()
