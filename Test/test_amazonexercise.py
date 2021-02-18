import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from Pages.test_testcase import LoginPage
from Pages.test_addcart import AddCart
from Pages.test_newuser import NewUser


@pytest.fixture()
def test_setup():
    global driver
    print("Initiating Firefox driver")
    driver = webdriver.Firefox()
    print("-----------------------------------------")
    print("Test is started")
    driver.maximize_window()
    driver.get("https://www.amazon.com.mx/")
    yield
    print("-----------------------------------------")
    print("Tests is finished")
    driver.close()


def test_amazonexercise(test_setup):
    loginpage = LoginPage(driver)
    loginpage.search()


def test_amazonexercise1(test_setup):
    addcart = AddCart(driver)
    addcart.addcart()


def test_amazonexercise2(test_setup):
    newuser = NewUser(driver)
    newuser.newuser()
    try:
        driver.find_element_by_xpath('//*[@id="auth-password-mismatch-alert"]/div/div')
        print("Element exist")
    except NoSuchElementException:
        print("Element does not exist")
