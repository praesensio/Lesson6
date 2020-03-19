from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators
from pages.locators import BasePageLocators
from pages.locators import LoginPageLocators
import pytest
import time

def test_guest_can_registrated(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)    
    page.open()                      
    page.go_to_login_page()
    page = LoginPage(browser, link)    
    page.register_new_user()
    browser.implicitly_wait(5)
    page.should_be_authorized_user()
