from pydantic import BaseModel


class CIBILCheck(BaseModel):
    name: str
    pan_number: str
    phone: str
    email: str