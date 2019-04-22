import unittest
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# file should be kept in the current directory
FILENAME = "Customers.csv"


def read_content():
    customers = []
    with open(FILENAME, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            customers.append(row)
    return customers


def addCustomers(driver):
    customers = read_content()
    print((len(customers)))
    for i in range(len(customers)):
        customer = customers[i]
        if i != 0:
            id_customer_name = customer[0]
            id_organization = customer[1]
            id_role = customer[2]
            id_email = customer[3]
            id_bldgroom = customer[4]
            id_address = customer[5]
            id_account_number = customer[6]
            id_city = customer[7]
            id_state = customer[8]
            id_zipcode = customer[9]
            id_phone = customer[10]

            elem = driver.find_element_by_id("id_cust_name")
            elem.send_keys(id_customer_name)
            elem = driver.find_element_by_id("id_organization")
            elem.send_keys(id_organization)
            elem = driver.find_element_by_id("id_role")
            elem.send_keys(id_role)
            elem = driver.find_element_by_id("id_email")
            elem.send_keys(id_email)
            elem = driver.find_element_by_id("id_bldgroom")
            elem.send_keys(id_bldgroom)
            elem = driver.find_element_by_id("id_address")
            elem.send_keys(id_address)
            elem = driver.find_element_by_id("id_account_number")
            elem.send_keys(id_account_number)
            elem = driver.find_element_by_id("id_city")
            elem.send_keys(id_city)
            elem = driver.find_element_by_id("id_state")
            elem.send_keys(id_state)
            elem = driver.find_element_by_id("id_zipcode")
            elem.send_keys(id_zipcode)
            elem = driver.find_element_by_id("id_phone_number")
            elem.send_keys(id_phone)
            driver.get_screenshot_as_file(
                "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\Customer.png")
            driver.find_element_by_xpath('//*[@id="customer_form"]/div/div/input[1]').click()

            time.sleep(2)

            if i < len(customers)-1:
                print(i)
                driver.get_screenshot_as_file(
                    "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\NewCustomer.png")
                driver.find_element_by_xpath('//*[@id="content-main"]/ul/li/a').click()


class MFS_addcustomer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=
            'C:/Users/devan/OneDrive/Documents/Github/8210_goodshepherdfoodpantry/8210projectT4/venv/'
            'Scripts/chromedriver.exe')

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com/admin")

        # enter user credentials
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        # driver.get("https://gs-foodpantry.herokuapp.com/")
        assert "Logged In"
        time.sleep(3)

        elem = driver.find_element_by_xpath('//*[@id="content-main"]/div[2]/table/tbody/tr[1]/td[1]/a')
        elem.click()
        time.sleep(3)
        assert "Add Customer"
        # driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span').click()
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\AddFirstCustomer.png")
        addCustomers(driver)
        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com/customer_list")
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\AddedCustomerList.png")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()


