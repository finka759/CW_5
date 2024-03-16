
from abc import abstractmethod, ABC


class AbstractJsonSaver(ABC):

    @abstractmethod
    def save_file(self, data: list):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def add_vacancy_to_file(self):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: str):
        pass
