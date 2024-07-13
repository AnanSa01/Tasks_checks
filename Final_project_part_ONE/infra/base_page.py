from selenium import webdriver


class BasePage:

    # always get driver
    def __init__(self, driver):
        self._driver = driver

        # this function to refresh page from everywhere in the website.
    def refresh_page(self):
        self._driver.refresh()

        # this function to turn back page from everywhere in the website.
    def back_func(self):
        self._driver.back()
