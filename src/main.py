from src.config import config
from src.db_manager import DBManager
from src.employer import Employer
from src.head_hunter_api import HeadHunrterApi
from src.vacancy import Vacancy


def main():
    user_interaction()


def user_interaction():
    # search_query = ''
    # while search_query == '':
    #     search_query = input("Введите поисковый запрос: ")
    #
    # salary = None
    # while salary is None:
    #     salary_str = input("Введите минимальную зарплату в рублях: ")
    #     if salary_str.isdigit():
    #         salary = int(salary_str)
    #
    # hh_api = HeadHunrterApi()
    # hh_vacancies = hh_api.get_vacancies(search_query, salary)
    #
    # vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
    #
    # sorted_vacancies_list = Vacancy.sort_vacancies(vacancies_list)
    #
    # top_emloyers_list = Employer.generate_emloyers_list_from_vacancies_list(sorted_vacancies_list, 2)
    # Employer.print_employers(top_emloyers_list)
    # data = Employer.get_employers_data(top_emloyers_list)
    # print(data)
    #
    params = config()
    dm_manager_top_employers = DBManager('top_employers', params)
    # dm_manager_top_employers.create_database()
    # dm_manager_top_employers.save_data_to_database(data)

    dm_manager_top_employers.get_companies_and_vacancies_count()
    dm_manager_top_employers.get_all_vacancies()
    dm_manager_top_employers.get_avg_salary()
    dm_manager_top_employers.get_vacancies_with_higher_salary()
    dm_manager_top_employers.get_vacancies_with_keyword('python')




if __name__ == "__main__":
    main()
