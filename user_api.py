import logging

from api_handler import ApiHandler
from data_saver import DataSaver
from data_extractor import DataExtractor

class UserApi():
    def __init__(self):
        self.save_filename = 'save.json'
        self.data_saver = DataSaver()

    def _save_new_data(self, city, temperature, date, hour):
        extra_dict = self.data_saver.create_dict_from_data(city, temperature, date, hour)
        self.data_saver.append_data_to_file(extra_dict, self.save_filename)

    def new_log(self, city="Gorzów"):
        api_handler = ApiHandler()
        print("rozpoczęto łączenie z serwerem")
        cities_info_as_list_dict = api_handler.request_dict_list()
        print("zakończono łączenie z serwerem")
        data_extractor = DataExtractor()
        city_info = data_extractor.extract_city_temperature_date_time(city, cities_info_as_list_dict)
        data_dict = self.data_saver.create_dict_from_data(city, city_info['temperature'], city_info['date'], city_info['hour'])
        self.data_saver.append_data_to_file(data_dict, self.save_filename)
