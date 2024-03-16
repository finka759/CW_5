import pytest

from src.json_saver import JsonSaver


@pytest.fixture
def json_saver1():
    return JsonSaver()


@pytest.fixture
def json_saver2():
    return JsonSaver()


def test___init__(json_saver1):
    assert json_saver1.way_to_json == '..\\data\\hh_data.json'
