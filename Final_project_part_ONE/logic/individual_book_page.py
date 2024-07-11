from selenium.webdriver.common.by import By

from logic.base_app_page import BaseAppPage


class IndividualBookPage(BaseAppPage):
    RATING_BOOK = '//div[@class="Sticky"]//button[@class="baseClass RatingStar--medium RatingStar--selectable"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._rating_book = self._driver.find_elements(By.XPATH, self.RATING_BOOK)

    def rating_the_book(self, rating_input):
        print(rating_input)
        self._rating_book[3].click()

