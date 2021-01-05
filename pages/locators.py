from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ByPageLocators():
    BUTTON_LINK = (By.CSS_SELECTOR,"button.btn-add-to-basket")
    ADD_TO_CART=(By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_FORM = (By.CSS_SELECTOR, '.product_main h1')
    PRICE_FORM = (By.CSS_SELECTOR, '.product_main .price_color')
    ALERT_LIST = (By.CSS_SELECTOR, '.alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
class BasketPageLocators():
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BUTTON_ITEM = (By.CSS_SELECTOR, "span.btn-group")