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
    """Тестируем пустой список"""
    assert handler.get_executed([]) == []


def test_get_executed(not_executed):
    """Тестируем список без выполненных операций"""
    assert handler.get_executed(not_executed) == []


def test_sort_operations_executed(executed):
    """Тестируем список с выполненными операциями"""
    expected_result = [
        {'date': '2022-01-02', 'state': 'EXECUTED'},
        {'date': '2022-01-01', 'state': 'EXECUTED'}
    ]
    assert handler.get_executed(executed) == expected_result
