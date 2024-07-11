from infra.base_page import BasePage


class PasswordLoginPage(BasePage):
    PASSWORD_INPUT = '//input[@name="Passwd"]'
    PASSWORD_PAGE_NEXT_BUTTON = '//span[contains(text(),"Next")]'

