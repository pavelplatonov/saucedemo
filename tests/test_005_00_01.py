import time
from pages.login_page import LoginPage
from pages.locators import CatalogPageLocators


link = "https://www.saucedemo.com/"


def test_login(browser):
    page = LoginPage(browser, link)
    page.open_page()
    page.login_standard_user()
    page.enter_valid_password()
    page.click_login_btn()
    time.sleep(1)
    browser.find_element(*CatalogPageLocators.ADD_TO_CART_SAUCE_LABS_BACKPACK)


# def test_add_product_to_cart(browser)
#     page.


