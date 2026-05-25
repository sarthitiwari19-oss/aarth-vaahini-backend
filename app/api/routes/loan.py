from fastapi import APIRouter
from app.models.loan_model import LoanApplication
from app.core.database import supabase

router = APIRouter()


# LOAN APPLY API
@router.post("/apply")
def apply_loan(data: LoanApplication):

    loan_data = {
        "name": data.name,
        "email": data.email,
        "phone": data.phone,
        "loan_type": data.loan_type,
        "amount": data.amount,
        "monthly_income": data.monthly_income,
        "employment_type": data.employment_type,
        "status": "new",
        "source": "loan_apply"
    }

    supabase.table("leads").insert(loan_data).execute()

    return {
        "success": True,
        "message": "Loan application submitted successfully"
    }