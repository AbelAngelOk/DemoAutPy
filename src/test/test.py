import unittest

from src.page.page_login import PageLogin
from src.page.page_base import PageBase

class Test_Login_01(unittest.TestCase):

    def setUp(self):
        self.driver = PageBase.iniciar_ChromeDriver(self)
        PageLogin.abrir_navegador(self)

    def test_login(self):
        PageLogin.logIn(self)

    def tearDown(self):
        PageLogin.cerrar_navegador(self)


if __name__ == "__main__":
    unittest.main()
