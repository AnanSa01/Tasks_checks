from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from infra.base_page import BasePage
from logic.base_app_page import BaseAppPage


class HomePage(BaseAppPage):
    SIGN_IN_BUTTON = '//a[@aria-label="Sign in"]//div[@class="yt-spec-touch-feedback-shape__fill"][1]'
    SETTINGS_BUTTON = '//div[@id="end"]//button[@id="button"]'

    SETTINGS_APPEARANCE_BUTTON = '//ytd-toggle-theme-compact-link-renderer//yt-icon[@id="primary-icon"]'
    SETTINGS_APPEARANCE_DARK_BUTTON = '//yt-formatted-string[contains(text(),"Dark theme")]'

    EXPLORE_SPORTS_BUTTON = '//yt-formatted-string[contains(text(),"Sports")]'

    SEARCH_INPUT = '//input[@id="search"]'
    SEARCH_LOGO_BUTTON = '//button[@id="search-icon-legacy"]'

    HAMBURGER_MENU_BUTTON = '//div[@id ="container"]//yt-icon-button[@id="guide-button"]'

    def __init__(self, driver):
        super().__init__(driver)

        self._sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
        self._settings_button = self._driver.find_element(By.XPATH, self.SETTINGS_BUTTON)
        self._explore_sports_button = self._driver.find_element(By.XPATH, self.EXPLORE_SPORTS_BUTTON)
        self._search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        self._search_logo_button = self._driver.find_element(By.XPATH, self.SEARCH_LOGO_BUTTON)


    def click_on_sign_in_button(self):
        self._sign_in_button.click()

    def click_on_settings_button(self):
        self._settings_button.click()

    def click_on_settings_appearance_button(self):
        self._settings_appearance_button = self._driver.find_element(By.XPATH, self.SETTINGS_APPEARANCE_BUTTON)
        self._settings_appearance_button.click()

    def click_on_settings_appearance_dark_mode_button(self):
        self._settings_appearance_dark_button = self._driver.find_element(By.XPATH, self.SETTINGS_APPEARANCE_DARK_BUTTON)
        self._settings_appearance_dark_button.click()

    def click_on_search_input(self):
        self._search_input.click()

    def write_in_search_input(self, user_input):
        self._search_input.send_keys(user_input)

    def click_on_search_logo_button(self):
        self._search_logo_button.click()

    def click_on_explore_sports_button(self):
        self._explore_sports_button.click()








