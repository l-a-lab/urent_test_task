from selenium.webdriver.common.by import By
from pages.page import Page


class CartPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.item_selector = (By.CLASS_NAME, "cart_item")
        self.remove_button_selector = (By.CLASS_NAME, "cart_button")
        self.continue_button_selector = (By.CLASS_NAME, "btn_secondary")
        self.checkout_button_selector = (By.CLASS_NAME, "checkout_button")

    def get_products_in_cart(self):
        return self.driver.find_elements(*self.item_selector)

    def remove_product(self, product):
        button = product.find_element(*self.remove_button_selector)
        button.click()

    def click_continue_shopping(self):
        self.click_element(self.continue_button_selector)

    def click_checkout(self):
        self.click_element(self.checkout_button_selector)
