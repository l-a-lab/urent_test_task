from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.page import Page


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.username_selector = (By.ID, "user-name")
        self.password_selector = (By.ID, "password")
        self.login_button_selector = (By.CLASS_NAME, "btn_action")
        self.error_message_selector = (By.XPATH, '//h3[@data-test="error"]')
        self.get_page()

    def find_username(self):
        self.driver.find_element(*self.username_selector)

    def input_username(self, username):
        self.send_keys_to_element(self.username_selector, username)

    def input_password(self, password):
        self.send_keys_to_element(self.password_selector, password)

    def click_login(self):
        self.click_element(self.login_button_selector)
        WebDriverWait(self.driver, 5).until(EC.url_changes)

    def login_error(self):
        return len(self.driver.find_elements(*self.error_message_selector))

    def get_error_text(self):
        if self.login_error() > 0:
            return self.driver.find_element(*self.error_message_selector).text

    def success_login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login()
        if self.get_error_text():
            print(self.get_error_text())
            raise Exception
