from pydantic import BaseModel


class SIPCalculator(BaseModel):

    monthly_investment: float
    annual_return_rate: float
    investment_years: int