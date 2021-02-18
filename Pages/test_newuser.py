from selenium.common.exceptions import NoSuchElementException

from Locators.test_locators import LoginLocators


class NewUser:

    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginLocators()
    #    self.driver.get("https://www.amazon.com.mx/")

    def newuser(self):
        try:
            self.driver.find_element_by_id(self.locators.accountdropdown_id).click()
            self.driver.find_element_by_id(self.locators.createacc_id).click()
            self.driver.find_element_by_id(self.locators.name_id).send_keys("hellouser")
            self.driver.find_element_by_id(self.locators.email_id).send_keys("hellouser@gmail.com")
            self.driver.find_element_by_id(self.locators.password_id).send_keys("qwerty")
            self.driver.find_element_by_id(self.locators.repassword_id).send_keys("qwertyu")
            self.driver.find_element_by_id(self.locators.newusercreatbtn_id).click()
            self.driver.find_element_by_xpath('//*[@id="auth-password-mismatch-alert"]/div/div')
            print("Element exist")
        except NoSuchElementException:
            print("Element does not exist")
