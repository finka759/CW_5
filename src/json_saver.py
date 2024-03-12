import json
import os
from abc import ABC

from src.abstract_json_saver import AbstractJsonSaver




class JsonSaver(AbstractJsonSaver, ABC):

    def save_file(self, data: list):
        with open(JsonSaver.way_to_json, 'w', encoding='utf-8') as file:
            file.write(json.dumps(data, indent=2, ensure_ascii=False))

    def read_file(self):
        with open(JsonSaver.way_to_json, encoding='utf-8') as file:
            return json.load(file)

    def add_vacancy_to_file(self, data: list):
        old_list = self.read_file()
        new_list = data + old_list
        self.save_file(new_list)

    def delete_vacancy(self, vacancy: str):
        new_list = []

        old_list = self.read_file()

        for params in old_list:
            if params['name'] != vacancy:
                new_list.append(params)

        self.save_file(new_list)
