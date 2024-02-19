import random
from pages.cart_page import CartPage


def remove_products(driver, products):
    if products > 0:
        cart_page = CartPage(driver)
        random_products = random.choices(cart_page.get_products_in_cart(), k=products)
        for product in random_products:
            cart_page.remove_product(product)
    else:
        print("No products in cart")
        raise Exception("No products in cart")


def go_to_checkout(driver):
    cart_page = CartPage(driver)
    cart_page.click_checkout()
