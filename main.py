from utils import loader, handler
from classes import operation
from config import JSON_DATA_PATH, NUMBER_OF_TRANSACTIONS_TO_SHOW


def main():
    operations = loader.load_data_from_file(JSON_DATA_PATH)
    last_operations = handler.sort_operations(operations)[:NUMBER_OF_TRANSACTIONS_TO_SHOW]

    transactions = [operation.Operation(i) for i in last_operations]

    for one_transaction in transactions:
        print(f'{one_transaction.get_date()} {one_transaction.get_description()}\n'
              f'{one_transaction.get_account_info(one_transaction.get_from())} -> '
              f'{one_transaction.get_account_info(one_transaction.get_to())}\n'
              f'{one_transaction.create_amount()}\n')


if __name__ == '__main__':
    main()
