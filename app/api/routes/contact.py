from fastapi import APIRouter
from app.models.contact_model import ContactInquiry
from app.core.database import supabase

router = APIRouter()


# CONTACT API
@router.post("/")
def contact_us(data: ContactInquiry):

    contact_data = {
        "name": data.name,
        "email": data.email,
        "phone": data.phone,
        "message": data.message
    }

    supabase.table("contact_leads").insert(contact_data).execute()

    return {
        "success": True,
        "message": "Contact inquiry submitted successfully"
    }