from pydantic import BaseModel


class EMICalculator(BaseModel):
    loan_amount: float
    interest_rate: float
    tenure_years: int
