from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    PRODUCTS_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "form.basket_summary")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators:
    # Группа локаторов для формы 'Войти'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[name=\"login-username\"]")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[name=\"login-password\"]")
    LOGIN_ENTER_BUTTON = (By.CSS_SELECTOR, "button[name=\"login_submit\"]")

    # Группа локаторов для формы 'Зарегистрироваться'
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input[name=\"registration-email\"]")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input[name=\"registration-password1\"]")
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input[name=\"registration-password2\"]")
    REGISTER_ENTER_BUTTON = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-safe .alertinner strong")
    PRODUCT_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
