from enum import Enum
from src.baseclasses.pyenum import PyEnum

"""
Один из тысяч файлов ENUM которые будут  в проекте. 
Нужны они для того, чтобы упростить поддержку проекта и упростить
фикс самых простых изменений, которые могли бы занять у вас много времени.
It is one of billion ENUM files in your project.
They will help you in your project support and error fixing.
"""


class Genders(Enum):
    """
    Класс для хранения пола пользователя.
    Example of gender enum.
    """
    female = 'female'
    male = 'male'


class Statuses(PyEnum):
    """
    Вариант хранения всех возможных статусов пользователя.
    Example of status enums.
    """
    ACTIVE = "ACTIVE"
    BANNED = "BANNED"
    DELETED = "DELETED"
    INACTIVE = "INACTIVE"


class UserErrors(Enum):
    """
    Enum с кастомными ошибками для какого-то конкретной сущности или
    тестируемого ендпоинта.
    Enum with custom errors, for some difficult cases or testing endpoint.
    """
    WRONG_EMAIL = "Email doesn't contain @"


print(Statuses.list())