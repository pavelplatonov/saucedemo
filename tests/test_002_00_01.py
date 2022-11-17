import time
from pages.login_page import LoginPage
from pages.locators import CatalogPageLocators

link = "https://www.saucedemo.com/"
link_2 = "https://www.saucedemo.com/inventory.html"

"""TC_002.00.01 | Страница каталога > Просмотр каталога товаров"""


# login valid user
def test_login_standard_user(browser):
    page = LoginPage(browser, link)
    page.open_page()
    page.login_standard_user()
    page.enter_valid_password()
    page.click_login_btn()
    page.should_be_current_page(link_2)


def test_count_catalog_cards(browser):
    catalogue = browser.find_elements(*CatalogPageLocators.CATALOGUE_LIST)
    count = len(catalogue)
    assert count == 6, "Общее количество товаро не соответсвует 6"


def test_menu_sidebar(browser):
    browser.find_element(*CatalogPageLocators.MENU_BTN).click()
    browser.find_element(*CatalogPageLocators.SIDEBAR_BTN_LOGOUT).click()
    # проверяет переход на страницу авторизации
    assert browser.current_url == "https://www.saucedemo.com/"
