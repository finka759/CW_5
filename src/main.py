from src.employer import Employer
from src.head_hunter_api import HeadHunrterApi
from src.json_saver import JsonSaver
from src.vacancy import Vacancy


def main():
    user_interaction()


def user_interaction():
    search_query = ''
    while search_query == '':
        search_query = input("Введите поисковый запрос: ")

    salary = None
    while salary is None:
        salary_str = input("Введите минимальную зарплату в рублях: ")
        if salary_str.isdigit():
            salary = int(salary_str)

    hh_api = HeadHunrterApi()
    hh_vacancies = hh_api.get_vacancies(search_query, salary)

    file_json = JsonSaver()
    file_json.save_file(hh_vacancies)

    file_vacancies = file_json.read_file()

    vacancies_list = Vacancy.cast_to_object_list(file_vacancies)
    list_to_sort = vacancies_list
    print(list_to_sort)

    sorted_vacancies_list = Vacancy.sort_vacancies(list_to_sort)
    emloyers_list = Employer.generate_emloyers_list_from_vacancies(vacancies_list)
    # top_n = None
    # while top_n is None:
    #     top_n_str = input(f"Введите количество вакансий для вывода в топ N(до {len(sorted_vacancies_list)}): ")
    #     if top_n_str.isdigit():
    #         top_n = int(top_n_str)
    #
    # top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies_list, top_n)
    # Vacancy.print_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
