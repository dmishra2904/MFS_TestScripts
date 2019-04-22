import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



class MFS_DeleteCustomer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
           executable_path=
           'C:/Users/devan/OneDrive/Documents/Github/8210_goodshepherdfoodpantry/8210projectT4/venv/'
           'Scripts/chromedriver.exe')

    def test_deletecustomer(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        # opens homepage url
        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com")
        driver.implicitly_wait(5)

        # select login option from navigation bar
        elem = driver.find_element_by_xpath('//*[@id="myNavbar"]/ul[2]/li[1]/a')
        elem.click()


        # enter user credentials
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com/admin")
        assert "Logged In"
        time.sleep(3)


        # go to Customer Portal
        elem = driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[1]/th/a')
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\DeleteCustomerPortal.png")
        elem.click()
        time.sleep(3)
        # select items to be deleted
        elem = driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[5]/td[1]/input')
        elem.click()
        elem = driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[6]/td[1]/input')
        elem.click()
        elem = driver.find_element_by_xpath('//*[@id="result_list"]/tbody/tr[7]/td[1]/input')
        elem.click()
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\DeleteSelectedCustomers.png")
        time.sleep(3)

        # select action dropdown
        elem = driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/label/select')
        elem.click()
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\SelectDeleteCustomer.png")
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/label/select/option[2]')
        elem.click()
        elem = driver.find_element_by_xpath('//*[@id="changelist-form"]/div[1]/button')
        elem.click()
        time.sleep(2)

        # confirm deleting item
        elem = driver.find_element_by_xpath('//*[@id="content"]/form/div/input[4]')
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\DeleteSelectedCustomerConfirmation.png")
        elem.submit()

        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\CustomerDeletedList.png")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()










