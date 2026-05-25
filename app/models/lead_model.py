from pydantic import BaseModel


class CreateLead(BaseModel):
    name: str
    email: str
    phone: str
    loan_type: str
    amount: str
    source: str