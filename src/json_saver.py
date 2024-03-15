import json
import os

from src.abstract_json_saver import AbstractJsonSaver


class JsonSaver(AbstractJsonSaver):

    def __init__(self, fail_name: str = 'hh_data.json'):
        self.way_to_json = os.path.join('..', 'data', fail_name)

    def save_file(self, data_: list):
        with open(self.way_to_json, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data_, indent=2, ensure_ascii=False))

    def read_file(self):
        with open(self.way_to_json, encoding='utf-8') as file:
            return json.load(file)

    def add_vacancy_to_file(self, data_: list = None):
        old_list = self.read_file()
        new_list = data_ + old_list
        self.save_file(new_list)

    def delete_vacancy(self, vacancy: str):
        new_list = []

        old_list = self.read_file()

        for params in old_list:
            if params['name'] != vacancy:
                new_list.append(params)

        self.save_file(new_list)
