import math

import allure
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException

from pages.locators import BasePageLocators


# noinspection Assert
class BasePage:
    def __init__(self, browser, url) -> None:
        self.browser = browser
        self.url = url

    @allure.step(title=f"Открытие тестовой страницы в браузере")
    def open(self):
        self.browser.get(url=self.url)

    def is_element_present(self, locator, value):
        try:
            self.browser.find_element(by=locator, value=value)
        except NoSuchElementException:
            return False
        return True

    @allure.step(title="Проверка на то, что пользователь авторизован")
    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON
        ), "User icon is not presented, probably unauthorised user"

    @allure.step(title="Переход на страницу корзины")
    def go_to_basket_page(self):
        with allure.step(title="Поиск кнопки для перехода"):
            basket_btn = self.browser.find_element(
                *BasePageLocators.BASKET_BUTTON
            )
        with allure.step(title="Нажатие на кнопку для перехода"):
            basket_btn.click()

    @allure.step(title="Переход на страницу авторизации")
    def go_to_login_page(self):
        with allure.step(title="Поиск ссылки для перехода"):
            login_link = self.browser.find_element(
                *BasePageLocators.LOGIN_LINK
            )
        with allure.step(title="Нажатие на ссылку перехода"):
            login_link.click()

    @allure.step(title="Проверка наличия ссылки на авторизацию пользователя")
    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK
        ), "Login link is not presented"

    @allure.step(title="Рассчитываем значение из алерта и отправляем на сервер")
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
