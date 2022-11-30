from .locators import CatalogPageLocators
from .login_page import LoginPage


class CatalogPage(LoginPage):
    def find_all_items_names_in_inventory(self):
        items = self.browser.find_elements(
            *CatalogPageLocators.FIRST_ITEM_NAME_IN_INVENTORY
        )
        return items

    def find_all_items_cost_in_inventory(self):
        costs = self.browser.find_elements(
            *CatalogPageLocators.COST_LOCATOR_FOR_ALL_ITEMS
        )
        return costs
