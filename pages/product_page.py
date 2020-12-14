from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ByPageLocators
from .login_page import LoginPage

class ByPage(BasePage):
    def go_to_button_page(self):
        button = self.browser.find_element(*ByPageLocators.BUTTON_LINK)
        button.click()
        #alert = self.browser.switch_to.alert
        #alert.accept()