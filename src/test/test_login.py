import unittest
import allure
import pytest

from src.page.page_login import PageLogin
from src.page.page_base import PageBase

@allure.feature("Login")
@allure.story("Iniciamos sesión con distintos tipos de usuarios")
@allure.suite("Login")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Descripción")
class test_Login_01(unittest.TestCase):

    def setUp(self):
        with allure.step("Precondición: Iniciar ChromeDriver y abrir navegador"):
            self.driver = PageBase.iniciar_ChromeDriver(self)
            PageLogin.abrir_navegador(self)

    def test_correctly_login(self):
        with allure.step("validar inicio de sesión con datos correcto"):
            PageLogin.logIn(self)
            message = "key is not in container."
            self.assertIn('/inventory.html', self.driver.current_url, message)

    def test_login_with_incorrect_password(self):
        with allure.step("validar inicio de sesión con contraseña incorrecta"):
            PageLogin.logIn(self, 'standard_user', 'incorrect_password')
            self.assertTrue(PageLogin.debe_aparecer_cartel_de_error(self))

    def test_login_with_blocked_user(self):
        with allure.step("validar inicio de sesión con usuario bloqueado"):
            PageLogin.logIn(self, 'locked_out_user')
            self.assertTrue(PageLogin.debe_aparecer_cartel_de_error(self))

    def test_login_with_problem_user(self):
        with allure.step("validar inicio de sesión con usuario bloqueado"):
            PageLogin.logIn(self, 'problem_user')
            self.assertIn('/inventory.html', self.driver.current_url, 'No ingresa a /inventory')

    def tearDown(self):
        with allure.step("Post-condición: cerrar navegador"):
            PageLogin.cerrar_navegador(self)


if __name__ == "__main__":
    unittest.main()
