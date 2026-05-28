from pydantic import BaseModel
from enum import Enum


class MutualFundType(str, Enum):

    sip_investment = "sip_investment"
    tax_saving = "tax_saving"
    wealth_management = "wealth_management"
    mutual_fund_services = "mutual_fund_services"


class MutualFundInquiry(BaseModel):

    name: str
    email: str
    phone: str
    investment_type: MutualFundType
    monthly_investment: str
    message: str