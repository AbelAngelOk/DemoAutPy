import unittest
import test_login

# propósito: ejecuta todas las suites de prueba agregadas al método.
if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(test_login))
    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)
