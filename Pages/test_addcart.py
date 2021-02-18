from Locators.test_locators import LoginLocators


class AddCart:

    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginLocators()
    #    self.driver.get("https://www.amazon.com.mx/")

    def addcart(self):
        self.driver.find_element_by_id(self.locators.searchbox_id).send_keys("iwatch")
        self.driver.find_element_by_id(self.locators.submitbtn_id).click()
        self.driver.find_element_by_css_selector(self.locators.firstarticle_css).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id(self.locators.addtocartbtn_id).click()
        self.driver.implicitly_wait(10)