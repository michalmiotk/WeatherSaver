class DataExtractor():
    def extract_temperature(self, city, list_dict):
        for city_info in list_dict:
            if city_info['stacja'] == city:
                return float(city_info['temperatura'])

    def extract_city_temperature_date_time(self, city, list_dict):
        for city_info in list_dict:
            if city_info['stacja'] == city:
                return {'temperature':float(city_info['temperatura']), 'date': city_info['data_pomiaru'], 'hour':city_info['godzina_pomiaru']}