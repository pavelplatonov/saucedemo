from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import LoginLocators

link = "https://www.saucedemo.com/"
valid_user = "standard_user"
locked_out_user = "locked_out_user"
problem_user = "problem_user"
performance_glitch_user = "performance_glitch_user"
password = "secret_sauce"


class LoginPage(BasePage):
    def open_login_page(self):
        self.open_page()
        self.should_be_current_page(link)

    def login_standard_user(self):
        self.keyboard_input(*LoginLocators.login_field, valid_user)

    def login_problem_user(self):
        self.keyboard_input(*LoginLocators.login_field, problem_user)

    def login_locked_out_user(self):
        self.keyboard_input(*LoginLocators.login_field, locked_out_user)

    def login_performance_glitch_user(self):
        self.keyboard_input(*LoginLocators.login_field, performance_glitch_user)

    def login_invalid_user(self):
        self.keyboard_input(*LoginLocators.login_field, "admin")

    def enter_valid_password(self):
        self.keyboard_input(*LoginLocators.password_field, password)

    def enter_invalid_password(self):
        self.keyboard_input(*LoginLocators.password_field, "%password")

    def click_login_btn(self):
        self.click_element(*LoginLocators.login_btn)

    def click_enter(self):
        self.keyboard_input(*LoginLocators.password_field, Keys.RETURN)

    def getting_error_text(self):
        elem = self.browser.find_element(*LoginLocators.error_warning)
        text = elem.text
        return text
