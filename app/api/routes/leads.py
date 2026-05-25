from fastapi import APIRouter
from app.models.lead_model import CreateLead
from app.core.database import supabase

router = APIRouter()


# CREATE LEAD API
@router.post("/")
def create_lead(lead: CreateLead):

    data = {
        "name": lead.name,
        "email": lead.email,
        "phone": lead.phone,
        "loan_type": lead.loan_type,
        "amount": lead.amount,
        "source": lead.source
    }

    supabase.table("leads").insert(data).execute()

    return {
        "success": True,
        "message": "Lead created successfully"
    }