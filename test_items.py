import pytest
from selenium import webdriver
import time

#@pytest.fixture(scope="function")
#def browser():
    #print("\nstart browser for test..")
    #browser = webdriver.Chrome()
    #yield browser
    #print("\nquit browser..")
    #browser.quit()

#@pytest.mark.parametrize('language', ["es", "fr"])
def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_class_name (".btn-a-dd-to-basket").text
    button.click() 
    assert "Ajouter au panier" in button
