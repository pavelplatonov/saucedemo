import time
from pages.login_page import LoginPage

link = "https://www.saucedemo.com/"


def test_login(browser):
    page = LoginPage (browser, link)
    page.open_login_page()
    page.login_standard_user()
    page.enter_valid_password()
    page.click_login_btn()
    time.sleep(1)


