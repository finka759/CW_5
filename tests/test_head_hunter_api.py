import pytest

from src.head_hunter_api import HeadHunrterApi


@pytest.fixture
def class_hh_api1():
    return HeadHunrterApi()


@pytest.fixture
def class_hh_api2():
    return HeadHunrterApi('https://api.hh.ru')


def test___init__(class_hh_api2):
    assert class_hh_api2.base_url == 'https://api.hh.ru'


def test_get_vacancies(class_hh_api1):
    assert len(class_hh_api1.get_vacancies('python', 10000)) == 100
