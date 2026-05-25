from fastapi import APIRouter
from app.models.emi_model import EMICalculator

router = APIRouter()


# EMI CALCULATOR API
@router.post("/calculate")
def calculate_emi(data: EMICalculator):

    P = data.loan_amount

    R = data.interest_rate / 12 / 100

    N = data.tenure_years * 12

    emi = (
        P * R * (1 + R) ** N
    ) / (
        (1 + R) ** N - 1
    )

    total_payment = emi * N

    total_interest = total_payment - P

    return {
        "success": True,
        "monthly_emi": round(emi, 2),
        "total_payment": round(total_payment, 2),
        "total_interest": round(total_interest, 2)
    }