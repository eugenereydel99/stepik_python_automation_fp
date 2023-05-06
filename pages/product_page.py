import selenium.webdriver.support.expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


# noinspection Assert
class ProductPage(BasePage):

    def get_product_name(self) -> str:
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

    def get_product_name_from_alert(self) -> str:
        return self.browser.find_element(
            *ProductPageLocators.SUCCESS_MESSAGE
        ).text

    def get_product_price(self) -> str:
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

    def get_product_price_from_alert(self) -> str:
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_MESSAGE
        ).text

    def is_product_name_match(self):
        assert self.get_product_name() \
               == self.get_product_name_from_alert() \
            , "Product name doesn't match"

    def is_product_price_match(self):
        assert self.get_product_price() \
               == self.get_product_price_from_alert() \
            , "Product price doesn't match"

    def should_be_match_attributes(self):
        self.is_product_name_match()
        self.is_product_price_match()

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return True
        return False

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False
        return True

    def should_be_element_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message should have disappeared, but it didn't"

    def should_be_add_to_cart(self):
        add_to_cart_btn = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BUTTON
        )
        add_to_cart_btn.click()
