import time

import allure

from pages.locators import LoginPageLocators
from .base_page import BasePage


# noinspection Assert
class LoginPage(BasePage):

    @allure.step(title="Проверка нахождения пользователя на странице авторизации")
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    @allure.step(title="Проверка вхождения строки 'login' в название url")
    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    @allure.step(title="Проверка наличия формы авторизации")
    def should_be_login_form(self):
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), "Login form is not presented"

    @allure.step(title="Проверка наличия формы регистрации")
    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), "Register form is not presented"

    @allure.step(title="Заполнение формы регистрации пользователя")
    def __fill_credentials_for_register(self, email: str, password: str):
        self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL) \
            .send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD) \
            .send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_REPEAT) \
            .send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTER_ENTER_BUTTON) \
            .click()

    @allure.step(title="Регистрация пользователя")
    def register_new_user(self, email: str, password: str):
        self.should_be_login_url()
        self.__fill_credentials_for_register(email, password)
