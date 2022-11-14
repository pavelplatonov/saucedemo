from pages.login_page import LoginPage
import time


link = "https://www.saucedemo.com/"


def test_try_to_checkout_empty_cart_valid_user(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.login_valid_user()
    page.enter_valid_password()
    page.click_login_btn()
    time.sleep(1)
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html'

    page.go_to_cart()
    assert browser.current_url == 'https://www.saucedemo.com/cart.html'
    time.sleep(1)

    assert not page.check_element_is_enable(), "Button enabled"

    # page.click_on_checkout_button()
    # assert browser.current_url == "https://www.saucedemo.com/cart.html"