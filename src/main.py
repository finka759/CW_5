from src.config import config
from src.db_manager import DBManager
from src.employer import Employer
from src.head_hunter_api import HeadHunrterApi
from src.vacancy import Vacancy



def main():
    search_query = ''
    while search_query == '':
        search_query = input("Введите поисковый запрос(это-же слово будет использовано в get_vacancies_with_keyword): ")

    salary = None
    while salary is None:
        salary_str = input("Введите минимальную зарплату в рублях: ")
        if salary_str.isdigit():
            salary = int(salary_str)

    limit = None
    while limit is None:
        limit_str = input("Введите количество работодателей(от 1 до 10): ")
        if limit_str.isdigit() and 0 < int(limit_str) < 11:
            limit = int(limit_str)

    hh_api = HeadHunrterApi()
    hh_vacancies = hh_api.get_vacancies(search_query, salary)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    sorted_vacancies_list = Vacancy.sort_vacancies(vacancies_list)

    top_emloyers_list = Employer.generate_emloyers_list_from_vacancies_list(sorted_vacancies_list, 2)
    print('')
    print('Выбраны работодатели:')
    print('---------------------')
    Employer.print_employers(top_emloyers_list)
    data = Employer.get_employers_data(top_emloyers_list)


    params = config()
    dm_manager_top_employers = DBManager('top_employers', params)
    dm_manager_top_employers.create_database()
    dm_manager_top_employers.save_data_to_database(data)
    print()
    print('get_companies_and_vacancies_count()')
    print('-----------------------------------')
    dm_manager_top_employers.get_companies_and_vacancies_count()
    print()
    print('get_all_vacancies()')
    print('-----------------------------------')
    dm_manager_top_employers.get_all_vacancies()
    print()
    print('get_avg_salary()')
    print('-----------------------------------')
    dm_manager_top_employers.get_avg_salary()
    print()
    print('get_vacancies_with_higher_salary()')
    print('-----------------------------------')
    dm_manager_top_employers.get_vacancies_with_higher_salary()
    print()
    print('get_vacancies_with_keyword(search_query)')
    print('-----------------------------------')
    dm_manager_top_employers.get_vacancies_with_keyword(search_query)




if __name__ == "__main__":
    main()
