def get_executed(operations: list) -> list:
    """
    Возвращает только ВЫПОЛНЕННЫЕ транзакции
    """
    return [operation for operation in operations
            if operation.get('state') == 'EXECUTED']


def sort_operations(operations: list) -> list:
    """
    Сортирует выполненные транзакции по дате
    """
    return sorted(get_executed(operations),
                  key=lambda x: x['date'], reverse=True)


