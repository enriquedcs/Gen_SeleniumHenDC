"""
Author: Enrique DeCoss
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
import os

class WebDriverFactory():

    def __init__(self, browser, env):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
        self.env = env
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """

        if self.env == "qa":
            #Set ctcorp QA
            baseURL = "http://qa1.smbstaging.com/"
        elif self.env == "prep":
            baseURL = "https://preprod.ct.wolterskluwer.com/"
        elif self.env == "prod":
            baseURL = "https://ct-portal-skeleton-ui.azurewebsites.net/customers"
        elif self.env == "dev":
            baseURL = "http://10.204.239.110/QA/CTCorp.WebAPI/CreateOrder/Dashboard/NAEnriqueDecoss"
        elif self.env == "other":
            baseURL = "http://10.205.224.91/CTCorp.WebAPI/CreateOrder/Dashboard/NAEnriqueDecoss"
        else:
            baseURL = "http://qa1.smbstaging.com/"

        if self.browser == "iexplorer":
            # Set ie driver
            iedriver = "C:\\Users\\\enriquealejandro.d\\\Documents\\Lib\\IEDriverServer.exe"
            os.environ["webdriver.ie.driver"] = iedriver
            driver = webdriver.Ie(iedriver)

        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            chromedriver = "C:\\Users\\\enriquealejandro.d\\\Documents\\Lib\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(1440, 900)
        else:
            chromedriver = "C:\\Users\\\enriquealejandro.d\\\Documents\\Lib\\chromedriver.exe"
            os.environ["webdriver.chrome.driver"] = chromedriver
            driver = webdriver.Chrome(chromedriver)
            driver.set_window_size(1440, 900)
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver