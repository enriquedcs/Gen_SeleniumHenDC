from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class ClickandSendKeys():

    def test(self):
        BaseURL= "http://enrique.decoss:Ae1883iv$@10.204.239.110/QA/CT.CTCorp.OrderSearch/Dashboard/CreateOrder.aspx/"
        driverLocation = "C:\\Users\\\enriquealejandro.d\\\Documents\\Lib\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.maximize_window()
        driver.get(BaseURL)
        driver.implicitly_wait(10)

        #Find Elements

        cookiecheck = driver.find_element(By.ID, "txtCustomerName")
        #cookieclick.is_displayed()
        cookiecheck.click()
        cookieclick = driver.find_element(By.ID, "txtCustomerPhoneNumber")
        cookieclick.click()

        time.sleep(2)

        MyaccountL = driver.find_element(By.XPATH, "//span[contains(text(),'My Account')]")
        MyaccountL.click()

        emailField = driver.find_element(By.ID, "edit-name")
        emailField.is_displayed()
        emailField.send_keys("enrique.decoss@wolterskluwer.co")

        passwordField = driver.find_element(By.ID, "edit-pass")
        passwordField.send_keys("Today123")

        Submitbtn = driver.find_element(By.ID, "edit-submit")
        Submitbtn.click()

        time.sleep(3)

        AllProducts = driver.find_element(By.XPATH, "//div[@class='box-content']//a[@id='btndocumentUri']")
        #AllProducts.is_displayed()
        AllProducts.click()

        time.sleep(3)

        # MyOrder = driver.find_element(By.ID, "MYORDERS")
        # MyOrder.is_displayed()
        # MyOrder.click()

cc = ClickandSendKeys()
cc.test()