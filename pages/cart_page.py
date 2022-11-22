from .base_page import BasePage
from .locators import CartPageLocators
from .locators import CatalogPageLocators
from .locators import LoginPageLocators
from selenium.webdriver.support.color import Color


link = "https://www.saucedemo.com/"
valid_user = "standard_user"
locked_out_user = "locked_out_user"
problem_user = "problem_user"
performance_glitch_user = "performance_glitch_user"
valid_password = "secret_sauce"


class CartPage(BasePage):
    def open_login_page(self):
        self.open_page()
        self.should_be_current_page(link)

    def login_standard_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, valid_user)

    def login_problem_user(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_USER, problem_user)

    def login_performance_glitch_user(self):
        self.keyboard_input(
            *LoginPageLocators.LOGIN_USER, performance_glitch_user
        )

    def enter_valid_password(self):
        self.keyboard_input(*LoginPageLocators.LOGIN_PASSWORD, valid_password)

    def click_login_btn(self):
        self.click_element(*LoginPageLocators.LOGIN_BTN)

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

    def find_item_name_text_in_cart(self):
        items_text = self.browser.find_element(
            *CartPageLocators.ELEMENT_IN_CART
        ).text
        return items_text

    def find_first_item_name_in_inventory(self):
        first_item = str(
            self.browser.find_element(
                *CatalogPageLocators.FIRST_ITEM_NAME_IN_INVENTORY
            ).text
        )
        return first_item

    def click_first_item_add_to_cart(self):
        self.click_element(*CatalogPageLocators.FIRST_ITEM_BTN_ADD_TO_CART)
