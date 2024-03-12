import requests

from abstract_head_hunter_api import AbstractHeadHunrterApi


class HeadHunrterApi(AbstractHeadHunrterApi):

    def __init__(self, base_url: str = 'https://api.hh.ru'):
        self.base_url = 'https://api.hh.ru'

    def get_vacancies(self, search_query: str, salary):
        vacancies_url_list = (self.base_url, 'vacancies')
        vacancies_url = '/'.join(vacancies_url_list)

        params = {
            'area': 113,  # Поиск в зоне 113 Pjccbz
            'text': search_query,  # Поисковый запрос
            'page': 0,
            'per_page': 100
        }

        req = requests.get(vacancies_url, params)

        data_ = req.json()
        req.close()
        return data_['items']
