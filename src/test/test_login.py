import unittest

from src.page.page_login import PageLogin
from src.page.page_base import PageBase

class Test_Login_01(unittest.TestCase):

    def setUp(self):
        self.driver = PageBase.iniciar_ChromeDriver(self)
        PageLogin.abrir_navegador(self)

    def test_correctly_login(self):
        PageLogin.logIn(self)
        message = "key is not in container."
        self.assertIn('/inventory.html', self.driver.current_url, message)

    def test_login_with_incorrect_password(self):
        PageLogin.logIn(self, 'standard_user', 'incorrect_password')
        self.assertTrue(PageLogin.debe_aparecer_cartel_de_error(self))

    def test_login_with_blocked_user(self):
        PageLogin.logIn(self, 'locked_out_user')
        self.assertTrue(PageLogin.debe_aparecer_cartel_de_error(self))

    def test_login_with_problem_user(self):
        PageLogin.logIn(self, 'problem_user')
        self.assertIn('/inventory.html', self.driver.current_url, 'No ingresa a /inventory')

    def tearDown(self):
        PageLogin.cerrar_navegador(self)


if __name__ == "__main__":
    unittest.main()