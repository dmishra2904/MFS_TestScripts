import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


FILENAME = "Services.csv"


def read_content():
    services = []
    with open(FILENAME, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            services.append(row)
    return services


def addServices(driver):
    services = read_content()
    print((len(services)))
    for i in range(len(services)):
        service = services[i]
        if i != 0:
            id_customer = service[0]
            id_service_category = service[1]
            id_description = service[2]
            id_location = service[3]
            id_setup_time = service[4]
            id_cleanup_time = service[5]
            id_cost = service[6]

            elem = driver.find_element_by_id("id_cust_name")
            elem.send_keys(id_customer)
            elem = driver.find_element_by_id("id_service_category")
            elem.send_keys(id_service_category)
            elem = driver.find_element_by_id("id_description")
            elem.send_keys(id_description)
            elem = driver.find_element_by_id("id_location")
            elem.send_keys(id_location)
            elem = driver.find_element_by_id("id_setup_time")
            elem.clear()
            elem.send_keys(id_setup_time)
            elem = driver.find_element_by_id("id_cleanup_time")
            elem.clear()
            elem.send_keys(id_cleanup_time)
            elem = driver.find_element_by_id("id_service_charge")
            elem.send_keys(id_cost)
            time.sleep(3)
            driver.get_screenshot_as_file(
                "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\AddService.png")

            driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/form/button').submit()

            time.sleep(2)

            if i < len(services)-1:
                print(i)

                elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span')
                driver.get_screenshot_as_file(
                    "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\AddMoreServices.png")
                elem.click()



class MFS_AddService(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome(
           executable_path=
           'C:/Users/devan/OneDrive/Documents/Github/8210_goodshepherdfoodpantry/8210projectT4/venv/'
           'Scripts/chromedriver.exe')

    def test_addservice(self):
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


        # go to Services Portal
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a')
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\AddServicePortal.png")
        elem.click()
        time.sleep(3)

        # click on Add Services
        elem = driver.find_element_by_xpath('//*[@id="app-layout"]/div/div/div/div[3]/div/a/span')
        elem.click()
        time.sleep(5)

        #run script to  add services from CSV
        addServices(driver)

        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com/service_list")
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\AddedService.png")

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()





