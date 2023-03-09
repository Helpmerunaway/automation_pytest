import pytest
import requests

from configuration import GO_REST_URL
from src.baseclasses.response_pydantic import ResponsePydantic
from src.pydantic_schemas.user import User
from src.pydantic_schemas.computer import Computer
from example import computer

# resp = requests.get(GO_REST_URL)
# print(resp.__getstate__())
# print(resp.url)


def test_get_users_list(get_users, calculate):
    """
        Пример использования фикстуры которая отправляет запрос и возвращает
        респонс. Далее мы просто обрабатываем его с помощью нашего Response class
        применяя все доступные валидации.

        Example of using fixture that requesting server and returns raw response
        object. After it we put that data into our response class and accept all
        possible validation methods.
        """
    ResponsePydantic(get_users).assert_status_code(200).validate(User)
    print(calculate) # сама функция <function _calculate at 0x0000011DB8471120>
    print(calculate(1, 1)) # результат функции calculate исходя из введенных данных


def test_get_users_list_sec(get_users, make_number):
    ResponsePydantic(get_users).assert_status_code(200).validate(User)
    print(make_number)

# endpoint /users с разными методами
# /users -> [GET, POST, PUT, DELETE]


@pytest.mark.develop
@pytest.mark.prod
@pytest.mark.skip('[ISSUE-23412] Issue with network connection')
def test_another():
    """
    Обычный тест, но не совсем. Обратите внимание на декораторы к нему.
    Мы скипаем его с определённым сообщением, а так же помечаем с каким скоупом
    его выполнять.

    It is just common test. Please check decorators of the test. Here is you
    can find decorator for skip test with some message and useful tags for
    case when you need to run some scope of tests.
    """
    assert 1 == 2


def test_calculation_both_negative(calculate):
    print(calculate(-1, -2))


def test_calculation_one_negative(calculate):
    print(calculate(-1, 2))


def test_calculation_both_positive(calculate):
    print(calculate(-1, 2))


def test_calculation_one_char(calculate):
    print(calculate('b', 2))


def test_calculation_two_char(calculate):
    print(calculate('b', 'b'))


@pytest.mark.develop
@pytest.mark.parametrize('first_value, second_value, result', [
    (1, 2, 3),
    (-1, -2, -3),
    (-1, 2, 1),
    ('b', -2, None),
    ('b', 'b', None)
])
def test_calculator(first_value, second_value, result, calculate):
    """
    Вариант параметризации нашего теста, с несколькими параметрами за один
    раз.

    Example of parametrization, when during one iteration should be passed
    more than one value.
    """
    assert calculate(first_value, second_value) == result


@pytest.mark.develop
@pytest.mark.prod
@pytest.mark.xfail(reason='[ISSUE-23413] Wrong conditions')
def test_one_is_equal_two():
    """
    In this test-case we try to check that 1 is equal 2
    :return:
    """
    assert 1 == 2


def test_pydantic_object_computer():
    """
        Пример того, как после инициализации pydantic объекта, можно получить
        доступ к любому из его параметров.
        Example for case, when after initialization your JSON as a pydantic object
        you can get access to all parameters.
    """
    comp = Computer.parse_obj(computer)
    print('JsonSchema File:', comp.schema_json())
    print('Photo - Host:', comp.detailed_info.physical.photo.host)
    print('Photo - Color as hex:', comp.detailed_info.physical.color.as_hex())
    print('Photo - Color as rgb:', comp.detailed_info.physical.color.as_rgb())

