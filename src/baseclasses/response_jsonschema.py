from jsonschema import validate
from src.enums.global_enums import GlobalErrorMessages


class ResponseJsonSchema:
    # конструктор класса
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.response_status = response.status_code

    def validate(self, schema):
        # если у нас список то пробегаем по нему циклом
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)

    def assert_status_code(self, status_code):
        if isinstance(self.response_status, list):
            assert self.response_status in status_code, f'Actual result: {self.response_status}' #GlobalErrorMessages.WRONG_STATUS_CODE.value
        else:
            assert self.response_status == status_code, f'Actual result: {self.response_status}' #GlobalErrorMessages.WRONG_STATUS_CODE.value
        return self
