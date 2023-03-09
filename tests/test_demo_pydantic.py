import requests
from configuration import SERVICE_URL
from jsonschema import validate
from src.baseclasses.response_pydantic import ResponsePydantic
from src.pydantic_schemas.post_pydantic import Post


def test_getting_posts_version_two():
    r = requests.get(url=SERVICE_URL)
    response = ResponsePydantic(r)
    response.assert_status_code(200).validate(Post)