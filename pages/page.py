from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import testconfig


class Page:
    def __init__(self, driver):
        self.driver = driver
        self.url = testconfig.URL

    def get_page(self):
        self.driver.get(self.url)

    def click_element(self, selector, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.click()

    def send_keys_to_element(self, selector, text, wait_time=10):
        element = WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(selector)
        )
        element.send_keys(text)
