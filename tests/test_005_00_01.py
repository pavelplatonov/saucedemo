from pages.login_page import LoginPage
from pages.locators import CatalogPageLocators, MainPageLocators, CartPageLocators, CheckoutPageLocators, FinishPageLocators
from pages.checkout_page import CheckoutPage


link = "https://www.saucedemo.com/"

def test_login(browser):
    page = LoginPage(browser, link)
    page.open_page()
    page.login_standard_user()
    page.enter_valid_password()
    page.click_login_btn()
    browser.find_element(*CatalogPageLocators.BTN_ADD_BACKPACK).click()
    browser.find_element(*MainPageLocators.CART_BTN).click()
    page = CheckoutPage(browser, link)
    page.click_element(*CartPageLocators.BTN_CHECKOUT)
    page.input_valid_first_name()
    page.input_valid_last_name()
    page.input_valid_zip_code()
    page.click_element(*CartPageLocators.BTN_CONTINUE)
    page.click_element(*FinishPageLocators.BTN_FINISH)
    page.click_element(*FinishPageLocators.BTN_BACK_HOME)

