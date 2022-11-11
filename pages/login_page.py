from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import LoginPageLocators


link = "https://www.saucedemo.com/"
valid_user = "standard_user"
locked_out_user = "locked_out_user"
problem_user = "problem_user"
performance_glitch_user = "performance_glitch_user"
valid_password = "secret_sauce"


class LoginPage(BasePage):
    def open_login_page(self):
        self.open_page()
        self.should_be_current_page(link)


    def login_standard_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, valid_user)

    def login_problem_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, problem_user)

    def login_locked_out_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, locked_out_user)

    def login_performance_glitch_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, performance_glitch_user)

    def login_invalid_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, "admin")

    def enter_valid_password(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_PASSWORD, password)

    def enter_invalid_password(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_PASSWORD, "%password")

    def click_login_btn(self):
        self.click_element(*LoginPageLocators.LOGIN_BTN)

    def click_enter(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_PASSWORD, Keys.RETURN)

    def getting_error_text(self):
        elem = self.browser.find_element(*LoginPageLocators.ERROR_WARNING)
        text = elem.text
        return text

    def getting_error_text_with_empty_username_password(self):
        elem = self.browser.find_element(*LoginPageLocators.ERROR_WARNING_1)
        text = elem.text
        return text
