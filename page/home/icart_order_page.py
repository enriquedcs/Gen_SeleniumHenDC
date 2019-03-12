import utilities.custom_logger as cl
import logging
from base.selenium_driver import SeleniumDriver
import time

class IcartOrderPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _dashboard = "//a[@pathname='/QA/CT.CTCorp.OrderSearch/Dashboard/DashboardTab2.aspx']/span[@innertext='Dashboard']"
    _icart_link = "//a[@pathname='/QA/CT.CTCorp.OrderSearch/Dashboard/CreateOrder.aspx']/span[@innertext='iCart']"
    _start_new_order = "btnStartNewOrder"
    #_chk_existing_cust = "rdoSearchExistingCustomer"
    #_existing_name = "txtSearchFirstName"
    #_existing_lastname = "txtSearchLastName"
    #_btn_exiting = "btnSearchCustomer"
    #_search_order = "btnSearchOrderQuote"
    _customer_name = "//input[@id='txtCustomerName']"
    _phone_int = "//input[@id='txtCustomerPhoneNumber']"
    _customer_email = "//input[@id='txtCustomerEmail']"
    _mail_address = "//div[@id='divCSTForm']/div[@class='add-order-placer-fields form']/table/tbody/tr[3]/td[1]/input[@type='text']"
    _city = "//input[@id='txtCustomerCity']"
    _state = "//select[@id='drpCustomerState']"
    _zip_code = "//input[@id='txtCustomerZipCode']"
    _btn_save = "btnSaveCSTDetails"
    _name_placer = "txtOrderPlacerFirstName_0"
    _last_placer = "txtOrderPlacerLastName_0"
    _email_placer = "txtOrderPlacerEmail_0"
    _county = "txtOrderPlacerCounty_0"
    _btn_save2 = "btnSaveCDetails_0"
    _target_name = "txtTargetName_0"
    _business_structure = "drpTargetEntityType_0"
    _state_target = "drpTargetState_0"
    _btn_targetsave = "btnSaveTarget_0"
    #_existing_target = "rdoNewsearchCSTTarget"
    #_entity_name = "txtExistTargetName"
    #_click_search = "btnNewCSTSearchExitingTarget"
    _btn_continue = "btnContinutToAddProduct"
    _btn_order_pref = "btnSaveOrderPreference"
    _product_list = "productList"
    _btn_next = "//button[contains(text(),'Next >>')]"
    #_state_check = ""
    _btn_cart = "btnAddToCart"
    _btn_save_order = "btnSaveOrderServiceContinue"
    _sf_opportunity_id = "txtSFOpportunityId"
    _sf_account_id = "txtSFAccountId"
    _btn_pay_now = "btnPayNow"
    _chk_invoice = "rdoInvoiceMethod"
    _place_order = "edit-placeorder"
    _order_placed = "lblCartOrderId"
    _placeneworder = "btnPlaceNewOrder"


    def navigateToDashboard(self):
        self.elementClick(locator=self._dashboard, locatorType="xpath")

    def navigateToIcart(self):
        self.elementClick(locator=self._icart_link, locatorType="xpath")

    def navigateToOrder(self):
        self.elementClick(locator=self._start_new_order, locatorType="id")

    def navigateToCustomer(self, customer="HCLAutomation"):
        self.waitForElement(locator=self._customer_name, locatorType="xpath", timeout=10)
        self.elementClick(locator=self._customer_name, locatorType="xpath")
        self.sendKeys(customer, locator=self._customer_name, locatorType="xpath")

    def navigateToPhone(self, phone="8587658934"):
        self.sendKeys(phone, locator=self._phone_int, locatorType="xpath")

    def navigateToCustomerEmail(self, email="enrique.decoss@wolterskluwer.com"):
        self.sendKeys(email, self._customer_email, locatorType="xpath")

    def navigateToMail(self, mail="123 Test"):
        self.sendKeys(mail, locator=self._mail_address, locatorType="xpath")

    def navigateToCity(self, city="New York"):
        self.sendKeys(city, locator=self._city, locatorType="xpath")

    def navigateToState(self, state="AL"):
        self.selectType(state, locator=self._state, locatorType="xpath")

    def navigateToZipcode(self, zipcode="78978"):
        self.sendKeys(zipcode, locator=self._zip_code, locatorType="xpath")

    def navigateToSave(self):
        self.elementClick(locator=self._btn_save, locatorType="id")

    def navigateToNamePlacer(self, nameP="Enrique"):
        self.waitForElement(locator=self._name_placer, locatorType="id", timeout=2)
        self.sendKeys(nameP, self._name_placer)

    def navigateToLastNamePlacer(self, nameL="Dc"):
        self.sendKeys(nameL, self._last_placer)

    def navigateToEmailPlacer(self, email="enrique.decoss@wolterskluwer.com"):
        self.sendKeys(email, self._email_placer)

    def navigateToCounty(self, county="Manhattan"):
        self.sendKeys(county, self._county)

    def navigateToSave1(self):
        self.elementClick(locator=self._btn_save2, locatorType="id")

    def navigateToTargetName(self, targetN = "HCLAutomation"):
        self.waitForElement(self._target_name, locatorType="id", timeout=2)
        self.sendKeys(targetN, self._target_name, locatorType="id")
    # 112 - Corporation 113 - Limited Liability Company 114 - Non - Profit
    def navigateToBusiness(self, corporationT = "112"):
        self.selectType(corporationT, locator=self._business_structure, locatorType="id")

    def navigateToStateTarget(self, stateT = "60"):
        self.selectType(stateT, locator=self._state_target, locatorType="id")

    def navigateToBtnSaveTarget(self):
        self.elementClick(locator=self._btn_targetsave, locatorType="id")

    def navigateTocontinueAddProduct(self):
        self.waitForElement(locator=self._btn_continue, locatorType="id")
        self.elementClick(locator=self._btn_continue, locatorType="id")

    def navigateToBtnOrderPreference(self):
        self.waitForElement(locator=self._btn_order_pref, locatorType="id")
        self.elementClick(locator=self._btn_order_pref, locatorType="id")

    def navigateToProduct(self, selProduct = "153"):
        self.waitForElement(locator=self._product_list, locatorType="id")
        self.selectType(selProduct, locator=self._product_list, locatorType="id")

    def navigateToNextP(self):
        self.waitForElement(locator=self._btn_next, locatorType="xpath")
        self.elementClick(locator=self._btn_next, locatorType="xpath")

    def navigateToStateService(self, statev = "//input[@id='chkBoxState_6']"):
        self.waitForElement(locator=statev, locatorType="xpath", timeout=10)
        self.elementClick(locator=statev, locatorType="xpath")

    def navigateToBtnAddCart(self):
        self.waitForElement(locator=self._btn_cart, locatorType="id", timeout=3)
        self.elementClick(locator=self._btn_cart, locatorType="id")
        time.sleep(3)

    def navigateToContinue(self):
        self.waitForElement(locator=self._btn_save_order, locatorType="id", timeout=30)
        self.elementClick(locator=self._btn_save_order, locatorType="id")

    def navigateToSFOpportunity(self, sfopp = "TestHCL"):
        self.waitForElement(self._sf_opportunity_id, locatorType="id")
        self.sendKeys(sfopp, self._sf_opportunity_id, locatorType="id")

    def navigateToSFAccount(self, sfacc = "155621"):
        self.sendKeys(sfacc, self._sf_account_id, locatorType="id")

    def navigateToInvoice(self):
        self.waitForElement(locator=self._chk_invoice, locatorType="id", timeout=26)
        self.elementClick(locator=self._chk_invoice, locatorType="id")
        time.sleep(5)
        self.waitForElement(locator=self._chk_invoice, locatorType="id", timeout=10)
        self.elementClick(locator=self._chk_invoice, locatorType="id")

    def navigateToPayNow(self):
        self.waitForElement(locator=self._btn_pay_now, locatorType="id")
        self.elementClick(locator=self._btn_pay_now, locatorType="id")
        time.sleep(5)

    def navigateToPlaceOrder(self):
        self.elementClick(locator=self._place_order, locatorType="id")

    def icartorder(self, customer, phone, email, targetN, selProduct, statev):
        time.sleep(1)
        #self.navigateToDashboard()
        #self.navigateToIcart()
        #self.navigateToOrder()
        self.navigateToCustomer(customer)
        self.navigateToPhone(phone)
        self.navigateToCustomerEmail(email)
        self.navigateToMail()
        self.navigateToCity()
        self.navigateToState()
        self.navigateToZipcode()
        self.navigateToSave()
        self.navigateToNamePlacer()
        self.navigateToLastNamePlacer()
        self.navigateToEmailPlacer()
        self.navigateToCounty()
        self.navigateToSave1()
        self.navigateToTargetName(targetN)
        self.navigateToBusiness()
        self.navigateToStateTarget()
        self.navigateToBtnSaveTarget()
        self.navigateTocontinueAddProduct()
        self.navigateToBtnOrderPreference()
        self.navigateToProduct(selProduct)
        self.navigateToNextP()
        self.navigateToStateService(statev)
        self.navigateToBtnAddCart()
        self.navigateToContinue()
        self.navigateToSFOpportunity()
        self.navigateToSFAccount()
        self.navigateToPayNow()
        self.navigateToInvoice()
        self.navigateToPlaceOrder()
        time.sleep(4)


    def verifyOrderConfirmation(self):
        time.sleep(2)
        self.waitForElement(locator=self._order_placed, locatorType="id", timeout=10)
        result = self.isElementPresent(locator=self._order_placed,
                                       locatorType="id")
        return result

    def captureOrderNumber(self):
        time.sleep(1)
        ordertext = self.getText(locator=self._order_placed, locatorType="id")

        return ordertext

    def startNewOrder(self):
        self.elementClick(locator=self._placeneworder, locatorType="id")
        time.sleep(2)
