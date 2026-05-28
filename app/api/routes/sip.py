from fastapi import APIRouter
from app.models.sip_model import SIPCalculator

router = APIRouter()


# SIP CALCULATOR API
@router.post("/calculate")
def calculate_sip(data: SIPCalculator):

    monthly_rate = data.annual_return_rate / 12 / 100

    months = data.investment_years * 12

    maturity_amount = (
        data.monthly_investment *
        (((1 + monthly_rate) ** months - 1) / monthly_rate) *
        (1 + monthly_rate)
    )

    invested_amount = data.monthly_investment * months

    estimated_returns = maturity_amount - invested_amount

    return {
        "success": True,
        "monthly_investment": data.monthly_investment,
        "invested_amount": round(invested_amount, 2),
        "estimated_returns": round(estimated_returns, 2),
        "maturity_amount": round(maturity_amount, 2)
    }