from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    # валидация при помощи встроенной функции Field
    id: int = Field(le=2)
    # id: int
    title: str
    # алиас для поля с нижним подчеркиванием
    # name: str = Field(alias='_name')
"""
    # аналог id: int = Field(le=2) - самописный валидатор если id > 2
    @validator("id")
    def check_that_id_is_less_than_two(cls, v):
        if v > 2:
            raise ValueError('Id is not less than two')
        else:
            return v
"""

# [{'id': 1, 'title': 'Post 1', '_name': "Igor"},