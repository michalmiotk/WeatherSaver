class DataExtractor():
    def extract_temperature(self, city, list_dict):
        for city_info in list_dict:
            if city_info['stacja'] == city:
                return city_info['temperatura']