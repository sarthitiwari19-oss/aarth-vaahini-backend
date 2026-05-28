from pydantic import BaseModel
from enum import Enum


class InsuranceType(str, Enum):

    life_insurance = "life_insurance"
    term_insurance = "term_insurance"
    health_insurance = "health_insurance"
    motor_insurance = "motor_insurance"
    business_insurance = "business_insurance"
    travel_insurance = "travel_insurance"


class InsuranceApplication(BaseModel):

    name: str
    email: str
    phone: str
    insurance_type: InsuranceType
    message: str