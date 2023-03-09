from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber
from src.pydantic_schemas.physical import Physical
from src.pydantic_schemas.owners import Owners


class DetailedInfo(BaseModel):
    physical: Physical
    owners: List[Owners]