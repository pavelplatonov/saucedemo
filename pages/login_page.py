from selenium.webdriver import Keys
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import CartPageLocators
from .locators import CatalogPageLocators
from selenium.webdriver.support.color import Color

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

    def authorization_standart_user(self):
        self.open_login_page()
        self.login_standard_user()
        self.enter_valid_password()
        self.click_login_btn()

    def login_standard_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, valid_user)

    def login_problem_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, problem_user)

    def login_locked_out_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, locked_out_user)

    def login_performance_glitch_user(self):
        self.keyboard_input(
            *LoginPageLocators.LOGIN_USER, performance_glitch_user
        )

    def login_invalid_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, "admin")

    def enter_valid_password(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_PASSWORD, valid_password)

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

    def username_error_svg_is_present(self):
        self.element_is_present(*LoginPageLocators.ERROR_ITEM_ON_NAME_FIELD)

    def password_error_svg_is_present(self):
        self.element_is_present(
            *LoginPageLocators.ERROR_ITEM_ON_PASSWORD_FIELD
        )

    def find_error_element_bottom_line_color(self):
        rgb1 = self.browser.find_element(
            *LoginPageLocators.ERROR_ELEMENT_BOTTOM_COLOR
        ).value_of_css_property("border-bottom-color")
        color = Color.from_string(rgb1).hex
        return color

    def add_bike_light(self):
        self.click_element(*CatalogPageLocators.BTN_ADD_BIKE_LIGHT)

    def go_to_cart(self):
        self.click_element(*CatalogPageLocators.CART_BTN)

    def go_to_bike_light_from_basket(self):
        self.click_element(*CatalogPageLocators.IN_BASKET)

    def add_fleece_jacket_to_cart(self):
        self.click_element(*CatalogPageLocators.BTN_ADD_FLEECE_JACKET)

    def click_on_checkout_button(self):
        self.click_element(*CartPageLocators.BTN_CHECKOUT)

    def check_element_is_enable(self):
        return self.browser.find_element(
            *CartPageLocators.BTN_CHECKOUT
        ).is_enabled()

    def find_checkout_button_color(self):
        rgb = self.browser.find_element(
            *CartPageLocators.BTN_CHECKOUT
        ).value_of_css_property("background-color")
        color = Color.from_string(rgb).hex
        return color
