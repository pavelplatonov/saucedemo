from .base_page import BasePage
from .locators import CatalogPageLocators

link = "https://www.saucedemo.com/inventory.html"


class CatalogPage(BasePage):

    """Открываем страницу каталога"""

    def open_catalog_page(self):
        self.open_page()
        self.should_be_current_page(link)

    """Сохраняем переменные с данными карточек"""

    def open_catalog_page_save_item_info(self):
        self.element_is_present(*CatalogPageLocators)

    """Открываем рюкзак из каталога по фото"""

    def open_catalog_page_item_img_backpack(self):
        self.click_element(*CatalogPageLocators.ITEM_IMG_BACKPACK)
