from src.abstract_vacancy import AbstractVacancy


class Vacancy(AbstractVacancy):

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

            item_area_id = item.get('area', {}).get('id', None)
            item_area_name = item.get('area', {}).get('name', None)
            item_employer_id = item.get('employer', {}).get('id', None)
            item_employer_name = item.get('employer', {}).get('name', None)
            vacancies_list.append(Vacancy(item['id'], item['name'], item['alternate_url'], item['published_at'],
                                          salary_from, item_area_id, item_area_name, item_employer_id, item_employer_name))
        return vacancies_list

    @staticmethod
    def sort_vacancies(vacancies_list):
        """
        Получает на вход список не отсортированных объектов вакансий
        Возвращает отсортированный по мин зарплате список объектов вакансий
        """
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

    @staticmethod
    def get_areas_from_vacancies(vacancies_list):
        """
        Получает список объектов вакансий
        возвращает словарь регионов в найденных вакансиях
        """
        regions_dict: dict = {}
        for vacancy in vacancies_list:
            regions_dict[vacancy.area_name] = vacancy.area_id
        sorted_dict = dict(sorted(regions_dict.items()))
        return sorted_dict

    @staticmethod
    def get_vacancies_in_region(vacancies_list, seaking_region_id):
        vacancies_in_region = []
        for item in vacancies_list:
            if item.area_id == seaking_region_id:
                vacancies_in_region.append(item)
        return vacancies_in_region

    def __init__(self, vacancy_id: str, name: str, alternate_url: str, published_at: str = None,
                 salary_from: int = 0, area_id: str = None, area_name: str = None, employer_id: str = None,
                 employer_name: str = None):
        self.vacancy_id = vacancy_id
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from
        self.published_at = published_at
        self.area_id = area_id
        self.area_name = area_name
        self.employer_id = employer_id
        self.employer_name = employer_name

    def __str__(self):
        return (f"id выкансии - {self.vacancy_id}\nМин.зарплата - {self.salary_from}\nСсылка - {self.alternate_url}\n"
                f"Опубликована - {self.published_at}\nРегион - {self.area_name} (id - {self.area_id})\nРаботодатель - {self.employer_name} (id - {self.employer_id})\n")

    def __lt__(self, other):
        if other.salary_from < self.salary_from:
            return True
        return False
