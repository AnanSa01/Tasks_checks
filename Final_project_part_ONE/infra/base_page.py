from selenium import webdriver


class BasePage:

    # Always get driver
    def __init__(self, driver):
        self._driver = driver

    def refresh_page(self):
        self._driver.refresh()

    def back_func(self):
        self._driver.back()