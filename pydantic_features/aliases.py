from pydantic import BaseModel
from pydantic import schema

class User(BaseModel):
    name: str = schema(
                    ...,
                    alias='AbstractUserAbstractNameFabricValue')

data = '{"AbstractUserAbstractNameFabricValue:": "Hodor"}'

User.parse_raw(data)