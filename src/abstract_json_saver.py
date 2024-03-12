import os
from abc import abstractmethod


class AbstractJsonSaver:
    way_to_json = os.path.join('..', 'data', 'hh_data.json')
    @abstractmethod
    def save_file(self, data: list):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def add_vacancy(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: str):
        pass
