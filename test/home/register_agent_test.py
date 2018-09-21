"""
Author: Enrique Decoss
@package: test

Flow for Register Agent Test
"""

from page.home.login_page import LoginPage
from page.home.navigation_page import NavigationPage
from utilities.teststatus import TestStatus
from page.home.register_agent_page import RegisterAgentPage
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        #self.np = NavigationPage(self.driver)
        self.re = RegisterAgentPage(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/enriquealejandro.d/PycharmProjects/WKSelenium/testdata.csv"))
    @unpack
    def test_registeredagent(self, user, password, domesticCSV, countyCSV, companyCSV, ccvCSV):
        self.lp.login(user, password)
        #result1 = self.lp.verifyTitle()
        #self.ts.mark(result1, "Title Verified")
        self.re.registerAgent(domestic=domesticCSV, county=countyCSV, companyname=companyCSV, cvv=ccvCSV)
        result2 = self.re.verifyOrderConfirmation()
        result3 = self.re.captureOrderNumber()
        self.re.logoutMyCT()
        self.ts.mark(result2, "Order Created" + str(result3))
        self.ts.markFinal("test_sanity_registeredAgent", result2, "Order was placed correctly")