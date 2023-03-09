import requests
from configuration import SERVICE_URL
from jsonschema import validate
from src.json_schemas.post_jsonschema import POST_SCHEMA
from src.baseclasses.response_jsonschema import ResponseJsonSchema


def test_getting_posts_version_one():
    response = requests.get(url=SERVICE_URL)
    received_posts = response.json()
    print('RESPONSE:', received_posts)
    assert response.status_code == 200
    #assert len(received_posts) == 3, GlobalErrorMessages.WRONG_ELEMENT_COUNT.value
    # валидируем каждый айтем из массива данных
    for item in received_posts:
        validate(item, POST_SCHEMA)

# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]


def test_getting_posts_version_two():
    r = requests.get(url=SERVICE_URL)
    response = ResponseJsonSchema(r)
    response.assert_status_code(200).validate(POST_SCHEMA)

