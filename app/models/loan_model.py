from pydantic import BaseModel
from enum import Enum


class LoanType(str, Enum):

    home_loan = "home_loan"
    personal_loan = "personal_loan"
    business_loan = "business_loan"
    education_loan = "education_loan"
    car_loan = "car_loan"
    gold_loan = "gold_loan"
    bike_loan = "bike_loan"
    travel_loan = "travel_loan"
    medical_loan = "medical_loan"
    lap = "lap"


class LoanApplication(BaseModel):

    name: str
    email: str
    phone: str
    loan_type: LoanType
    amount: str
    monthly_income: str
    employment_type: str