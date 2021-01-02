#3from .locators import BasePageLocator
from .locators import BasketPageLocators
from .base_page import BasePage
#from selenium.webdriver.common.by import B
#from .login_page import LoginPage
import pytest

class BasketPage():

    #def go_to_basket_page(self):
        #button = self.browser.find_element(*BasketPageLocators.BUTTON_ITEM)
        #button.click()

    def should_be_in_element_present(self):
        #assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
        assert 'empty' in self.browser.find_element(By.XPATH, "//p[contains(text(), 'empty')]"), " Basket not empty"  
    def is_not_basket_empty(self):
         assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty"   