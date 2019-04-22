import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class MFS_Login(unittest.TestCase):
    def setUp(self):
       self.driver = webdriver.Chrome(
           executable_path=
           'C:/Users/devan/OneDrive/Documents/Github/8210_goodshepherdfoodpantry/8210projectT4/venv/'
           'Scripts/chromedriver.exe')

    def test_login(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver
        driver.maximize_window()
        # opens homepage url
        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com/admin")
        driver.get_screenshot_as_file("C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\Login.png")
        driver.implicitly_wait(5)


        # enter user credentials
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        driver.get_screenshot_as_file\
            ("C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\Login_Credentials.png")
        elem.send_keys(Keys.RETURN)
        driver.get("https://devanshika-mfscrm-a1p2.herokuapp.com/admin")
        assert "Logged In"
        driver.get_screenshot_as_file(
            "C:\\Users\\devan\\8210 Projects\\MFS test scripts\\screenshots\\LoggedIn.png")
        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

