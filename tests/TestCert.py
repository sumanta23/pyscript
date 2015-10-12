from pyscript.reader import Reader

__author__ = 'sumanta'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        r = Reader("google.com",443)
        x509 = r.get_server_cert()
        var = str(x509.get_subject())
        print(var)
        self.assertTrue("*.google.com" in var.lower(),"Subject does not match")


if __name__ == '__main__':
    unittest.main()
