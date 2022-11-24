import time
from pages.catalog_page import CatalogPage
from pages.login_page import LoginPage

link = "https://www.saucedemo.com/"
link_catalog = "https://www.saucedemo.com/inventory.html"


# AT_002.01.01 | Страница каталога > Отображение данных карточки товара
def test_open_catalog_page(browser):
    page = LoginPage(browser, link)
    page.authorization_standart_user()
    time.sleep(2)
    page = CatalogPage(browser, link)
    page.should_be_current_page(link_catalog)
    page.open_catalog_page_item_img_backpack()
    time.sleep(2)


#     **Шаги:**
# Кликнуть по изображению товара в каталоге https://www.saucedemo.com/inventory.html

# **Ожидаемый результат:**
# На открытой странице присутствует и корректно отображается:
# - фото
# - наименование
# - описание
# - цена
# - кнопка для добавления товара в корзину
# Фото, наименование, описание и цена соответствуют выбранной карточке товара на странице https://www.saucedemo.com/inventory.html.

# **Постусловие**
# 1. Проверить всех пользователей из https://trello.com/c/lHdPWDPH
# 2. Проверить все карточки из https://trello.com/c/6XrNHGso
