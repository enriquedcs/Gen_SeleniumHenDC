from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time

class LoginPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _cookie_check = "epdagree"
    _cookie_btn = "explicitsubmit"
    _cookie_btn2 = "popup-buttons"
    _login_link = "//span[contains(text(),'My Account')]"
    _email_field = "edit-name"
    _password_field = "edit-pass"
    _login_button = "edit-submit"

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="xpath")

    def waitLoginLink(self):
        self.waitForElement(self._login_link, locatorType="xpath")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field)

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field)

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="id")

    def clickCookiechk(self):
        self.waitForElement(locator=self._cookie_check, locatorType="id", timeout=10)
        time.sleep(1)
        valCookie = self.isElementPresent(locator=self._cookie_check, locatorType="id")
        if valCookie is True:
            self.elementClick(self._cookie_check, locatorType="id")
            self.elementClick(self._cookie_btn, locatorType="id")
        else:
            self.elementClick(self._cookie_btn2, locatorType="id")

    def login(self, email="", password=""):
        self.clickCookiechk()
        self.waitLoginLink()
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(3)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//span[@id='login-user-fullname']",
                                       locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//div[@class='messages error']",
                                       locatorType="xpath")
        return result

    def verifyTitle(self):
        if "MYDASHBOARD | CT Corporation" in self.getTitle():
            return True
        else:
            return False
