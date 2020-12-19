from pages.product_page import ByPage
import pytest
import time
import math

product_link_by = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{product_link_by}/?promo=offer{number}" for number in range(10)]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ByPage(browser, link)
    page.open()
    page.go_to_button_page()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.compare_name()
    page.compare_price()

