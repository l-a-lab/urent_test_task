from pages.login_page import LoginPage


def go_to_login_page(driver):
    login_page = LoginPage(driver)


def check_username_field(driver):
    login_page = LoginPage(driver)
    try:
        login_page.find_username()
    except Exception:
        print("Element with id user-name not found")
        raise Exception("Element with id user-name not found")


def login_user(driver, username, password):
    login_page = LoginPage(driver)
    login_page.success_login(username, password)
