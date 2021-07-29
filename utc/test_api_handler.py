import unittest

from api_handler import ApiHandler


class ApiHandlerTestCase(unittest.TestCase):
    def setUp(self):
        self.api_handler = ApiHandler()

    def test_decoding(self):
        bytes_input = b'Gorz\u00f3w'
        desired_output = "Gorzów"
        self.assertEqual(self.api_handler.decoder(bytes_input), desired_output)


if __name__ == '__main__':
    unittest.main()
