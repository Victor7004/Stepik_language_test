from pages.product_page import ByPage
from pages.login_page import LoginPage
from pages.locators import ByPageLocators
from pages.basket_page import BasketPage
from pages.locators import BasketPageLocators
from pages.base_page import BasePage
import faker
import pytest
import time
import math


#product_link_by = "#http://"
#links = [f"{product_link_by}/?promo=offer{number}" for number in range(10)]

@pytest.mark.need_review
#@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = ByPage(browser, link)
    page.open()
    page.go_to_button_page()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.compare_name()
    page.compare_price() 

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ByPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ByPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page.should_be_in_element_present()
    page.is_not_basket_empty()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ByPage(browser, link)
    page.open()
    page.go_to_login_page() 


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ByPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ByPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_user_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
    page = BasketPage(browser, link)
    page.open()
    page.is_not_basket_empty()


class TestUserAddToBasketFromProductPage(BasePage):

    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser):
        login_link= "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        f = faker.Faker()
        email = f.email()
        password = str(time.time())
        page.register_new_user(email=email,password=password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
        page = ByPage(browser, link)
        page.open()
        page.user_can_add_product_to_basket()


    def test_user_cant_see_success_message(browser)
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer1"
        page = ByPage(browser, link)
        page.open()
        page.user_cant_see_success_message() 

   
 