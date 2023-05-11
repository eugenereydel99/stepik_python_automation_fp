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

    def should_be_authorized_user(self):
        assert self.is_element_present(
            *BasePageLocators.USER_ICON
        ), "User icon is not presented, probably unauthorised user"

    def go_to_basket_page(self):
        basket_btn = self.browser.find_element(
            *BasePageLocators.BASKET_BUTTON
        )
        basket_btn.click()

    def go_to_login_page(self):
        login_link = self.browser.find_element(
            *BasePageLocators.LOGIN_LINK
        )
        login_link.click()

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
