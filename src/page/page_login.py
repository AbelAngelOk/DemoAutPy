import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from src.page.page_base import PageBase


class PageLogin(PageBase):
    url = "https://www.saucedemo.com/"
    TxtUserName = "user-name"
    TxtPassword = "password"
    BtnLogin = "login-button"

    @staticmethod
    def get(locator):
        return locator

    def abrir_navegador(self):
        self.driver.get(PageLogin.url)

    def cerrar_navegador(self):
        self.driver.close()

    def logIn(self, user='standard_user', passwd='secret_sauce'):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, PageLogin.TxtUserName)))
        self.driver.find_element(By.ID, PageLogin.TxtUserName).send_keys(user)
        self.driver.find_element(By.ID, PageLogin.TxtPassword).send_keys(passwd)
        self.driver.find_element(By.ID, PageLogin.BtnLogin).click()
        time.sleep(10)
