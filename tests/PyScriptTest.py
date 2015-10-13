import unittest
from pyscript import pyscript

class MyTestCase(unittest.TestCase):
    def test_open(self):
        pys = pyscript.open("https://www.google.com")
        self.assertEqual(pys.terminal()._content_type, 'application/text' )

    def test_openSession(self):
        pys = pyscript.open("https://www.google.com")
        session = pys._open_session()
        self.assertEqual(session,True)



if __name__ == '__main__':
    unittest.main()
