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

        # this tearDown just for closing the browser after finishing testing.
    def tearDown(self):
        self.driver.quit()
        logging.info(f'{self.browser.config["browser"]} web driver is closed.\n')

        #  This test is to ensure that the user can search and find books by its author.
    def test_search_a_book_by_author(self):
        print("Test searching books by author -")
        logging.info("*TEST* searching books by author -")
        author_name = "Stephen King"  # Change name of the author searched here
        logging.info(f"The name of the author for the search: {author_name}")
        self.home_page.search_for_a_book(author_name)
        logging.info("Using function (search for a book)")
        search_page = SearchPage(self.driver)
        logging.info("Switching driver to SearchPage")
        self.assertEqual(search_page.search_for_author_name(), author_name.title(), "Error! No match.")
        logging.info("assertEqual if author name displayed in search is equal input author name.")

        #  This test is to ensure that the user can find a book in My Books list and open it.
    def test_find_book_in_my_books_list(self):
        print("Test finding book in my books list -")
        logging.info("*TEST* finding book in my books list -")
        self.home_page.click_on_my_books_button()
        logging.info("Click on my books button in BaseAppPage")
        my_books_page = MyBooksPage(self.driver)
        logging.info("Switching driver to MyBooksPage")
        name_of_the_book = "Return of the King"  # Change name of the book searched here
        logging.info(f"The name of the book for the search: {name_of_the_book}")
        self.assertIn(name_of_the_book, my_books_page.choose_one_of_my_books_by_title(name_of_the_book),
                      "The two titles in the result is not the same.")
        logging.info("assertIn if book input is in book displayed in search")

        #  This test is to ensure that the user can change the rating of a book and the website accept it.
    def test_changing_rating_of_a_book(self):
        print("Test changing rating of a book -")
        logging.info("*TEST* changing rating of a book -")
        name_of_the_book = "The Alchemist"  # Change name of the book searched here
        logging.info(f"The name of the book for the search: {name_of_the_book}")
        self.home_page.search_for_a_book(name_of_the_book)
        logging.info("Using function (search for a book)")
        search_page = SearchPage(self.driver)
        logging.info("Switching driver to SearchPage")
        search_page.first_result_in_search()
        logging.info("Using function (first result in search)")
        before_change = search_page.check_current_rating_of_the_book_open()
        logging.info("Using function (check current rating of the book open) before change")
        search_page.change_rating_of_the_book()
        logging.info("Using function (change rating of the book)")
        after_change = search_page.check_current_rating_of_the_book_open()
        logging.info("Using function (check current rating of the book open) after change")
        self.assertNotEqual(before_change, after_change, "Error! Rating did not change.")
        logging.info("assertNotEqual to ensure the rating before and after HAS changed.")

        # This test is to ensure that the user can change the order of books displayed in his lists.
    def test_changing_order_in_my_books(self):
        print("Test changing order in my books -")
        logging.info("*TEST* changing rating of a book -")
        self.home_page.click_on_my_books_button()
        logging.info("Click on my books button in BaseAppPage")
        my_books_page = MyBooksPage(self.driver)
        logging.info("Switching driver to MyBooksPage")
        order_previous = my_books_page.return_first_book_of_the_list()
        logging.info("Using function (return first book of the list) on previous order")
        my_books_page.change_order_in_my_books()
        logging.info("Using function (change order in my books)")
        order_next = my_books_page.return_first_book_of_the_list()
        logging.info("Using function (return first book of the list) on next order")
        self.assertNotEqual(order_previous, order_next, "Error! Order did not change.")
        logging.info("assertNotEqual to ensure the order before and after HAS changed.")

        # This test is to ensure that the user can add another user as a friend and also deleting the request.
    def test_add_a_friend_and_then_delete_request(self):
        print("Test adding a friend and then deleting the request -")
        logging.info("*TEST* adding a friend and then deleting the request -")
        self.home_page.click_on_friends_button()
        logging.info("Click on friends button in BaseAppPage")
        friends_page = FriendsPage(self.driver)
        logging.info("Switching driver to FriendsPage")
        search_friend_name = "Tzahi"  # Change name of the person searched here
        logging.info(f"The name of a friend for the search: {search_friend_name}")
        friends_page.search_for_a_person_flow(search_friend_name)
        logging.info("Using function (search for a person flow)")
        friends_page.add_as_a_friend_first_person()
        logging.info("Using function (add as a friend first person)")
        time.sleep(2)
        logging.info("Using sleep function to load the content")
        friends_page.click_on_pictures_button()
        logging.info("Click on picture button")
        friends_page.click_on_unfollow_button()
        logging.info("Click on unfollow button")
        time.sleep(2)
        logging.info("Using sleep function to load the content")
        friends_page.click_on_unfollow_confirm_button()
        logging.info("Click on confirm unfollow button")
        time.sleep(2)
        logging.info("Using sleep function to load the content")
        self.assertEqual(friends_page.return_follow_button_state(), "Follow", "Error! still following.")
        logging.info("assertEqual if Follow button is displayed.")


if __name__ == '__main__':
    unittest.main()
