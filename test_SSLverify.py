import unittest
import run

class MyTestCase(unittest.TestCase):
    def test_url_connect(self):
        status = run.url_connect('https://www.google.com')
        self.assertEqual('Success', status)


if __name__ == '__main__':
    unittest.main()
