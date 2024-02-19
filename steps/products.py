import random
from pages.products_page import ProductsPage


def add_random_products_to_cart(driver, num_of_products):
    if num_of_products > 0:
        product_page = ProductsPage(driver)
        random_products = random.choices(product_page.get_products(), k=num_of_products)
        total = 0
        for product in random_products:
            price = product_page.get_price(product)
            product_page.click_add_to_cart(product)
            total += price
        return total
    else:
        print("No products on page")
        raise Exception("No products on page")


def go_to_cart(driver):
    product_page = ProductsPage(driver)
    product_page.click_cart()


def logout(driver):
    product_page = ProductsPage(driver)
    product_page.click_menu()
    product_page.click_logout()
