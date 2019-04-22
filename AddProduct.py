import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


FILENAME = "Products.csv"


def read_content():
    products = []
    with open(FILENAME, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            products.append(row)
    return products


def addProducts(driver):
    products = read_content()
    print((len(products)))
    for i in range(len(products)):
        product = products[i]
        if i != 0:
            id_customer = product[0]
            id_product = product[1]
            id_description = product[2]
            id_quantity = product[3]
            id_pickup_time = product[4]
            id_charge = product[5]

            elem = driver.find_element_by_id("id_cust_name")
            elem.send_keys(id_customer)
            elem = driver.find_element_by_id("id_product")
            elem.send_keys(id_product)
            elem = driver.find_element_by_id("id_p_description")
            elem.send_keys(id_description)
            elem = driver.find_element_by_id("id_quantity")
            elem.send_keys(id_quantity)
            elem = driver.find_element_by_id("id_pickup_time")
            elem.clear()
            elem.send_keys(id_pickup_time)
            elem = driver.find_element_by_id("id_charge")
            elem.clear()
            elem.send_keys(id_charge)
            driver.get_screenshot_as_file(
                "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\AddProduct.png")

            time.sleep(2)

            driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').submit()

            time.sleep(2)

            if i < len(products)-1:
                print(i)
                driver.get_screenshot_as_file(
                    "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\AddMoreProduct.png")
                driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span').click()


class MFS_AddProduct(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome(
           executable_path=
           'C:/Users/devan/OneDrive/Documents/Github/8210_goodshepherdfoodpantry/8210projectT4/venv/'
           'Scripts/chromedriver.exe')

    def test_addproduct(self):
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
        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com/")
        assert "Logged In"
        time.sleep(2)


        # go to Product Portal
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a')
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\ProductPortal.png")
        elem.click()
        time.sleep(3)

        # click on Add Product
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span')
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\AddProduct.png")
        elem.click()
        time.sleep(5)

        #run script to  add services from CSV
        addProducts(driver)
        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com/product_list")
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\AddedProductList.png")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()





