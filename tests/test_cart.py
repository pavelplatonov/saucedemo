from pages.cart_page import CartPage
import time


link = "https://www.saucedemo.com/"


def test_try_to_checkout_empty_cart_standard_user(browser):
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


def test_checkout_first_page_with_one_item_in_cart_standard_user(browser):
    page = CartPage(browser, link)
    page.open_login_page()
    page.login_standard_user()
    page.enter_valid_password()
    page.click_login_btn()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    first_item = page.find_first_item_name_in_inventory()
    page.click_first_item_add_to_cart()
    page.go_to_cart()

    assert (
        browser.current_url == "https://www.saucedemo.com/cart.html"
    ), "Not cart page"

    assert (
        page.find_item_name_text_in_cart() == first_item
    ), "wrong item in cart"

    page.click_on_checkout_button()

    assert (
        browser.current_url
        == "https://www.saucedemo.com/checkout-step-one.html"
    ), "Not first checkout page"


def test_checkout_first_page_with_one_item_in_cart_problem_user(browser):
    page = CartPage(browser, link)
    page.open_login_page()
    page.login_problem_user()
    page.enter_valid_password()
    page.click_login_btn()

    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    first_item = page.find_first_item_name_in_inventory()
    page.click_first_item_add_to_cart()
    page.go_to_cart()

    assert (
        browser.current_url == "https://www.saucedemo.com/cart.html"
    ), "Not cart page"

    assert (
        page.find_item_name_text_in_cart() == first_item
    ), "wrong item in cart"

    page.click_on_checkout_button()

    assert (
        browser.current_url
        == "https://www.saucedemo.com/checkout-step-one.html"
    ), "Not first checkout page"
