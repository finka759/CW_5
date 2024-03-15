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

    choise = (input("Желаете сделать выборку с учётом региона? Y/N - ")).upper()
    if choise == 'Y':
        regions_dict = Vacancy.get_areas_from_vacancies(vacancies_list)
        for region, id_ in regions_dict.items():
            print(f"{region}, {id_}")
        seaking_region_id = None
        while seaking_region_id is None:
            str_ = input("Введите номер региона из списка - ")
            if str_.isdigit() and str_ in regions_dict.values():
                seaking_region_id = str_

        vacancies_list_in_region = Vacancy.get_vacancies_in_region(vacancies_list, seaking_region_id)
        list_to_sort = vacancies_list_in_region

    sorted_vacancies_list = Vacancy.sort_vacancies(list_to_sort)


    top_n = None
    while top_n is None:
        top_n_str = input(f"Введите количество вакансий для вывода в топ N(до {len(sorted_vacancies_list)}): ")
        if top_n_str.isdigit():
            top_n = int(top_n_str)

    top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies_list, top_n)
    Vacancy.print_vacancies(top_vacancies)


if __name__ == "__main__":
    main()
