import pytest

from src.vacancy import Vacancy


@pytest.fixture
def class_vacancy1():
    return Vacancy("1", "vacancy1_name", "https://api.hh.ru/vacancy1",
                   "2024-03-12T16:41:33+0301", 10000,  '1', 'Москва')


@pytest.fixture
def class_vacancy2():
    return Vacancy("2", "vacancy2_name", "https://api.hh.ru/vacancy2",
                   "2024-03-12T16:41:33+0302", 20000, '2', 'Санкт-Петербург')


def test_vacancy_init(class_vacancy1):
    assert class_vacancy1.vacancy_id == "1"
    assert class_vacancy1.name == "vacancy1_name"
    assert class_vacancy1.alternate_url == "https://api.hh.ru/vacancy1"
    assert class_vacancy1.published_at == "2024-03-12T16:41:33+0301"
    assert class_vacancy1.salary_from == 10000


def test___str__(class_vacancy1):
    assert str(class_vacancy1) == ('id выкансии - 1\nМин.зарплата - 10000\nСсылка - https://api.hh.ru/vacancy1\n'
                                   'Опубликована - 2024-03-12T16:41:33+0301\nРегион - Москва (id - 1)\n')


def test___lt__(class_vacancy1, class_vacancy2):
    assert (class_vacancy1 > class_vacancy2) is True
