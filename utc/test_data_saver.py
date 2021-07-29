import copy
import unittest
from data_saver import DataSaver
from copy import deepcopy

class TestDataSaver(unittest.TestCase):
    def setUp(self) -> None:
        self.data_saver = DataSaver()

    def test_extending_dict(self):
        existing_json = {'logs':[{'city':'Gorzów', 'temperature':30, 'date':"2021-07-29","hour":"7"}, ]}
        desired_json = {'logs':[{'city':'Gorzów', 'temperature':30, 'date':"2021-07-29","hour":"7"}, \
                {'city':'Szczecin', 'temperature':20, 'date':"2021-01-21","hour":"14"}]}
        extending_json =  {'city':'Szczecin', 'temperature':20, 'date':"2021-01-21","hour":"14"}
        self.assertEqual(desired_json, self.data_saver.get_extended_dict(existing_json, extending_json))

    def test_not_modify_existing_dict_during_extending_dict(self):
        existing_json = {'logs': [{'city': 'Gorzów', 'temperature': 30, 'date': "2021-07-29", "hour": "7"}, ]}
        existing_json_copy = copy.deepcopy(existing_json)
        extending_json = {'city': 'Szczecin', 'temperature': 20, 'date': "2021-01-21", "hour": "14"}
        self.data_saver.get_extended_dict(existing_json, extending_json)
        self.assertEqual(existing_json, existing_json_copy)

    def test_create_json_from_data(self):
        temperature = 20
        date = "2021-01-21"
        hour = "14"
        city = "Szczecin"
        desired_json =  {'city':'Szczecin', 'temperature':20, 'date':"2021-01-21","hour":"14"}
        self.assertEqual(desired_json, self.data_saver.create_dict_from_data(city, temperature, date, hour))



if __name__ == '__main__':
    unittest.main()
