from pages.product_page import ByPage
import time



def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ByPage(browser, link)
    page.open()
    page.go_to_button_page()
    page.solve_quiz_and_get_code()
    time.sleep(10)
    page.compare_name()
    page.compare_price()
