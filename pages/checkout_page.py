from selenium.webdriver.common.by import By
from pages.page import Page


class CheckoutPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.firstname_selector = (By.ID, "first-name")
        self.lastname_selector = (By.ID, "last-name")
        self.zipcode_selector = (By.ID, "postal-code")
        self.continue_button_selector = (By.CLASS_NAME, "btn_primary")
        self.total_price_selector = (By.CLASS_NAME, "summary_subtotal_label")
        self.finish_button_selector = (By.ID, "finish")
        self.back_home_button_selector = (By.ID, "back-to-products")

    def input_first_name(self, name):
        self.send_keys_to_element(self.firstname_selector, name)

    def input_last_name(self, name):
        self.send_keys_to_element(self.lastname_selector, name)

    def input_zip_code(self, zip_code):
        self.send_keys_to_element(self.zipcode_selector, zip_code)

    def click_continue(self):
        self.click_element(self.continue_button_selector)

    def total_price_in_cart(self):
        return float(self.driver.find_element(*self.total_price_selector).text.replace("Item total: $", ""))

    def click_finish(self):
        self.click_element(self.finish_button_selector)

    def click_back_home(self):
        self.click_element(self.back_home_button_selector)
