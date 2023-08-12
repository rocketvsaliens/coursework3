def get_executed(operations: list) -> list:
    """
    Returns only EXECUTED transactions
    """
    return [operation for operation in operations
            if operation.get('state') == 'EXECUTED']


def sort_operations(operations: list) -> list:
    """
    Returns transactions sorted by date
    """
    return sorted(get_executed(operations),
                  key=lambda x: x['date'], reverse=True)


