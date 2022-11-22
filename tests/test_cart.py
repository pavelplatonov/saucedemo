from pages.cart_page import CartPage
import time


link = "https://www.saucedemo.com/"


def test_try_to_checkout_empty_cart_valid_user(browser):
    page = CartPage(browser, link)
    page.open_login_page()
    page.login_standard_user()
    page.enter_valid_password()
    page.click_login_btn()
    time.sleep(1)
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    page.go_to_cart()
    assert browser.current_url == "https://www.saucedemo.com/cart.html"
    time.sleep(1)

    assert not page.check_element_is_enable(), "Button enabled"
    color = page.find_checkout_button_color()
    assert color == "#c1c7c6", "Button has wrong color"
    # """<-- проверка на серый цвет бэкграунда кнопки"""
    # assert browser.current_url == "https://www.saucedemo.com/cart.html"


def test_try_to_checkout_empty_cart_problem_user(browser):
    page = CartPage(browser, link)
    page.open_login_page()
    page.login_problem_user()
    page.enter_valid_password()
    page.click_login_btn()
    time.sleep(1)
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    page.go_to_cart()
    assert browser.current_url == "https://www.saucedemo.com/cart.html"
    time.sleep(1)

    assert not page.check_element_is_enable(), "Button enabled"
    color = page.find_checkout_button_color()
    assert color == "#c1c7c6", "Button has wrong color"
    # """<-- проверка на серый цвет бэкграунда кнопки"""
    # assert browser.current_url == "https://www.saucedemo.com/cart.html"
