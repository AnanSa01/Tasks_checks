import logging
import time

from infra.logging_basicConfig import LoggingSetup
from logic.base_app_page import BaseAppPage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *


class FriendsPage(BaseAppPage):
    FIND_FRIENDS_INPUT = '//input[@id="q"]'
    SEARCH_MEMBERS_BUTTON = '//input[@value="search members"]'
    ADD_AS_A_FRIEND_BUTTONS = '//a[contains(text(), "Add as a Friend")]'
    CLICK_ON_PICTURE_BUTTONS = '//table[@id="friendTable"]//tr//td[@width="1%"]'
    UNFOLLOW_BUTTON = '//div[@class="friendFollowModule"]//button//span[contains(text(), "Following")]'
    UNFOLLOW_CONFIRM_BUTTON = '//div[@class="modal__confirmButtonsContainer"]//button[contains(text(),"Confirm")]'
    FOLLOW_BUTTON_STATE = '//button[@class="friendFollowButton friendFollowButton--dark"]'

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("Attempting to find elements in FriendsPage")
        try:
            self._find_friends_input = self._driver.find_element(By.XPATH, self.FIND_FRIENDS_INPUT)
            self._search_members_button = self._driver.find_element(By.XPATH, self.SEARCH_MEMBERS_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element in FriendsPage")

    # this function is to search for a person flow by sending name to the input and clicking search.
    def search_for_a_person_flow(self, person_input):
        self._find_friends_input.send_keys(person_input)
        self._search_members_button.click()

    # this function is to click on the add as a friend button after find the profile in friends search.
    def add_as_a_friend_first_person(self):
        logging.info("Attempting to find elements for add as a friend function")
        try:
            self._add_as_a_friend_buttons = self._driver.find_element(By.XPATH, self.ADD_AS_A_FRIEND_BUTTONS)
        except NoSuchElementException:
            logging.error("Error in finding element for add as a friend function")
        self._add_as_a_friend_buttons.click()

    # this function is to open the user profile.
    def click_on_pictures_button(self):
        logging.info("Attempting to find elements for friend's picture function")
        try:
            self._click_on_picture_button = self._driver.find_element(By.XPATH, self.CLICK_ON_PICTURE_BUTTONS)
        except NoSuchElementException:
            logging.error("Error in finding element for friend's picture function")
        self._click_on_picture_button.click()

    # this function is to unfollow the user when opening his profile.
    def click_on_unfollow_button(self):
        logging.info("Attempting to find elements for unfollow function")
        try:
            self._unfollow_button = self._driver.find_element(By.XPATH, self.UNFOLLOW_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element for unfollow function")
        self._unfollow_button.click()

    # this function to confirm unfollowing the user after clicking unfollow.
    def click_on_unfollow_confirm_button(self):
        logging.info("Attempting to find elements for unfollow confirm function")
        try:
            self._unfollow_confirm_button = self._driver.find_element(By.XPATH, self.UNFOLLOW_CONFIRM_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element for unfollow confirm function")
        self._unfollow_confirm_button.click()

    # this function to return to the test the state of follow button to make self.assureEqual.
    def return_follow_button_state(self):
        logging.info("Attempting to find elements for follow button state function")
        try:
            self._follow_button_state = self._driver.find_element(By.XPATH, self.FOLLOW_BUTTON_STATE)
        except NoSuchElementException:
            logging.error("Error in finding element for follow button state function")
        return self._follow_button_state.text
