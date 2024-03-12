from abc import ABC, abstractmethod


class AbstractHeadHunrterApi:

    @abstractmethod
    def get_vacancies(self, search_query: str, salary):
        pass



