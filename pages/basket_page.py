from .locators import BasketPageLocators
from .base_page import BasePage
from selenium.webdriver.common.by import By
import pytest

class BasketPage(BasePage):

    def go_to_basket_page(self):
        button = self.browser.find_element(*BasketPageLocators.BUTTON_ITEM)
        button.click()


    def is_not_basket_empty(self):
         assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty"  