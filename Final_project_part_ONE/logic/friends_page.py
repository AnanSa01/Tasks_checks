import time

from selenium.webdriver.common.by import By

from logic.base_app_page import BaseAppPage


class FriendsPage(BaseAppPage):
    FIND_FRIENDS_INPUT = '//input[@id="q"]'
    SEARCH_MEMBERS_BUTTON = '//input[@value="search members"]'
    ADD_AS_A_FRIEND_BUTTONS = '//a[contains(text(), "Add as a Friend")]'

    def __init__(self, driver):
        super().__init__(driver)
        self._find_friends_input = self._driver.find_element(By.XPATH, self.FIND_FRIENDS_INPUT)
        self._search_members_button = self._driver.find_element(By.XPATH, self.SEARCH_MEMBERS_BUTTON)


    def search_for_a_person_flow(self, person_input):
        self._find_friends_input.click()
        self._find_friends_input.send_keys(person_input)
        time.sleep(3)
        self._search_members_button.click()

    def add_as_a_friend_first_person(self):
        self._add_as_a_friend_buttons = self._driver.find_element(By.XPATH, self.ADD_AS_A_FRIEND_BUTTONS)
        self._add_as_a_friend_buttons.click()
