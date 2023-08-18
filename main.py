from utils import loader, handler
from classes import operation
from config import JSON_DATA_PATH, NUMBER_OF_TRANSACTIONS_TO_SHOW


def main():
    """
    Основная функция вывода на экран последних выполненных транзакций вида:
    <дата перевода><описание перевода>
    <откуда><куда>
    <сумма перевода><валюта>
    """
    # собираем все операции
    operations = loader.load_data_from_file(JSON_DATA_PATH)
    # выбираем и сортируем по дате N последних выполненных транзакций
    last_operations = handler.get_executed(operations)[:NUMBER_OF_TRANSACTIONS_TO_SHOW]

    # создаём экземпляры класса из последних выполненных операций
    transactions = [operation.Operation(i) for i in last_operations]

    # выводим последние выполненные транзакции на экран
    for one_transaction in transactions:
        print(one_transaction.create_payment())


if __name__ == '__main__':
    main()
