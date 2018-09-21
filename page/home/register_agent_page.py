"""
Author: Enrique Decoss
@package: page

All objects for Register Agent flow
"""

import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
import time

class RegisterAgentPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _cart = "//a[@href='/cart']"
    _delete = "//input[@value='Delete']"
    _myaccount = "//a[@href='/user']"
    _we_do = "//a[contains(text(),'What We Do')]"
    _register_agent = "//a[@title='Registred Agent solutions for businesses of all sizes']"
    _get_started = "//a[@class='button button---secondary'][contains(text(),'Get Started')]"
    _domestic_jurisdiction = "//select[@name='DomesticJurisdiction']"
    _click_state = "//i[@class='selectdropdown dropdown icon']"
    _state_service = "//div[contains(text(),'Alabama')]"
    _next = "edit-checkout"
    _county = "txtBillingCounty"
    _btn_save_contact = "SaveContactInfo"
    _company_name = "//input[@class='form-control txtLegalCompanyName']"
    _btn_legal_address = "btnLegalAddressContinue"
    _btn_continue = "btnContinue"
    _cvv = "txtCVVE"
    _creditcard = "//div[@id='CCExistingPaymentOption']//label[@class='radio-inline']"
    _invoicetab = "tabInvoice"
    _btn_place_order = "edit-placeorder"
    _order_placed = "//h1[@class='section-title M-section-title']"
    _logout = "//span[@id='login-user-fullname']"
    _signout = "//ul[@class='root']//li[2]//a[1]"


    def navigateToCart(self):
        self.waitForElement(locator=self._cart, locatorType="xpath", timeout=15)
        self.elementClick(locator=self._cart, locatorType="xpath")
        time.sleep(2)
        valCart = self.isElementPresent(locator=self._delete, locatorType="xpath")
        if valCart is True:
            time.sleep(2)
            self.elementClick(locator=self._delete, locatorType="xpath")
            self.waitForElement(locator=self._myaccount, locatorType="xpath", timeout=10)
            self.elementClick(locator=self._myaccount, locatorType="xpath")
        else:
            self.elementClick(locator=self._myaccount, locatorType="xpath")

    def navigateTowedo(self):
        self.waitForElement(locator=self._we_do, locatorType="xpath", timeout=10)
        self.elementClick(locator=self._we_do, locatorType="xpath")

    def navigateToregisteredagent(self):
        self.waitForElement(locator=self._register_agent, locatorType="xpath", timeout=5)
        self.elementClick(locator=self._register_agent, locatorType="xpath")

    def navigateTogetstarted(self):
        self.waitForElement(locator=self._get_started, locatorType="xpath", timeout=10)
        self.elementClick(locator=self._get_started, locatorType="xpath")

    def navigateTodomesticjur(self, domestic):
        self.waitForElement(self._domestic_jurisdiction, locatorType="xpath", timeout=30)
        self.sendKeys(domestic, self._domestic_jurisdiction, locatorType="xpath")

    def navigateTodropdown(self):
        self.elementClick(locator=self._click_state, locatorType="xpath")

    def navigateTostateofservice(self):
        self.waitForElement(locator=self._state_service, locatorType="xpath")
        self.elementClick(locator=self._state_service, locatorType="xpath")
        #self.selectType(state, self._state_service, locatorType="xpath")

    def navigateTonext(self):
        self.waitForElement(locator=self._next, locatorType="id")
        self.elementClick(locator=self._next, locatorType="id")

    def navigateTocounty(self, county):
        self.waitForElement(locator=self._county, locatorType="id",  timeout=5)
        #self.clearField(locator=self._county, locatorType="id")
        #self.sendKeys(county, self._county)

    def navigateTosavecontact(self):
        self.waitForElement(locator=self._btn_save_contact, locatorType="id",  timeout=5)
        self.elementClick(locator=self._btn_save_contact, locatorType="id")

    def navigateTocompanyname(self, companyname):
        self.waitForElement(self._company_name, locatorType="xpath",  timeout=5)
        self.sendKeys(companyname, self._company_name, locatorType="xpath")

    def navigateTolegaladdress(self):
        self.waitForElement(locator=self._btn_legal_address, locatorType="id",  timeout=5)
        self.elementClick(locator=self._btn_legal_address, locatorType="id")

    def navigateTocontinue(self):
        self.waitForElement(locator=self._btn_continue, locatorType="id",  timeout=5)
        self.elementClick(locator=self._btn_continue, locatorType="id")

    def navigateTocvv(self, cvv):
        self.waitForElement(locator=self._cvv, locatorType="id",  timeout=5)
        valCred = self.isElementPresent(locator=self._invoicetab, locatorType="id")
        if valCred is True:
            self.elementClick(locator=self._invoicetab, locatorType="id")
        else:
            self.sendKeys(cvv, self._cvv)

    def navigateToplaceorder(self):
        self.waitForElement(locator=self._btn_place_order, locatorType="id",  timeout=5)
        self.elementClick(locator=self._btn_place_order, locatorType="id")

    def registerAgent(self, domestic="", county="", companyname="", cvv=""):
        self.navigateToCart()
        self.navigateTowedo()
        self.navigateToregisteredagent()
        self.navigateTogetstarted()
        self.navigateTodomesticjur(domestic)
        time.sleep(1)
        self.navigateTodropdown()
        self.navigateTostateofservice()
        self.navigateTonext()
        self.navigateTocounty(county)
        self.navigateTosavecontact()
        self.navigateTocompanyname(companyname)
        self.navigateTolegaladdress()
        self.navigateTosavecontact()
        self.navigateTocontinue()
        self.navigateTocvv(cvv)
        self.navigateToplaceorder()
        time.sleep(25)


    def verifyOrderConfirmation(self):
        time.sleep(30)
        self.waitForElement(locator=self._order_placed, locatorType="xpath", timeout=35)
        result = self.isElementPresent(locator=self._order_placed,
                                       locatorType="xpath")
        return result

    def captureOrderNumber(self):
        time.sleep(1)
        ordertext = self.getText(locator=self._order_placed, locatorType="xpath")

        return ordertext

    def logoutMyCT(self):
        time.sleep(1)
        self.waitForElement(locator=self._logout, locatorType="xpath", timeout=7)
        self.elementClick(locator=self._logout, locatorType="xpath")
        time.sleep(1)
        self.elementClick(locator=self._signout, locatorType="xpath")