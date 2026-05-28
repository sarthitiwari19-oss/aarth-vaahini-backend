from pydantic import BaseModel


class ContactInquiry(BaseModel):

    name: str
    email: str
    phone: str
    message: str