from typing import Any

import psycopg2


class DBManager:

    def __init__(self, database_name: str, params: dict):
        self.database_name = database_name
        self.params = params

    def create_database(self) -> None:
        conn = psycopg2.connect(dbname='postgres', **self.params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"DROP DATABASE IF EXISTS {self.database_name}")
        cur.execute(f"CREATE DATABASE {self.database_name}")

        conn.close()
        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        create_employers = "CREATE TABLE employers (\
                                           employer_id int UNIQUE PRIMARY KEY,\
                                           employer_name varchar(200) NOT NULL,\
                                           employer_url varchar(200) NOT NULL,\
                                           vacancies_url varchar(250) NOT NULL\
                                           );"

        create_vacancy = "CREATE TABLE vacancies (\
                                           vacancy_id int UNIQUE PRIMARY KEY,\
                                           vacancy_name varchar(200) NOT NULL,\
                                           vacancy_url varchar(200) NOT NULL,\
                                           salary int,\
                                           employer_id int REFERENCES employers(employer_id),\
                                           requirements text\
                                           );"

        with conn.cursor() as cur:
            cur.execute(create_employers)
            cur.execute(create_vacancy)

        conn.commit()
        conn.close()

    def save_data_to_database(self, data: list[dict[str, Any]]) -> None:

        """Сохранение данных о работодателях и вакансиях в базу данных."""

        conn = psycopg2.connect(dbname=self.database_name, **self.params)

        with conn.cursor() as cur:
            for employer in data:
                empr_data = employer['employer']
                cur.execute(
                    """
                    INSERT INTO employers (employer_id, employer_name, employer_url, vacancies_url)
                    VALUES (%s, %s, %s, %s)                    
                    """,
                    (empr_data['id'], empr_data['name'], empr_data['site_url'],empr_data['vacancies_url'])
                )


                vacancyes_data = employer['vacancies']
                for vacancy in vacancyes_data:
                    vacy_data = vacancy

                    salary_from = 0
                    if vacy_data['salary'] is not None:
                        if vacy_data['salary']['from'] is not None:
                            salary_from = vacy_data.get('salary', {}).get('from', '0')

                    if salary_from > 0:#добавляем в БД вакансии только с указанной мин зарплатой
                        cur.execute(
                            """
                            INSERT INTO vacancies (vacancy_id, vacancy_name, vacancy_url, salary, employer_id, requirements)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """,
                            (vacy_data['id'], vacy_data['name'], vacy_data['url'], salary_from,
                            vacy_data['employer']['id'], vacy_data['snippet']['requirement'])
                        )

        conn.commit()
        conn.close()



    def get_companies_and_vacancies_count(self):
        '''
        получает список всех компаний и количество вакансий у каждой компании
        '''
        with psycopg2.connect(dbname=self.database_name, **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT employer_id, employer_name, COUNT(*) AS vacancies_count FROM vacancies RIGHT "
                            "JOIN employers USING(employer_id) GROUP BY employer_id;")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_all_vacancies(self):
        '''
        получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию
        '''
        with psycopg2.connect(dbname=self.database_name, **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT  vacancy_id, vacancy_name, requirements, vacancy_url, salary, employer_name AS "
                    "company FROM vacancies JOIN employers USING(employer_id);")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_avg_salary(self):
        '''
        получает среднюю зарплату по вакансиям.
        '''
        with psycopg2.connect(dbname=self.database_name, **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT AVG(salary) as avg_salary FROM vacancies JOIN employers USING(employer_id);")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_vacancies_with_higher_salary(self):
        '''
        получает список всех вакансий, у которых зарплата выше средней по всем вакансиям
        '''
        with psycopg2.connect(dbname=self.database_name, **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT * FROM vacancies WHERE salary > (SELECT AVG(salary) FROM vacancies JOIN employers USING("
                    "employer_id));")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

    def get_vacancies_with_keyword(self, keyword: str):
        '''
        получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python
        '''
        with psycopg2.connect(dbname=self.database_name, **self.params) as conn:
            with conn.cursor() as cur:
                cur.execute(f" SELECT * FROM vacancies WHERE vacancy_name ILIKE \'%{keyword}%\' ;")
                rows = cur.fetchall()
                for row in rows:
                    print(row)

