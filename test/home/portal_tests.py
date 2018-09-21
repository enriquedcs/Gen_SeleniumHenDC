from page.home.portaldemo_page import PortalPage
from utilities.teststatus import TestStatus
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.pp = PortalPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_validLogin(self):
        self.pp.page("Testing", "Today")
        result1 = self.lp.verifyTitle()
        self.ts.mark(result1, "Title Verified")
        self.ts.markFinal("test_validL", result1, "Successful")

