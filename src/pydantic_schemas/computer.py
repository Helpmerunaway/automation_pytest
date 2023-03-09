from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from src.enums.user_enums import Statuses
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from pydantic.networks import IPv4Address, IPv6Address
from src.pydantic_schemas.physical import Physical
from src.pydantic_schemas.owners import Owners
from src.pydantic_schemas.detailed_info import DetailedInfo
from example import computer


class Computer(BaseModel):
    id: int
    status: Statuses
    activated_at: PastDate
    expiration_at: FutureDate
    host_v4: IPv4Address
    host_v6: IPv6Address
    detailed_info: DetailedInfo


comp = Computer.parse_obj(computer)
print(comp)