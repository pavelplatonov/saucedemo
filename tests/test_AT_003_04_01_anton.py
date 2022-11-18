import time
import pytest
from pages.login_page import LoginPage

link = "https://www.saucedemo.com/"
def test_login_to_item_card(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.login_valid_user()
    page.enter_valid_password()
    page.click_login_btn()
    time.sleep(1)
    assert browser.current_url == 'https://www.saucedemo.com/inventory.html'

    page.add_bike_light()
    page.go_to_cart()
    time.sleep(1)

    assert browser.current_url == 'https://www.saucedemo.com/cart.html'

    page.go_to_bike_light_from_basket()
    time.sleep(1)
    page.go_to_cart()
    time.sleep(1)
    assert browser.current_url == 'https://www.saucedemo.com/cart.html'
