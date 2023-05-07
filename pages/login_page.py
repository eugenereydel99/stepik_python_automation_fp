import time

from pages.locators import LoginPageLocators
from .base_page import BasePage


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

    def __fill_credentials_for_register(self, email: str, password: str):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL) \
            .send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD) \
            .send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT) \
            .send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_ENTER_BUTTON) \
            .click()

    def register_new_user(self, email: str, password: str):
        self.should_be_login_url()
        self.__fill_credentials_for_register(email, password)
