import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver

class NavigationPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    _my_account = "MYDASHBOARD"
    _my_orders = "MYORDERS"
    _my_companies = "MYCOMPANIES"
    _my_events = "MYEVENTS"
    _my_invoices = "MYBILLING"
    _account_settings = "MYSETTINGS"
    _order_data = "btndocumentUri"


    def navigateToMyAccount(self):
        self.waitForElement(locator=self._my_account, locatorType="id")
        self.elementClick(locator=self._my_account, locatorType="id")

    def navigateToMyOrders(self):
        self.waitForElement(locator=self._my_orders, locatorType="id")
        self.elementClick(locator=self._my_orders, locatorType="id")

    def navigateToMyCompanies(self):
        self.waitForElement(locator=self._my_companies, locatorType="id", timeout=30)
        self.elementClick(locator=self._my_companies, locatorType="id")

    def navigateToMyEvents(self):
        self.waitForElement(locator=self._my_events, locatorType="id")
        self.elementClick(locator=self._my_events, locatorType="id")

    def navigateToMyInvoices(self):
        self.waitForElement(locator=self._my_invoices, locatorType="id")
        self.elementClick(locator=self._my_invoices, locatorType="id")

    def navigateToAccountSettings(self):
        self.waitForElement(locator=self._account_settings, locatorType="id")
        self.elementClick(locator=self._account_settings, locatorType="id")

    def verifymyaccoutSuccessful(self):
        self.waitForElement(locator=self._order_data, locatorType="id")
        result = self.isElementPresent("btndocumentUri",
                                       locatorType="id")
        return result

    def verifymyordersSuccessful(self):
        result = self.isElementPresent("txtSearchKey",
                                       locatorType="id")
        return result

    def verifymyeventsSuccessful(self):
        result = self.isElementPresent("txtSearchValue",
                                       locatorType="id")
        return result

    def verifymyinvoicesSuccessful(self):
        result = self.isElementPresent("txtSearchKey",
                                       locatorType="id")
        return result

    def verifyaccountSuccessful(self):
        result = self.isElementPresent("profileinformation",
                                       locatorType="id")
        return result
