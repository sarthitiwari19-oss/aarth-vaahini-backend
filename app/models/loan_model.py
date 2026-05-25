from pydantic import BaseModel


class LoanApplication(BaseModel):
    name: str
    email: str
    phone: str
    loan_type: str
    amount: str
    monthly_income: str
    employment_type: str