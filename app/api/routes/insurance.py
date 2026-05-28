from fastapi import APIRouter
from app.models.insurance_model import InsuranceApplication
from app.core.database import supabase

router = APIRouter()


# INSURANCE APPLY API
@router.post("/apply")
def apply_insurance(data: InsuranceApplication):

    insurance_data = {
        "name": data.name,
        "email": data.email,
        "phone": data.phone,
        "insurance_type": data.insurance_type,
        "message": data.message,
        "status": "new",
        "source": "insurance"
    }

    supabase.table("insurance_leads").insert(insurance_data).execute()

    return {
        "success": True,
        "message": "Insurance inquiry submitted successfully"
    }