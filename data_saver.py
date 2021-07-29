import copy
import json

class DataSaver():

    def get_extended_dict(self, existing_json, extending_json):
        extended_json = copy.deepcopy(existing_json)
        extended_json['logs'].append(extending_json)
        return extended_json

    def create_json_from_data(self, city, temperature, date, hour):
        return {'city': city, 'temperature': temperature, 'date': date,"hour": hour}

    def append_data_to_file(self, new_dict, file_path):
        old_data = json.load(file_path)
        json.dump(file_path, dict)