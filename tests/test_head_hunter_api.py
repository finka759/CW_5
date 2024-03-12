import pytest

from src.head_hunter_api import HeadHunrterApi


@pytest.fixture
def class_head_hunter_api():
    return HeadHunrterApi()


def test___init__(class_head_hunter_api):
    assert class_head_hunter_api.base_url == 'https://api.hh.ru'
