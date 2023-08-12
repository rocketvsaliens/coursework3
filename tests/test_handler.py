import pytest
from utils import handler


@pytest.fixture
def not_executed():
    return [
        {'date': '2022-01-01', 'state': 'PENDING'},
        {'date': '2022-01-02', 'state': 'APPROVED'},
        {'date': '2022-01-03', 'state': 'CANCELLED'}
    ]


@pytest.fixture
def executed():
    return [
        {'date': '2022-01-01', 'state': 'EXECUTED'},
        {'date': '2022-01-03', 'state': 'CANCELLED'},
        {'date': '2022-01-02', 'state': 'EXECUTED'}
    ]


def test_sort_operations_empty_list():
    assert handler.sort_operations([]) == []


def test_get_executed(not_executed):
    assert handler.get_executed(not_executed) == []


def test_sort_operations_executed(executed):
    expected_result = [
        {'date': '2022-01-02', 'state': 'EXECUTED'},
        {'date': '2022-01-01', 'state': 'EXECUTED'}
    ]
    assert handler.sort_operations(executed) == expected_result