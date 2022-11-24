import time
from pages.catalog_page import CatalogPage
from pages.locators import (
    CatalogPageLocators,
    MainPageLocators,
    ItemPageLocators,
)
from pages.login_page import LoginPage

link = "https://www.saucedemo.com/"
link_catalog = "https://www.saucedemo.com/inventory.html"


# AT_002.01.01 | Страница каталога > Отображение данных карточки товара
def test_view_exam_item_page_standart_user(browser):
    page = LoginPage(browser, link)
    page.authorization_standart_user()
    time.sleep(2)
    page = CatalogPage(browser, link)
    page.should_be_current_page(link_catalog)

    # Присваиваем переменные для проверяемых элементов в каталоге
    item_img_src_cat = browser.find_element(
        *CatalogPageLocators.ITEM_IMG_BACKPACK
    ).get_dom_attribute("src")
    item_name_cat = browser.find_element(
        *CatalogPageLocators.ITEM_NAME_BACKPACK
    ).text
    item_desc_cat = browser.find_element(
        *CatalogPageLocators.ITEM_DESC_BACKPACK
    ).text
    item_price_cat = browser.find_element(
        *CatalogPageLocators.PRICE_BACKPACK
    ).text
    assert page.element_is_present(
        *CatalogPageLocators.BTN_ADD_BACKPACK
    ) or page.element_is_present(*CatalogPageLocators.BTN_REMOVE_BACKPACK)

    # Переходим на страницу карточки товара
    page.click_element(*CatalogPageLocators.ITEM_IMG_BACKPACK)
    time.sleep(1)
    assert page.element_is_present(
        *ItemPageLocators.BIG_BTN_ADD_BACKPACK
    ) or page.element_is_present(*ItemPageLocators.BIG_BTN_REMOVE_BACKPACK)

    # Присваиваем переменные для проверяемых элементов в карточке товара
    item_img_src_item = browser.find_element(
        *ItemPageLocators.BIG_ITEM_IMG_BACKPACK
    ).get_dom_attribute("src")
    item_name_item = browser.find_element(
        *ItemPageLocators.BIG_ITEM_NAME_BACKPACK
    ).text
    item_desc_item = browser.find_element(
        *ItemPageLocators.BIG_ITEM_DESC_BACKPACK
    ).text
    item_price_item = browser.find_element(
        *ItemPageLocators.BIG_PRICE_BACKPACK
    ).text

    # Сверяем соответствие данных на страницах каталога и карточки
    assert item_img_src_cat == item_img_src_item
    assert item_name_cat == item_name_item
    assert item_desc_cat == item_desc_item
    assert item_price_cat == item_price_item


# AT_002.05.01 Страница каталога > Удалить товар из корзины через каталог
def test_delete_item_standart_user(browser):
    page = LoginPage(browser, link)
    page.authorization_standart_user()
    time.sleep(2)
    page = CatalogPage(browser, link)
    page.click_element(*CatalogPageLocators.BTN_ADD_BACKPACK)
    time.sleep(1)
    assert page.element_is_present(*MainPageLocators.CART_BTN_BAGE)
    assert page.element_is_present(*CatalogPageLocators.BTN_REMOVE_BACKPACK)
    page.click_element(*CatalogPageLocators.BTN_REMOVE_BACKPACK)
    time.sleep(2)
    assert not page.element_is_present(*MainPageLocators.CART_BTN_BAGE)
