from abc import ABC

from src.abstract_vacancy import AbstractVacancy


class Vacancy(AbstractVacancy, ABC):

    @staticmethod
    def cast_to_object_list(hh_vacancies):
        """
        Получает на вход словарь вкансий
        Возвращает список объектов типа Vacancy
        """
        vacancies_list = []
        for item in hh_vacancies:
            salary_from = 0
            if item['salary'] is not None:
                if item['salary']['from'] is not None:
                    salary_from = int(item.get('salary', {}).get('from', '0'))
            vacancies_list.append(
                Vacancy(item['id'], item['name'], item['alternate_url'], item['published_at'], salary_from))
        return vacancies_list

    @staticmethod
    def sort_vacancies(vacancies_list):
        """
        Получает на вход список не отсортированных объектов вакансий
        Возвращает отсортированный по мин зарплате список объектов вакансий
        """
        # sorted_vacancies = sorted(vacancies_list, key=lambda x: x.salary_from, reverse=True)
        sorted_vacancies = sorted(vacancies_list)
        return sorted_vacancies

    @staticmethod
    def get_top_vacancies(vacancies_list, top_n):
        """
        Получает на вход список  отсортированных объектов вакансий
        Возвращает  список объектов вакансий с наибольшей минимальной зарплатой в количестве  top_n
        """
        return vacancies_list[:top_n]

    @staticmethod
    def print_vacancies(vacancies_list):
        """
        Получает список объектов вакансий
        вызывает для каждой вакансии метод print
        """
        for vacancy in vacancies_list:
            print(vacancy)

    def __init__(self, vacancy_id: str, name: str, alternate_url: str, published_at: str = None,
                 salary_from: int = 0):
        self.vacancy_id = vacancy_id
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from
        self.published_at = published_at

    def __str__(self):
        return f"id выкансии - {self.vacancy_id}\n Мин.зарплата - {self.salary_from}\nСсылка - {self.alternate_url}\nОпубликована - {self.published_at}\n"

    def __lt__(self, other):
        if other.salary_from < self.salary_from:
            return True
