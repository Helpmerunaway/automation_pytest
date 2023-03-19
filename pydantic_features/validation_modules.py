"""
Python modules

1. Cerberus (Schema, Voluptuous)

2. Marshmallow

3. Pydantic
"""

# 1 Cerberus
class Cerberus:
    from dataclasses import dataclass


    @dataclass
    class User1:
        external_uuid: str
        name: str

    import json
    from cerberus import Validator

    user = Validator(
        {
            'name': {'type': 'string'},
            'external_uuid': {'type': 'string'}
        }
    )

    user.validate(json.loads(request_data))  # True

    """
    Cerberus Results:
    ✅ Validate data
    ❌ Another Language
    ❌ Complex data structures need complex schemas
    ❌ Senior YAML developer
    ❌ Validation only, can't get class instances easily
    """

# 2 Marshmallow
class Marshmallow:
    from dataclasses import dataclass

    @dataclass
    class User2:
        external_uuid: str
        name: str


    from marshmallow import Schema

    class User:
        def __init__(self, external_uuid, name):
            self.external_uuid = external_uuid
            self.name = name

    class UserSchema(Schema):
        external_uuid = fields.Str()
        name = fields.Str()

        @post_load
        def make_user(self, data, **kwargs):
            return User(**data)

    class UserGroupSchema(Schema):
        group_name = fields.String()
        users = fields.Nested(UserSchema, many=True)

    user_schema = UserSchema

    """
    Marshmallow Results:
    ✅Class-like description
    ✅No need to learn data types
    ✅Can produce instances
    ✅Complex data structures made simple
    ❌ Writing 2 classes if we need instances
    """

# 3 Pydantic
class Pydantic:
    from pydantic.dataclasses import dataclass

    @dataclass
    class User3:
        external_uuid: str
        name: str

    from pydantic import BaseModel

    class User(BaseModel):
        external_uuid: UUID
        name: str
    @dataclass
    class Users3Group:
        group_name: str
        users: List[User3]

    request_data = '{"external__uuid": "dickbutt", ' \
                    '"name": "Gill Bates"}'

    user = User3.parse_raw(request_data)

    user1 = {'external__uuid': "1337",
                    'name': "Jaime Lannister"}
    user2 = {'external__uuid': "1338",
                    'name': "Cersei Lannister"}
    data = {
        'group_name': 'loving_family',
        'users': [user1, user2]
    }

    users_group = Users3Group(**data)
#   UsersGroup(
#         group_name = 'loving_family',
#         users=[
#             User3(external_uuid='1337', name='Jaime Lannister'),
#             User3(external_uuid='1338', name='Cersei Lannister')
#         ]
# )


    """
    Pydantic Results:
    ✅Class-like description
    ✅Python data types
    ✅Dont need another class
    ✅Modern syntax (dataclass)
    ✅Complex data types
    ✅Validate: 
    str, bool, int, float, bytes
    dict, set, list, ...
    typing.*
    enum, decimal, datetime, pathlib, uuid, ...
    IPvAnyAddress
    EmailStr
    AnyUrl, AnyHttpUrl
    PaymentCardNumber
    Json
    """
