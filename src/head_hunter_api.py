import json

import requests

from src.abstract_head_hunter_api import AbstractHeadHunrterApi


class HeadHunrterApi(AbstractHeadHunrterApi):

    @staticmethod
    def get_areas():
        req = requests.get('https://api.hh.ru/areas')
        data = req.content.decode()
        req.close()
        jsObj = json.loads(data)
        areas = []
        for k in jsObj:
            for i in range(len(k['areas'])):
                if len(k['areas'][i]['areas']) != 0:  # Если у зоны есть внутренние зоны
                    for j in range(len(k['areas'][i]['areas'])):
                        areas.append([k['id'],
                                      k['name'],
                                      k['areas'][i]['areas'][j]['id'],
                                      k['areas'][i]['areas'][j]['name']])
                else:  # Если у зоны нет внутренних зон
                    areas.append([k['id'],
                                  k['name'],
                                  k['areas'][i]['id'],
                                  k['areas'][i]['name']])
        return areas

    def __init__(self, base_url: str = 'https://api.hh.ru'):
        self.base_url = base_url

    def get_vacancies(self, search_query: str, salary):
        vacancies_url_list = (self.base_url, 'vacancies')
        vacancies_url = '/'.join(vacancies_url_list)

        params = {
            'area': 113,  # Поиск в зоне 113 Pjccbz
            'text': search_query,  # Поисковый запрос
            'salary': salary,
            'page': 0,
            'per_page': 100
        }

        req = requests.get(vacancies_url, params)

        data_ = req.json()
        req.close()

        return data_['items']

    def get_vacancies_for_employer(self, employer_id, page: str = '0'):
        vacancies_url_list = (self.base_url, 'vacancies')
        vacancies_url = '/'.join(vacancies_url_list)

        params = {
            'employer_id': employer_id,
            'page': int(page)
        }

        print(requests.get(vacancies_url, params))
        req = requests.get(vacancies_url, params)

        data_ = req.json()
        req.close()

        return data_

    def get_employer(self, employer_id: str):
        employer_url_list = (self.base_url, 'employers', employer_id)
        employer_url = '/'.join(employer_url_list)
        req = requests.get(employer_url)
        data_ = req.json()
        req.close()

        return data_
