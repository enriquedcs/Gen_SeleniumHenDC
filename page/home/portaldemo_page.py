from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class PortalPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _customer_name = "//tr//th[2]//input[1]"
    _jurisdiction = "//tr//th[3]//input[1]"
    _btn_save = "//div[@class='wk-button-group-right']//button[@type='button'][contains(text(),'Save')]"
    _login_link = "//span[contains(text(),'My Account')]"
    _email_field = "edit-name"
    _password_field = "edit-pass"
    _login_button = "edit-submit"

    def enterEmail(self, email):
        self.waitForElement(locator=self._customer_name, locatorType="xpath", timeout=15)
        self.sendKeys(email, self._customer_name, locatorType="xpath")

    def enterPassword(self, password):
        self.sendKeys(password, self._jurisdiction, locatorType="xpath")

    def clickLoginButton(self):
        self.elementClick(self._btn_save, locatorType="xpath")

    def page(self, email="", password=""):
        time.sleep(4)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(1)


    def verifyTitle(self):
        if "MYDASHBOARD | CT Corporation" in self.getTitle():
            return True
        else:
            return False
