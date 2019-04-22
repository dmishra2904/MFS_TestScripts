import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MFS_ReadCustomerSummary(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome(
           executable_path=
           'C:/Users/devan/OneDrive/Documents/Github/8210_goodshepherdfoodpantry/8210projectT4/venv/'
           'Scripts/chromedriver.exe')

    def test_readcustomer(self):
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
        time.sleep(2)


        # go to Customer Portal
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[2]/a')
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\SelectSummaryCustomerPortal.png")
        elem.click()
        time.sleep(3)

        # click on customer's details
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/table/tbody/tr[5]/td[14]/a')
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\SelectCustomerforSummary.png")
        elem.click()
        time.sleep(5)

        #email report to customer
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div[1]/div[4]/a/span')
        elem.click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()





