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
        try:
            self._find_friends_input = self._driver.find_element(By.XPATH, self.FIND_FRIENDS_INPUT)
            self._search_members_button = self._driver.find_element(By.XPATH, self.SEARCH_MEMBERS_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element in FriendsPage")

    def search_for_a_person_flow(self, person_input):
        """
        this function is to search for a person flow by sending name to the input and clicking search.
        :param person_input: input to search for a user in "Friends"
        """
        self._find_friends_input.send_keys(person_input)
        self._search_members_button.click()

    def add_as_a_friend_first_person(self):
        """
        this dynamic function is to click on the add as a friend button after find the profile in friends search.
        """
        try:
            self._add_as_a_friend_buttons = self._driver.find_element(By.XPATH, self.ADD_AS_A_FRIEND_BUTTONS)
        except NoSuchElementException:
            logging.error("Error in finding element for add as a friend function")
        self._add_as_a_friend_buttons.click()
        time.sleep(2)

    def click_on_pictures_button(self):
        """
        this dynamic function is to open the user profile.
        """
        try:
            self._click_on_picture_button = self._driver.find_element(By.XPATH, self.CLICK_ON_PICTURE_BUTTONS)
        except NoSuchElementException:
            logging.error("Error in finding element for friend's picture function")
        self._click_on_picture_button.click()

    def click_on_unfollow_button(self):
        """
        this dynamic function is to unfollow the user when opening his profile.
        """
        try:
            self._unfollow_button = self._driver.find_element(By.XPATH, self.UNFOLLOW_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element for unfollow function")
        self._unfollow_button.click()
        time.sleep(2)

    def click_on_unfollow_confirm_button(self):
        """
        this dynamic function to confirm unfollowing the user after clicking unfollow.
        """
        try:
            self._unfollow_confirm_button = self._driver.find_element(By.XPATH, self.UNFOLLOW_CONFIRM_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element for unfollow confirm function")
        self._unfollow_confirm_button.click()
        time.sleep(2)

    def return_follow_button_state(self):
        """
        this function returns the state of follow button (Follow/Unfollow) to make self.assureEqual
        :return: (Follow/Unfollow)
        """
        try:
            self._follow_button_state = self._driver.find_element(By.XPATH, self.FOLLOW_BUTTON_STATE)
        except NoSuchElementException:
            logging.error("Error in finding element for follow button state function")
        return self._follow_button_state.text
