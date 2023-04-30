from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    # Группа локаторов для формы 'Войти'
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_USERNAME = (By.CSS_SELECTOR, "input[name=\"login-username\"]")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[name=\"login-password\"]")
    LOGIN_ENTER_BUTTON = (By.CSS_SELECTOR, "button[name=\"login_submit\"]")

    # Группа локаторов для формы 'Зарегистрироваться'
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_USERNAME = (By.CSS_SELECTOR, "input[name=\"registration-email\"]")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input[name=\"registration-password1\"]")
    REGISTER_PASSWORD_REPEAT = (By.CSS_SELECTOR, "input[name=\"registration-password2\"]")
    REGISTER_ENTER_BUTTON = (By.CSS_SELECTOR, "button[name=\"registration_submit\"]")