from .base_page import BasePage
from .locators import MainPageLocators

"""Шапка и футер сайта общие на всех страницах"""


class MainPage(BasePage):

    """Элементы выпадающего окна sidebar"""

    # Открываем sidebar по бутерброду
    def sidebar_open(self):
        self.click_element(*MainPageLocators.MENU_BTN)

    # Открываем ALLITEMS в sidebar
    def sidebar_click_allitems(self):
        self.click_element(*MainPageLocators.SIDEBAR_BTN_ALL)

    # Открываем ABOUT в sidebar
    def sidebar_click_about(self):
        self.click_element(*MainPageLocators.SIDEBAR_BTN_ABOUT)

    # Logout из системы
    def sidebar_click_logout(self):
        self.click_element(*MainPageLocators.SIDEBAR_BTN_LOGOUT)

    # Сброс системы до дефолтного состояния
    def sidebar_click_reset_app(self):
        self.click_element(*MainPageLocators.SIDEBAR_BTN_RESET)

    # Закрыть sidebar
    def sidebar_close(self):
        self.click_element(*MainPageLocators.SIDEBAR_BTN_CROSS)

    """Элемент перехода на страницу корзины"""

    # Открыть страницу корзины
    def go_to_cart_page(self):
        self.click_element(*MainPageLocators.CART_BTN)

    """"Элементы подвала сайта"""
