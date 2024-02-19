from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.page import Page


class ProductsPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.item_selector = (By.CLASS_NAME, "inventory_item")
        self.item_price_selector = (By.CLASS_NAME, "inventory_item_price")
        self.add_to_cart_selector = (By.CLASS_NAME, "btn_inventory")
        self.cart_selector = (By.CLASS_NAME, "shopping_cart_link")
        self.menu_selector = (By.ID, "react-burger-menu-btn")
        self.logout_selector = (By.ID, "logout_sidebar_link")

    def get_products(self):
        return self.driver.find_elements(*self.item_selector)

    def get_price(self, product):
        return float(product.find_element(*self.item_price_selector).text.replace("$", ""))

    def click_add_to_cart(self, product):
        button = product.find_element(*self.add_to_cart_selector)
        button.click()

    def click_cart(self):
        self.click_element(self.cart_selector)

    def click_menu(self):
        self.click_element(self.menu_selector)

    def click_logout(self):
        button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.logout_selector))
        button.click()
