from pydantic import BaseModel, HttpUrl, UUID4, EmailStr
from pydantic.types import PastDate, FutureDate, List, PaymentCardNumber


class Owners(BaseModel):
    name: str
    card_number: PaymentCardNumber
    email: EmailStr