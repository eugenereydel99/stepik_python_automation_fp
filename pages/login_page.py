from .base_page import BasePage
from pages.locators import LoginPageLocators


# noinspection Assert
class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # проверка корректности запущенной страницы логина
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        # проверка наличия формы авторизации
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    def should_be_register_form(self):
        # проверка наличия формы регистрации
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"
