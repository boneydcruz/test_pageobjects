from Locators.test_locators import LoginLocators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginLocators()
    #    self.driver.get("https://www.amazon.com.mx/")

    def search(self):
        self.driver.find_element_by_id(self.locators.searchbox_id).send_keys("iphone")
        self.driver.find_element_by_id(self.locators.submitbtn_id).click()
        self.driver.execute_script("window.scrollTo(0, 6900)")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_css_selector(self.locators.secondpage_css).click()
        self.driver.find_element_by_css_selector(self.locators.secondarticle_css).click()
        self.driver.implicitly_wait(10)
