import unittest

from data_extractor import DataExtractor


class DataExtractorTestCase(unittest.TestCase):
    def setUp(self):
        self.data_extractor = DataExtractor()

    def test_extract_city_temperature_date_time(self):
        city = 'Gorzów'
        desired_output = {'temperature':20, 'date': "2021-01-21","hour":"14"}
        sample_dict_list = [{'stacja':'Gorzów', 'temperatura':20, 'data_pomiaru':"2021-01-21","godzina_pomiaru":"14"},]
        self.assertEqual(desired_output, self.data_extractor.extract_city_temperature_date_time(city, sample_dict_list))


if __name__ == '__main__':
    unittest.main()
