from .base_page import BasePage


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert True

    
    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*MainPageLocators. REGISTER_FORM), "Register form is not presented "
        assert True
    def register_new_user(self, email, password):
        # реализуйте метод регистрации нового пользователя
        wait = Webdriver(self.driver, 5)
        wait.until(EC.presence_of_element_located(*LoginPageLocators.REGISTER_FORM))
        self.driver.find_element((*LoginPageLocators.LOGIN_FORM).send_keys(email))