from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logic.base_app_page import BaseAppPage


class HomePage(BaseAppPage):
    SIGN_IN_BUTTON = '//a[@aria-label="Sign in"]//div[@class="yt-spec-touch-feedback-shape__fill"][1]'
    SETTINGS_BUTTON = '//div[@id="end"]//button[@id="button"]'
    DARK_SETTING_BUTTON = '//yt-icon[@class="style-scope ytd-topbar-menu-button-renderer"]'
    SETTINGS_APPEARANCE_BUTTON = '//ytd-toggle-theme-compact-link-renderer//yt-icon[@id="primary-icon"]'
    SETTINGS_APPEARANCE_DARK_BUTTON = '//yt-formatted-string[contains(text(),"Dark theme")]'
    SETTINGS_APPEARANCE_BUTTON_AFTER = '//ytd-toggle-theme-compact-link-renderer//div[@id="label"]'
    EXPLORE_SPORTS_BUTTON = '//yt-formatted-string[contains(text(),"Sports")]'
    SEARCH_INPUT = '//input[@id="search"]'
    SEARCH_LOGO_BUTTON = '//button[@id="search-icon-legacy"]'
    HAMBURGER_MENU_BUTTON = '//div[@id ="container"]//yt-icon-button[@id="guide-button"]'
    VIDEO_SEARCH = '//h3//a'
    HISTORY_BUTTON = '//yt-formatted-string[contains(text(),"History")]'
    LANGUAGE_BUTTON = '//yt-formatted-string[contains(text(),"Language")]'
    HEBREW_LANGUAGE = '//yt-formatted-string[contains(text(),"עברית")]'
    HEBREW_MESSAGE = '//yt-formatted-string[contains(text(),"כדאי להתחיל לחפש")]'

    def __init__(self, driver):
        super().__init__(driver)

        self._sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
        self._settings_button = self._driver.find_element(By.XPATH, self.SETTINGS_BUTTON)
        self._explore_sports_button = self._driver.find_element(By.XPATH, self.EXPLORE_SPORTS_BUTTON)
        self._search_input = self._driver.find_element(By.XPATH, self.SEARCH_INPUT)
        self._search_logo_button = self._driver.find_element(By.XPATH, self.SEARCH_LOGO_BUTTON)
        self._history_button = self._driver.find_element(By.XPATH, self.HISTORY_BUTTON)

    def click_on_sign_in_button(self):
        self._sign_in_button.click()

    def click_on_settings_button(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.SETTINGS_BUTTON)))
        self._settings_button.click()

    def click_on_dark_settings_button(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.DARK_SETTING_BUTTON)))
        self._dark_settings_button = self._driver.find_element(By.XPATH, self.DARK_SETTING_BUTTON)
        self._dark_settings_button.click()

    def click_on_settings_appearance_button(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.SETTINGS_APPEARANCE_BUTTON)))
        self._settings_appearance_button = self._driver.find_element(By.XPATH, self.SETTINGS_APPEARANCE_BUTTON)
        self._settings_appearance_button.click()

    def return_status_appearance_button(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.SETTINGS_APPEARANCE_BUTTON_AFTER)))
        self._settings_appearance_button_after = self._driver.find_element(By.XPATH, self.SETTINGS_APPEARANCE_BUTTON_AFTER)
        return self._settings_appearance_button_after.text

    def click_on_settings_appearance_dark_mode_button(self):
        self._settings_appearance_dark_button = self._driver.find_element(By.XPATH,
                                                self.SETTINGS_APPEARANCE_DARK_BUTTON)
        self._settings_appearance_dark_button.click()

    def click_on_search_input(self):
        self._search_input.click()

    def write_in_search_input(self, user_input):
        self._search_input.send_keys(user_input)

    def click_on_search_logo_button(self):
        self._search_logo_button.click()

    def click_on_explore_sports_button(self):
        self._explore_sports_button.click()

    def return_first_video_text(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.VIDEO_SEARCH)))
        self._video_search = self._driver.find_element(By.XPATH, self.VIDEO_SEARCH)
        return self._video_search.text

    def click_on_history_button(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH,self.HISTORY_BUTTON)))
        self._history_button.click()

    def click_on_language_button(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.LANGUAGE_BUTTON)))
        self._language_button = self._driver.find_element(By.XPATH, self.LANGUAGE_BUTTON)
        self._language_button.click()

    def click_on_hebrew_language(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.HEBREW_LANGUAGE)))
        self._hebrew_language = self._driver.find_element(By.XPATH, self.HEBREW_LANGUAGE)
        self._hebrew_language.click()

    def return_hebrew_message(self):
        WebDriverWait(self._driver, 10).until(EC.visibility_of_element_located((By.XPATH, self.HEBREW_MESSAGE)))
        self._hebrew_message = self._driver.find_element(By.XPATH, self.HEBREW_MESSAGE)
        return self._hebrew_message.text

