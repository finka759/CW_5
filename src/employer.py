from typing import Any

from src.head_hunter_api import HeadHunrterApi


class Employer:
    @staticmethod
    def generate_emloyers_list_from_vacancies_list(vacancies_list, limit_: int = 10):
        """
        Получает на вход словарь вкансий
        Возвращает список список из 10 работодателей
        """
        top_employers = []
        count: int = 0
        while len(top_employers) < limit_:
            if vacancies_list[count].employer_id is not None:  # проверка наличия id у работодателя
                if Employer(vacancies_list[count].employer_id,
                            vacancies_list[count].employer_name) not in top_employers:
                    top_employers.append(
                        Employer(vacancies_list[count].employer_id, vacancies_list[count].employer_name))
            count += 1

        return top_employers

    @staticmethod
    def print_employers(employers_list):
        """
        Получает список объектов Работодателей
        вызывает для каждой вакансии метод print
        """
        for employer in employers_list:
            print(employer)

    @staticmethod
    def get_employers_data(top_emloyers_list) -> list[dict[str, Any]]:
        data = []
        hh_api_2 = HeadHunrterApi()
        for employer in top_emloyers_list:
            employer_data = hh_api_2.get_employer(employer.employer_id)
            page = '0'
            pages = '1'
            vacancies_for_employer_data = []
            while int(page) < int(pages):
                response = hh_api_2.get_vacancies_for_employer(employer.employer_id, page)
                page = str(int(response['page']) + 1)
                pages = response['pages']
                vacancies_for_employer_data.extend(response['items'])
            data.append({
                'employer': employer_data,
                'vacancies': vacancies_for_employer_data
            })
        return data

    def __init__(self, employer_id: str, name: str):
        self.employer_id = employer_id
        self.name = name

    def __str__(self):
        return (f"Работодатель - {self.name} (id - {self.employer_id})\n")
