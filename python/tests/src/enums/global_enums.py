from enum import Enum


class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Полученный статус-код страницы не равен ожидаемому'
    WRONG_ELEMENT_COUNT = 'Полученное количество элементов не соответствует ожидаемому'
    WRONG_URL_STATUS = 'Полученный статус-код не равен ожидаемому'
