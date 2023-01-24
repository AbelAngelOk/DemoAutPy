import unittest

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

# libreria correcta para time sleep
import time

# libreria correcta para EC en WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageBase:

    def iniciar_ChromeDriver(self):
        #self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        return self.driver

    # deprecated
    def esperar_elemento_visible(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, locator)))

    # deprecated
    @staticmethod
    def esperar_segundos(seconds):
        time.sleep(seconds)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True
