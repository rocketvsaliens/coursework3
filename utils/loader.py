import json


def load_data_from_file(path: str):
    """
    Loads json data from source
    :param path: file destination
    :return: list with dicts
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return 'Файл не найден'
