import time
from selenium.webdriver.common.keys import Keys
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
from pages.locators import CatalogPageLocators

link_2 = "https://www.saucedemo.com/inventory.html"
link = "https://www.saucedemo.com/"


"""TC_002.00.01 | Страница каталога > Просмотр каталога товаров"""

# login standard user
def test_login_standard_user(browser):
# проверка под стандартным юзером
#open login page
    page = LoginPage(browser, link)
    page.full_login_standard_user()
    page.should_be_current_page(link_2)
# # count catalogue cards
#     catalogue = browser.find_elements(*CatalogPageLocators.CATALOGUE_LIST)
#     count = len(catalogue)
#     assert count == 6, 'Общее количество товаро не соответсвует 6'
# # scrolling keyboard

    browser.find_element(*CatalogPageLocators.ITEM_NAME_BACKPACK).send_keys(Keys.END)
    time.sleep(2)
# .ElementNotInteractableException: ошибка нв селектор в футере. линки на социалки тоже не подошли
#     browser.find_element(By.XPATH, "//img[@class = 'footer_robot']").send_keys(Keys.HOME)
#     time.sleep(2)
#     browser.find_element(*CatalogPageLocators.ITEM_NAME_BACKPACK).send_keys(Keys.PAGE_DOWN)
#     time.sleep(2)
#     browser.find_element(By.XPATH, "//img[@class = 'footer_robot']").send_keys(Keys.PAGE_UP)
