from fastapi import APIRouter
from app.core.database import supabase
from app.models.admin_model import UpdateLeadStatus

router = APIRouter()


# GET ALL LEADS
@router.get("/leads")
def get_all_leads():

    data = (
        supabase
        .table("leads")
        .select("*")
        .execute()
    )

    return {
        "success": True,
        "data": data.data
    }


# UPDATE LEAD STATUS
@router.put("/leads/{id}")
def update_lead_status(
    id: int,
    lead: UpdateLeadStatus
):

    data = (
        supabase
        .table("leads")
        .update({
            "status": lead.status
        })
        .eq("id", id)
        .execute()
    )

    return {
        "success": True,
        "message": "Lead status updated successfully",
        "data": data.data
    }