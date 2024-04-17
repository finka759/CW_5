from typing import Any

import psycopg2


class DBManager:
    @staticmethod
    def create_database(database_name: str, params: dict) -> None:
        conn = psycopg2.connect(dbname='postgres', **params)
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"DROP DATABASE IF EXISTS {database_name}")
        cur.execute(f"CREATE DATABASE {database_name}")

        conn.close()
        conn = psycopg2.connect(dbname=database_name, **params)

        create_employers = "CREATE TABLE employers (\
                                           employer_id int UNIQUE PRIMARY KEY,\
                                           name varchar(200) NOT NULL,\
                                           url varchar(200) NOT NULL,\
                                           vacancies_url varchar(250) NOT NULL\
                                           );"

        create_vacancy = "CREATE TABLE vacancies (\
                                           vacancy_id int UNIQUE PRIMARY KEY,\
                                           name varchar(200) NOT NULL,\
                                           url varchar(200) NOT NULL,\
                                           salary int,\
                                           employer_id int REFERENCES employers(employer_id),\
                                           requirements text\
                                           );"

        with conn.cursor() as cur:
            cur.execute(create_employers)
            cur.execute(create_vacancy)

        conn.commit()
        conn.close()

    @staticmethod
    def save_data_to_database(data: list[dict[str, Any]], db_name: str, params: dict) -> None:

        """Сохранение данных о работодателях и вакансиях в базу данных."""

        conn = psycopg2.connect(dbname=db_name, **params)

        with conn.cursor() as cur:
            for employer in data:
                empr_data = employer['employer']
                cur.execute(
                    """
                    INSERT INTO employers (employer_id, name, url, vacancies_url)
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

                    if salary_from > 0:#добавляем в БД вакансии с указанной мин зарплатой
                        cur.execute(
                            """
                            INSERT INTO vacancies (vacancy_id, name, url, salary, employer_id, requirements)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """,
                            (vacy_data['id'], vacy_data['name'], vacy_data['url'], salary_from,
                            vacy_data['employer']['id'], vacy_data['snippet']['requirement'])
                        )

        conn.commit()
        conn.close()
