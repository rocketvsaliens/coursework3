import pytest
from utils import loader


@pytest.fixture
def sample_data():
    return [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
             'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
             'to': 'Счет 64686473678894779589'},
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364',
             'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758',
             'to': 'Счет 35383033474447895560'}]


def test_load_data_from_file(sample_data):
    data = loader.load_data_from_file('tests/test_data.json')
    non_existing_file = loader.load_data_from_file("non_existing.json")
    assert data == sample_data
    assert non_existing_file == 'Файл не найден'
