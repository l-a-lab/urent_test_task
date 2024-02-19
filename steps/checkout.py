import random
from pages.checkout_page import CheckoutPage


def input_credentials(driver):
    checkout_page = CheckoutPage(driver)
    first_names = ('John', 'Andy', 'Joe')
    last_names = ('Johnson', 'Smith', 'Williams')
    zip_codes = ('12345', '67890', '00000')
    checkout_page.input_first_name(random.choice(first_names))
    checkout_page.input_last_name(random.choice(last_names))
    checkout_page.input_zip_code(random.choice(zip_codes))
    checkout_page.click_continue()


def checkout(driver):
    checkout_page = CheckoutPage(driver)
    input_credentials(driver)
    checkout_page.click_finish()
    checkout_page.click_back_home()


def check_price_in_cart(driver):
    checkout_page = CheckoutPage(driver)
    input_credentials(driver)
    return checkout_page.total_price_in_cart()
