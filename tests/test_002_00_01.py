import time
from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
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
    page.enter_valid_password()
    page.click_login_btn()
    page.should_be_current_page(link_2)

    # count catalog cards
    catalogue = browser.find_element(*CatalogPageLocators.CATALOGUE_LIST)
    count = len(catalogue)
    assert count == 6, 'Общее количество товаро не соответсвует 6'

    # scrolling keyboard
    browser.find_element(*CatalogPageLocators.CART_BTN).send_keys(Keys.END)
    time.sleep(2)
    browser.find_element(*CatalogPageLocators.FOOTER_TEXT)
    time.sleep(2)
