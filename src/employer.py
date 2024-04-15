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
            # top_employers.append(Employer(vacancies_list[count].employer_id, vacancies_list[count].employer_name))
            if Employer(vacancies_list[count].employer_id, vacancies_list[count].employer_name) not in top_employers:
                top_employers.append(Employer(vacancies_list[count].employer_id, vacancies_list[count].employer_name))
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

    def __init__(self, employer_id: str, name: str):
        self.employer_id = employer_id
        self.name = name

    def __str__(self):
        return (f"Работодатель - {self.name} (id - {self.employer_id})\n")