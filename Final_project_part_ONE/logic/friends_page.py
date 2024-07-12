import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

from logic.base_app_page import BaseAppPage


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
            print("Error in finding element in FriendsPage")

    def search_for_a_person_flow(self, person_input):
        self._find_friends_input.click()
        self._find_friends_input.send_keys(person_input)
        time.sleep(3)
        self._search_members_button.click()

    def add_as_a_friend_first_person(self):
        self._add_as_a_friend_buttons = self._driver.find_element(By.XPATH, self.ADD_AS_A_FRIEND_BUTTONS)
        self._add_as_a_friend_buttons.click()

    def click_on_pictures_button(self):
        self._click_on_picture_button = self._driver.find_element(By.XPATH, self.CLICK_ON_PICTURE_BUTTONS)
        self._click_on_picture_button.click()

    def click_on_unfollow_button(self):
        self._unfollow_button = self._driver.find_element(By.XPATH, self.UNFOLLOW_BUTTON)
        self._unfollow_button.click()

    def click_on_unfollow_confirm_button(self):
        self._unfollow_confirm_button = self._driver.find_element(By.XPATH, self.UNFOLLOW_CONFIRM_BUTTON)
        self._unfollow_confirm_button.click()

    def return_follow_button_state(self):
        self._follow_button_state = self._driver.find_element(By.XPATH, self.FOLLOW_BUTTON_STATE)
        return self._follow_button_state.text
