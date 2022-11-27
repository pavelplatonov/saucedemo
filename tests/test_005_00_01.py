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
    assert browser.current_url == "https://www.saucedemo.com/cart.html"

    page.click_element(*CartPageLocators.BTN_CHECKOUT)
    page.input_valid_first_name()
    page.input_valid_last_name()
    page.input_valid_zip_code()
    assert page.element_is_present(*CheckoutPageLocators.FIELD_FIRST_NAME)
    assert page.element_is_present(*CheckoutPageLocators.FIELD_LAST_NAME)
    assert page.element_is_present(*CheckoutPageLocators.FIELD_ZIP_CODE)
    assert browser.current_url == "https://www.saucedemo.com/checkout-step-one.html"

    page.click_element(*CartPageLocators.BTN_CONTINUE)
    assert page.element_is_present(*FinishPageLocators.BTN_FINISH)
    assert page.element_is_present(*FinishPageLocators.BTN_CANCEL)

    page.click_element(*FinishPageLocators.BTN_FINISH)
    page.click_element(*FinishPageLocators.BTN_BACK_HOME)


