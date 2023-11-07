from selenium.webdriver.common.by import By


class MainPageLocators():


class LoginPageLocators():
    LOGINFORM_LINK = (By.CSS_SELECTOR, "#login_form")
    REGISTERFORM_LINK = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators(object):
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_ABOUT_ADDING = (
        By.XPATH,
        "(//div[@id='messages']//div[contains(@class, 'alert-success')]//div[@class='alertinner ']//strong)[1]")

    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    MESSAGE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")