import unittest
from data_extractor import DataExtractor

class DataExtractorTestCase(unittest.TestCase):
    def setUp(self):
        self.data_extractor = DataExtractor()

    def test_extract_city_temperature(self):
        city = 'Gorzów'
        desired_output = 30
        sample_dict_list = [{'stacja':'Gorzów', 'temperatura':'30'},]
        self.assertEqual(desired_output, self.data_extractor.extract_temperature(city, sample_dict_list))

if __name__ == '__main__':
    unittest.main()
