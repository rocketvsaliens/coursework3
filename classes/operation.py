from datetime import datetime


class Operation:

    def __init__(self, operation: dict):
        self.__id = operation.get('id')
        self.__state = operation.get('state')
        self.__date = operation.get('date')
        self.__amount = operation.get('operationAmount')
        self.__description = operation.get('description')
        self.__from = operation.get('from')
        self.__to = operation.get('to')

    def __repr__(self):
        return f"{self.__class__.__name__}(" \
               f"id={self.__id}," \
               f"state=\"{self.__state}\"," \
               f"date=\"{self.__date}\"," \
               f"operation_amount={self.__amount}," \
               f"description=\"{self.__description}\"," \
               f"from=\"{self.__from}\"," \
               f"to=\"{self.__to}\")"

    @staticmethod
    def mask_number(number: str) -> str:
        """ Функция маскировки номера карты или счёта"""
        if len(number) == 16:
            number_hide = number[:6] + "*" * 6 + number[12:]
            return " ".join([number_hide[i:i + 4] for i in range(0, len(number_hide), 4)])
        elif len(number) == 20:
            return number.replace(number[:-4], "**")
        return 'Некорректный номер счёта или карты'

    @staticmethod
    def get_account_info(account: str) -> str:
        """
        Функция разбивки строки для корректной маскировки номера карты или счёта.
        Возвращает строку вида <название карты><замаскированный номер> или <счёт><замаскированный номер>.
        В случае отсутствия информации возвращает 'Неизвестно'
        """
        if account is not None:
            data_split = account.split()
            card_name = data_split[:-1]
            card_number = data_split[-1]
            return f'{" ".join(card_name)} {Operation.mask_number(card_number)}'
        else:
            return 'Неизвестно'

    def get_date(self) -> str:
        """Представление даты в понятном человекам формате"""
        try:
            date = datetime.strptime(self.__date, '%Y-%m-%dT%H:%M:%S.%f')
            return date.strftime('%d.%m.%Y')
        except ValueError:
            return "Некорректная дата"

    def get_description(self) -> str:
        """Получаем описание платежа"""
        return self.__description

    def get_from(self) -> str:
        """Получаем номер карты или счёт отправителя"""
        return self.__from

    def get_to(self) -> str:
        """Получаем номер карты или счёт получателя"""
        return self.__to

    def create_amount(self) -> str:
        """Получаем сумму платежа в формате <сумма платежа><валюта платежа>"""
        match self.__amount:
            case {'amount': amount, 'currency': {'name': name}}:
                return f"{amount} {name}"
            case _:
                return 'Неизвестная сумма или валюта платежа'
