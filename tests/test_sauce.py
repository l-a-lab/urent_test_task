import allure
import pytest

import testconfig
from steps import login, products, cart, checkout


@pytest.mark.parametrize("username, password", [(testconfig.USER, testconfig.PASSWORD)])
def test_saucedemo(driver, username, password):
    with allure.step('Перейти на сайт: https://www.saucedemo.com'):
        login.go_to_login_page(driver)

    with allure.step('Проверить наличие поля Username используя уникальный адрес id'):
        login.check_username_field(driver)

    with allure.step('Авторизоваться под пользователем «standard_user».'):
        login.login_user(driver, username, password)

    with allure.step('Добавить два случайных товара в корзину.'):
        products.add_random_products_to_cart(driver, 2)

    with allure.step('Перейти в корзину, удалить один любой из товаров из корзины.'):
        products.go_to_cart(driver)
        cart.remove_products(driver, 1)

    with allure.step('Подтвердить покупку, ввести любые данные пользователя.'):
        cart.go_to_checkout(driver)
        checkout.checkout(driver)

    with allure.step(
        'Подсчитать общую сумму товаров и сверить данную сумму с итоговой в корзине.'
        '(проверить правильно ли подсчитывает корзина общую сумму покупки)'
            ):
        total_price = products.add_random_products_to_cart(driver, 3)
        products.go_to_cart(driver)
        cart.go_to_checkout(driver)
        assert checkout.check_price_in_cart(driver) == total_price

    with allure.step('Деавторизоваться.'):
        products.logout(driver)
