import pytest

from classes import operation


@pytest.mark.parametrize("number, expected_result", [
    ("1234567890654321", "1234 56** **** 4321"),
    ("12345678901234567890", "**7890"),
    ("12345", "Некорректный номер счёта или карты")
])
def test_mask_number(number, expected_result):
    """Проверяем, что функция правильно маскирует номер"""
    assert operation.Operation.mask_number(number) == expected_result


@pytest.mark.parametrize("account, expected_result", [
    ("Счет 12345678901234567890", "Счет **7890"),
    ("МИР 9876543210987654", "МИР 9876 54** **** 7654"),
    (None, "Неизвестно")
])
def test_get_account_info(account, expected_result):
    """Проверяем, что функция правильно форматирует информацию о счете или карте"""
    assert operation.Operation.get_account_info(account) == expected_result


@pytest.fixture
def instance():
    """Создаем экземпляр класса перед каждым тестом"""
    transaction = {'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
                   'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                   'description': 'Перевод организации', 'from': 'Maestro 1596837868705199',
                   'to': 'Счет 64686473678894779589'}
    return operation.Operation(transaction)


def test_repr(instance):
    """Проверяем, что вывод __repr__ соответствует экземпляру класса"""
    expected_result = 'Operation(id=441945886,state="EXECUTED",date="2019-08-26T10:50:58.294041",' \
                      'operation_amount={\'amount\': \'31957.58\', \'currency\': {\'name\': \'руб.\', \'code\': \'RUB\'}},' \
                      'description="Перевод организации",from="Maestro 1596837868705199",to="Счет 64686473678894779589")'
    assert str(instance) == expected_result


def test_get_date_valid_format(instance):
    """Проверяем, что функция правильно возвращает дату в формате "дд.мм.гггг" для корректной строки даты"""
    instance._Operation__date = '2022-01-01T12:34:56.789'
    assert instance.get_date() == '01.01.2022'


def test_get_date_invalid_format(instance):
    """Проверяем, что функция возвращает "Некорректная дата" для некорректной строки даты"""
    instance._Operation__date = '2022-01-01'
    assert instance.get_date() == 'Некорректная дата'


def test_get_description(instance):
    """Проверяем корректное описание"""
    assert instance.get_description() == instance._Operation__description


def test_get_from(instance):
    """Проверяем правильное получение отправителя"""
    assert instance.get_from() == instance._Operation__from


def test_get_to(instance):
    """Проверяем правильное получение получателя"""
    assert instance.get_to() == instance._Operation__to


def test_create_amount_valid(instance):
    """Проверяем, что функция правильно форматирует сумму и валюту для корректного словаря"""
    instance._Operation__amount = {'amount': 100.0, 'currency': {'name': 'USD'}}
    assert instance.create_amount() == '100.0 USD'


def test_create_amount_invalid(instance):
    """Проверяем, что функция возвращает 'Неизвестная сумма' для некорректного словаря"""
    instance._Operation__amount = {'invalid_key': 100.0}
    assert instance.create_amount() == 'Неизвестная сумма или валюта платежа'
