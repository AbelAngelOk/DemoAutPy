import time
import unittest

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test_Login_01(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.saucedemo.com/")

    def test_puto(self):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "user-name")))
        self.driver.find_element(By.ID, "user-name").send_keys("user")
        self.driver.find_element(By.ID, "password").send_keys("passwd")
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(20)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
