import pytest

from src.head_hunter_api import HeadHunrterApi


@pytest.fixture
def class_hh_api1():
    return HeadHunrterApi()


@pytest.fixture
def class_hh_api2():
    return HeadHunrterApi()


def test_init(class_hh_api1):
    assert class_hh_api1.base_url == 'https://api.hh.ru'


