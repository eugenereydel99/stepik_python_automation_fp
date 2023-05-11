import allure
import selenium.webdriver.support.expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import BasketPageLocators


# noinspection Assert
class BasketPage(BasePage):

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    @allure.step(title="Проверка отсутствия товаров в корзине")
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCTS_IN_BASKET_MESSAGE
        ), "There are products in the basket, but should not be"

    @allure.step(title="Проверка наличия текста об отсутствии товаров в корзине")
    def should_be_text_about_basket_is_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY_MESSAGE
        ), "Not found text about basket is empty"
