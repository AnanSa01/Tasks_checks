from selenium.webdriver.common.by import By
from youtube_selenium_task.infra.base_page import BasePage


class BaseAppPage(BasePage):
    SEARCH_BAR = '//input[@id ="search"]'
    SEARCH_BUTTON = '//button[@id="search-icon-legacy"]'
    VOICE_SEARCH_BUTTON = '//button[@aria-label ="Search with your voice"]'
    HOME_PAGE_LOGO = '(//yt-icon[@id ="logo-icon"])[1]'
    HAMBURGER_MENU_BUTTON = '//div[@id ="container"]//yt-icon-button[@id="guide-button"]'
    CREATE_BUTTON = '//button[@aria-label="Create"]'
    NOTIFICATIONS_BUTTON = '//button[@aria-label="Notifications"]'
    PROFILE_BUTTON = '//button[@id="avatar-btn"]'
    WATCH_LATER_BUTTON = '//a[@id="endpoint"]//yt-formatted-string[text() = "Watch Later"]'
    LIKED_VIDEOS_BUTTON = '//a[@id="endpoint"]//yt-formatted-string[text() = "Liked videos"]'
    SHOW_MORE_SUBSCRIPTIONS_BUTTON = '//a[@id="endpoint"]//yt-formatted-string[text() = "Show more"]'
    SHOW_LESS_SUBSCRIPTIONS_BUTTON = '//a[@id="endpoint"]//yt-formatted-string[text() = "Show fewer"]'
    ALL_SUBSCRIPTION_BUTTON = '//a[@id="endpoint"]//yt-formatted-string[text() = "All subscriptions"]'

    def _init_(self, driver):
        super().__init__(driver)
        self._search_bar = self._driver.find_element(By.XPATH, self.SEARCH_BAR)
        self._search_button = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON)
        self._voice_search_button = self._driver.find_element(By.XPATH, self.VOICE_SEARCH_BUTTON)
        self._home_page_logo = self._driver.find_element(By.XPATH, self.HOME_PAGE_LOGO)
        self._hamburger_menu_button = self._driver.find_element(By.XPATH, self.HAMBURGER_MENU_BUTTON)
        self._create_button = self._driver.find_element(By.XPATH, self.CREATE_BUTTON)
        self._notifications_button = self._driver.find_element(By.XPATH, self.NOTIFICATIONS_BUTTON)
        self._profile_button = self._driver.find_element(By.XPATH, self.PROFILE_BUTTON)
        self._watch_later_button = self._driver.find_element(By.XPATH, self.WATCH_LATER_BUTTON)
        self._liked_videos_button = self._driver.find_element(By.XPATH, self.LIKED_VIDEOS_BUTTON)
        self._show_more_subscriptions_button = self._driver.find_element(By.XPATH, self.SHOW_MORE_SUBSCRIPTIONS_BUTTON)
        self._show_less_subscriptions_button = self._driver.find_element(By.XPATH, self.SHOW_LESS_SUBSCRIPTIONS_BUTTON)
        self._all_subscription_button = self._driver.find_element(By.XPATH, self.ALL_SUBSCRIPTION_BUTTON)

    def search_bar_input(self, user_input):
        self._search_bar.send_keys(user_input)

    def click_on_search_button(self):
        self._search_button.click()

    def voice_search(self):
        self._voice_search_button.click()

    def go_to_home_page(self):
        self._home_page_logo.click()

    def open_hamburger_menu(self):
        self._hamburger_menu_button.click()

    def create(self):
        self._create_button.click()

    def view_notifications(self):
        self._notifications_button.click()

    def open_profile(self):
        self._profile_button.click()

    def go_to_watch_later(self):
        self._watch_later_button.click()

    def go_to_liked_videos(self):
        self._liked_videos_button.click()

    def show_more_subscriptions(self):
        self._show_more_subscriptions_button.click()

    def show_less_subscriptions(self):
        self._show_less_subscriptions_button.click()

    def view_all_subscriptions(self):
        self._all_subscription_button.click()