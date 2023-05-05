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
            *ProductPageLocators.PRODUCT_NAME_ALERT
        ).text

    def get_product_price(self) -> str:
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

    def get_product_price_from_alert(self) -> str:
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_ALERT
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

    def should_be_add_to_cart(self):
        add_to_cart_btn = self.browser.find_element(
            *ProductPageLocators.ADD_TO_CART_BUTTON
        )
        add_to_cart_btn.click()
        self.solve_quiz_and_get_code()
        self.should_be_match_attributes()
