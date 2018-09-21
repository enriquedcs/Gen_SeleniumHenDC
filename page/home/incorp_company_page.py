"""
Author: Enrique Decoss
@package: page

All objects for Incorporate Company flow
"""

import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
import time

class IncorCompanyPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _we_do = "//a[contains(text(),'What We Do')]"
    _incorp_services = "//a[@title='Incorporation Services']"
    _company_LLC = "//a[contains(text(),'Limited Liability Company')]"
    _company_S = "//a[contains(text(),'S Corporation')]"
    _company_C = "//a[@class='button button---secondary v-margin-mini'][contains(text(),'C Corporation')]"
    _get_companyLLC = "//span[contains(text(),'Form your LLC online')]"

    _state_service = "//select[@title='State of Service']"
    _next = "edit-checkout"
    _btn_next_state = "BtnNextRelated"
    _company_name1 = "txtFirstNameChoice"
    _company_name1_suffix = "txtEntityOption1"
    _company_name2 = "txtSecondNameChoice"
    _company_name2_suffix = "txtEntityOption2"
    _street_name = "txtCompanyAddress1"
    _zip_code = "txtZipCode"
    _city = "txtCompanyCity"
    _state = "drpState"
    _phone = "txtCompanyPhoneNumber"
    _btn_continue = "btnContinue"
    _county = "txtBillingCounty"
    _co_manage_Name = "txtMemberFirstName_0"
    _co_manage_LastName = "txtMemberLastName_0"
    _btn_cont_company = "btnContinueCompanyMgmt"
    _saveContact = "SaveContactInfo"
    _cvv = "txtCVVE"
    _btn_place_order = "edit-placeorder"
    _order_placed = "//h1[@class='section-title M-section-title']"



    def navigateTowedo(self):
        self.waitForElement(locator=self._we_do, locatorType="xpath", timeout=20)
        self.elementClick(locator=self._we_do, locatorType="xpath")

    def navigateToIncorpcompany(self):
        self.waitForElement(locator=self._incorp_services, locatorType="xpath")
        self.elementClick(locator=self._incorp_services, locatorType="xpath")

    def navigateTogetstarted(self, locatorType ="LLC"):
        if locatorType == "C":
            self.waitForElement(locator=self._company_C, locatorType="xpath")
            self.elementClick(locator=self._company_C, locatorType="xpath")
        elif locatorType == "S":
            self.waitForElement(locator=self._company_S, locatorType="xpath")
            self.elementClick(locator=self._company_S, locatorType="xpath")
        else:
            self.waitForElement(locator=self._company_LLC, locatorType="xpath")
            self.elementClick(locator=self._company_LLC, locatorType="xpath")

    def navigateToLLC(self):
        self.waitForElement(self._get_companyLLC, locatorType="xpath")
        self.elementClick(self._get_companyLLC, locatorType="xpath")

    def navigateTostateofservice(self, state = "60"):
        self.waitForElement(locator=self._state_service, locatorType="xpath")
        #self.elementClick(locator=self._state_service, locatorType="xpath")
        self.selectType(state, self._state_service, locatorType="xpath")

    def navigateTonext(self):
        self.waitForElement(locator=self._next, locatorType="id")
        self.elementClick(locator=self._next, locatorType="id")


    def navigateTonextState(self):
        self.waitForElement(locator=self._btn_next_state, locatorType="id")
        self.elementClick(locator=self._btn_next_state, locatorType="id")

    def navigateTocompanyname1(self, companyname):
        self.waitForElement(self._company_name1, locatorType="id")
        self.sendKeys(companyname, self._company_name1, locatorType="id")

    def navigateTocompanyname1suffix(self, companysuffix="LLC"):
        self.sendKeys(companysuffix, self._company_name1_suffix, locatorType="id")

    def navigateTocompanyname2(self, companyname):
        self.sendKeys(companyname, self._company_name2, locatorType="id")

    def navigateTocompanyname2suffix(self, companysuffix="LLC"):
        self.sendKeys(companysuffix, self._company_name2_suffix, locatorType="id")

    def navigateTocontinue(self):
        self.waitForElement(locator=self._btn_continue, locatorType="id")
        self.elementClick(locator=self._btn_continue, locatorType="id")

    def navigateTocounty(self, county):
        self.waitForElement(locator=self._county, locatorType="id")
        self.clearField(locator=self._county, locatorType="id")
        self.sendKeys(county, self._county)

    def navigateTocontCompany(self):
        self.waitForElement(locator=self._btn_cont_company, locatorType="id")
        self.elementClick(locator=self._btn_cont_company, locatorType="id")

    def navigateToSaveCnt(self, cvv):
        self.waitForElement(locator=self._saveContact, locatorType="id")
        self.sendKeys(cvv, self._cvv)

    def navigateTocvv(self, cvv):
        self.waitForElement(locator=self._cvv, locatorType="id")
        self.sendKeys(cvv, self._cvv)

    def navigateToplaceorder(self):
        self.elementClick(locator=self._btn_place_order, locatorType="id")

    def incorpService(self, domestic="", county="", companyname="", cvv=""):
        self.navigateTowedo()
        self.navigateToIncorpcompany()
        self.navigateTogetstarted()
        time.sleep(1)
        self.navigateToLLC()
        self.navigateTostateofservice()
        self.navigateTonext()
        self.navigateTonextState()
        self.navigateTocompanyname1(companyname)
        self.navigateTocompanyname1suffix()
        self.navigateTocompanyname2(companyname)
        self.navigateTocompanyname2suffix()
        self.navigateTocontinue()
        time.sleep(1)


    def verifyOrderConfirmation(self):
        time.sleep(3)
        self.waitForElement(locator=self._order_placed, locatorType="xpath", timeout=3)
        result = self.isElementPresent(locator=self._order_placed,
                                       locatorType="xpath")
        return result

    def captureOrderNumber(self):
        time.sleep(1)
        ordertext = self.getText(locator=self._order_placed, locatorType="xpath")

        return ordertext