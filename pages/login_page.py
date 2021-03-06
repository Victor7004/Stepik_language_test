from .base_page import BasePage
from .locators import LoginPageLocators
from selenium import webdriver

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, "Cant find word login in url"
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), "Login form is not presented "
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators. REGISTER_FORM), "Register form is not presented "
        assert True
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        password_field.send_keys(password)