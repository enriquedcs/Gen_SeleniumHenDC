"""
Author: Enrique Decoss
@package: test

Flow for Incorporate a Company
"""

from page.home.login_page import LoginPage
from utilities.teststatus import TestStatus
from page.home.incorp_company_page import IncorCompanyPage
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class IncorporateTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        #self.np = NavigationPage(self.driver)
        self.ic = IncorCompanyPage(self.driver)

    @pytest.mark.run(order=1)
    def test_registeredagent(self):
        self.lp.login("enrique.decoss@wolterskluwer.com", "Today123")
        #result1 = self.lp.verifyTitle()
        #self.ts.mark(result1, "Title Verified")
        self.ic.incorpService("Connecticut", "Test", "Company_Test", "243")
        result2 = self.ic.verifyOrderConfirmation()
        result3 = self.ic.captureOrderNumber()
        self.ts.mark(result2, "Order Created" + str(result3))
        self.ts.markFinal("test_sanity_registeredAgent", result2, "Order was placed correctly Incorporate Services")

