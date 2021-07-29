import copy
import json

class DataSaver():

    def get_extended_dict(self, existing_json, extending_json):
        extended_json = copy.deepcopy(existing_json)
        extended_json['logs'].append(extending_json)
        return extended_json

    def create_dict_from_data(self, city, temperature, date, hour):
        return {'city': city, 'temperature': temperature, 'date': date,"hour": hour}

    def append_data_to_file(self, new_dict, file_path):
        try:
            with open(file_path, 'r') as f:
                try:
                    old_data = json.load(f)
                except json.JSONDecodeError :
                    old_data = {'logs': []}
        except IOError:
            old_data = {'logs':[]}
        extended_dict = self.get_extended_dict(old_data, new_dict)
        with open(file_path, 'w') as f:
            json.dump(extended_dict, f,  indent=4)
            print("Dane zapisane w ",file_path)