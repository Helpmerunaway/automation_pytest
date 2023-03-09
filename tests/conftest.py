import pytest
from src.generators.player_localization import PlayerLocalization
from src.generators.builder_player import Player
from random import randrange


@pytest.fixture()
def get_player_generator():
    """
       Пример фикстуры для инициализации объекта генератора и передачу его в
       тест.
       Fixture that initialize generator object and returns it into autotest.
    """
    return Player()

@pytest.fixture()
def get_number():
    """
    Просто метод для генерации рандомного числа :)
    Method that generates random number :)
    """
    return randrange(1, 1000, 5)


def _calculate(a, b):
    """
    Функция которая выполняет какую-то логику. При этом, ниже фикстура, которая
    отдаёт его в тест как объект, чтобы можно было применить там как
    именно как функцию.
    It is function that does some logic. Please check fixture below, that
    returns that function as object into autotest where you can call it as
    a common function and pass some param into it.
    """
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return None


@pytest.fixture()
def calculate():
    """
    Передача функции в тест используя фикстуру.
    Return function as an object into autotest.
    """
    return _calculate


@pytest.fixture()
def make_number():
    """
    Делаем какую-то логику, передаём управление тесту используя конструкцию
    yield и уже после того, как тест закончился, выполняем вторую часть кода.
    In that case we do some logic, than return number to autotest, wait till
    test has been passed and after it again do some logic.
    """
    print("I'm getting number")
    number = randrange(1, 1000, 5)
    yield number     # работает как return но с прерыванием на переключение контекста от теста к фикстуре
    print(f"Number at home {number}")