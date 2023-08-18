def decorator_sort_get_executed(func):
    """
    Сортирует выполненные транзакции по дате
    """

    def wrapper(*args, **kwargs):
        return sorted(func(*args, **kwargs), key=lambda x: x['date'], reverse=True)

    return wrapper


@decorator_sort_get_executed
def get_executed(operations: list) -> list:
    """
    Возвращает только ВЫПОЛНЕННЫЕ транзакции
    """
    return [operation for operation in operations
            if operation.get('state') == 'EXECUTED']
