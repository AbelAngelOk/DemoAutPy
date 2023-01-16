import unittest

from src.page.page_login import PageLogin
from src.page.page_base import PageBase

class Test_Login_01(unittest.TestCase):

    def setUp(self):
        self.driver = PageBase.iniciar_ChromeDriver(self)
        PageLogin.abrir_navegador(self)

    def test_correctly_login(self):
        PageLogin.logIn(self)

    def test_login_with_incorrect_password(self):
        PageLogin.logIn(self, 'standard_user', 'incorrect_password')

    def test_login_with_blocked_user(self):
        PageLogin.logIn(self, 'locked_out_user')

    def test_login_with_problem_user(self):
        PageLogin.logIn(self, 'problem_user')

    def tearDown(self):
        PageLogin.cerrar_navegador(self)


if __name__ == "__main__":
    unittest.main()
