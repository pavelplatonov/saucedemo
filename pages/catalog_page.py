from base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from .locators import LoginPageLocators
from .locators import CatalogPageLocators


link = "https://www.saucedemo.com/"
valid_user = "standard_user"
locked_out_user = "locked_out_user"
problem_user = "problem_user"
performance_glitch_user = "performance_glitch_user"
valid_password = "secret_sauce"
link_2 = "https://www.saucedemo.com/inventory.html"


class CatalogPage(BasePage):
    def open_catalog_page(self):
        self.browser.get(self.link)

    def element_is_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True

    def keyboard_input(self, method, locator, keys_text):
        self.browser.find_element(method, locator).send_keys(keys_text)
