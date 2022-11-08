import time
import pytest
from pages.login_page import LoginPage


link = "https://www.saucedemo.com/"
valid_user = "standard_user"
locked_out_user = "locked_out_user"
problem_user = "problem_user"
performance_glitch_user = "performance_glitch_user"
valid_password = "secret_sauce"


"""TC_001.00.01 | Страница авторизации > Авторизация стандартного пользователя с валидными данными"""


@pytest.mark.smoke
def test_login_valid_user(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.login_valid_user()
    page.enter_valid_password()
    page.click_login_btn()
    page.should_be_current_page("https://www.saucedemo.com/inventory.html")


"""TC_001.00.02 | Страница авторизации > Авторизация заблокированного пользователя с валидными данными"""


def test_locked_out_user(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.login_locked_out_user()
    page.enter_valid_password()
    page.click_login_btn()
    error_text = page.getting_error_text()
    assert (
        error_text == "Epic sadface: Sorry, this user has been locked out."
    ), "wrong warning text"
    """скриншот результата"""
    page.take_screenshot(test_name="test_locked_out_user")


"""TC_001.00.03 | Страница авторизации > Авторизация проблемного пользователя с валидными данными"""


def test_problem_user(browser):
    page = LoginPage(browser, link)
    start_loading_counter = time.perf_counter()
    page.open_login_page()
    page.login_problem_user()
    page.enter_valid_password()
    page.click_login_btn()
    loading_time = time.perf_counter() - start_loading_counter
    page.should_be_current_page("https://www.saucedemo.com/inventory.html")
    assert loading_time <= 30, "loading time exceed 30 seconds"


"""TC_001.00.04 | Страница авторизации > Авторизация performance glitch user с валидными данными"""


@pytest.mark.xfail
def test_performance_glitch_user(browser):
    page = LoginPage(browser, link)
    start_loading_counter = time.perf_counter()
    page.open_login_page()
    page.login_performance_glitch_user()
    page.enter_valid_password()
    page.click_login_btn()
    loading_time = time.perf_counter() - start_loading_counter
    page.should_be_current_page("https://www.saucedemo.com/inventory.html")
    assert loading_time <= 15, "loading time exceed 15 seconds"


"""TC_001.00.05 | Страница авторизации > Авторизация стандартного пользователя с валидным логином и пустым паролем"""


def test_login_valid_user_empty_password(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.login_valid_user()
    page.click_login_btn()
    error_text = page.getting_error_text()
    assert error_text == "Epic sadface: Password is required", "wrong warning text"
    page.take_screenshot(test_name="test_empty_password")


"""TC_001.00.06 | Страница авторизации > Авторизация с невалидным пользователем и валидным паролем"""


def test_login_invalid_user_valid_password(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.login_invalid_user()
    page.enter_invalid_password()
    page.click_login_btn()
    error_text = page.getting_error_text()
    assert (
        error_text
        == "Epic sadface: Username and password do not match any user in this service"
    ), "wrong warning text"
    page.take_screenshot(test_name="test_login_invalid_user")


"""TC_001.00.07 | Страница авторизации > Авторизация стандартного пользователя с невалидным паролем"""


def test_login_valid_user_invalid_password(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.login_valid_user()
    page.enter_invalid_password()
    page.click_login_btn()
    error_text = page.getting_error_text()
    assert (
        error_text
        == "Epic sadface: Username and password do not match any user in this service"
    ), "wrong warning text"
    page.take_screenshot(test_name="test_invalid_password")


"""TC_001.00.09 | Страница авторизации > Авторизация стандартного 
    пользователя с валидными данными и вводом через Enter"""


def test_login_valid_user_valid_password_enter_btn(browser):
    page = LoginPage(browser, link)
    page.open_login_page()
    page.login_valid_user()
    page.enter_valid_password()
    page.click_enter()
    page.should_be_current_page("https://www.saucedemo.com/inventory.html")
