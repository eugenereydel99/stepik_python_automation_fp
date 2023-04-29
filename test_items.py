from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_page_should_contain_add_to_cart_button(browser):
    browser.implicitly_wait(15)
    browser.get(url=link)

    result = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")

    assert result, "'Add to cart' button not found on this page"
