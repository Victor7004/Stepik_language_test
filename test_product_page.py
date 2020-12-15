from pages.product_page import ByPage
from pages.login_page import LoginPage
import time 
import math


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ByPage(browser, link)
    page.open()
    page.go_to_button_page()
    page.solve_quiz_and_get_code()
    time.sleep(3) 
    # выполнить проверку добавилась ли книга 
    # выполнить проверку правильности цены