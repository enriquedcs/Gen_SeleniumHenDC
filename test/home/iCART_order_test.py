from page.home.icart_order_page import IcartOrderPage
from utilities.teststatus import TestStatus
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class iCARTTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.ts = TestStatus(self.driver)
        self.ip = IcartOrderPage(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/enriquealejandro.d/PycharmProjects/WKSelenium/testdataicart.csv"))
    @unpack
    def test_icart(self, customerCSV, phoneCSV, emailCSV, targetNCSV, ProductCSV, statevarCSV):
        self.ip.icartorder(customer=customerCSV, phone=phoneCSV, email=emailCSV, targetN=targetNCSV, selProduct=ProductCSV, statev=statevarCSV)
        result2 = self.ip.verifyOrderConfirmation()
        result3 = self.ip.captureOrderNumber()
        self.ip.startNewOrder()
        self.ts.mark(result2, "Order Created: " + str(result3))
        self.ts.markFinal("test_sanity_iCART ", result2, "Order was placed correctly")