from abc import ABC, abstractmethod


class AbstractHeadHunrterApi(ABC):

    @abstractmethod
    def get_vacancies(self, search_query: str, salary):
        pass



