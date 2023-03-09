# from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class ResponsePydantic:
    """
    Полезный класс, который помогает нам экономить тонны кода в процессе
    валидации данных. На вход он принимает объект респонса и разбирает его.
    Можно добавить кучу различных методов в этом классе, которые нужны
    в работе с данными после их получения.
    It's useful class that helps to save a lot of code during validatio
    process in our tests. It receives response object and gets from it all
    values that should be validated. You can add additional methods into the
    Class if it needs for your project testing.
    """

    # конструктор класса
    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code
        self.parsed_object = None

    def validate(self, schema):
        # если у нас список то пробегаем по нему циклом
        if isinstance(self.response_json, list):
            for item in self.response_json:
                parsed_object = schema.parse_obj(item)
                self.parsed_object = parsed_object
        else:
            schema.parse_obj(self.response_json)
        return self

    def assert_status_code(self, status_code):
        """
        Метод для валидации статус кода. Из объекта респонса,
        который мы получили, мы берём статус и сравнимаем с тем, который
        нам был передан как параметр.
        Method for status code validation. It compares value from response
        object and compare it with received value from method params.
        """
        if isinstance(self.response_status, list):
            # assert self.response_status in status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
            assert self.response_status in status_code, self

        else:
            # assert self.response_status == status_code, GlobalErrorMessages.WRONG_STATUS_CODE.value
            assert self.response_status == status_code, self

        return self

    def get_parsed_object(self):
        return self.parsed_object

    def __str__(self):
        """
        Метод отвечает за строковое представление нашего объекта. Что весьма
        удобно, ведь в случае срабатывания валидации, мы получаем полную картину
        всего происходящего и все параметры которые нам нужны для определения
        ошибки.
         Method for string displaying of class instance. In case when our
         validation will be failed, we will get full information about our
         object and comparation data, that will help us in fail investigation.
        """
        return (
            f'\n Status code: {self.response_status}'
            f'\n Requested url: {self.response.url}'
            f'\n Response body: {self.response_json}'
        )
