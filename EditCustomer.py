import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MFS_EditCusotmer(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome(
           executable_path=
           'C:/Users/devan/OneDrive/Documents/Github/8210_goodshepherdfoodpantry/8210projectT4/venv/'
           'Scripts/chromedriver.exe')

    def test_editcustomer(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        # opens homepage url
        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com")

        # select login option from navigation bar
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[1]/a')
        elem.click()

        # enter user credentials
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com/")
        assert "Logged In"
        time.sleep(3)

        # go to Customer Portal
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a')
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\EditCustomerPortal.png")
        elem.click()
        time.sleep(3)

        # edit a customer's details
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[6]/td[12]/a')
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\EditSelectedCustomer.png")
        elem.click()
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="id_bldgroom"]')
        account = "PKI Room 143"
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\OriginalCustomerDetails.png")
        elem.clear()
        time.sleep(1)
        elem.send_keys(account)
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\UpdatedCustomerDetails.png")
        time.sleep(2)
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button')
        elem.click()
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\EditedCustomerList.png")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()





