from fastapi import APIRouter, Depends
from app.core.database import supabase
from app.models.admin_model import UpdateLeadStatus
from app.core.admin_auth import verify_admin_token

router = APIRouter()


# GET ALL LEADS
@router.get(
    "/leads",
    dependencies=[Depends(verify_admin_token)]
)
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
@router.put(
    "/leads/{id}",
    dependencies=[Depends(verify_admin_token)]
)
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


# GET ALL CONTACT LEADS
@router.get(
    "/contact-leads",
    dependencies=[Depends(verify_admin_token)]
)
def get_contact_leads():

    data = (
        supabase
        .table("contact_leads")
        .select("*")
        .execute()
    )

    return {
        "success": True,
        "data": data.data
    }


# GET ALL INSURANCE LEADS
@router.get(
    "/insurance-leads",
    dependencies=[Depends(verify_admin_token)]
)
def get_insurance_leads():

    data = (
        supabase
        .table("insurance_leads")
        .select("*")
        .execute()
    )

    return {
        "success": True,
        "data": data.data
    }


# ADMIN DASHBOARD STATS
@router.get(
    "/stats",
    dependencies=[Depends(verify_admin_token)]
)
def get_dashboard_stats():

    leads = (
        supabase
        .table("leads")
        .select("*")
        .execute()
    )

    contacts = (
        supabase
        .table("contact_leads")
        .select("*")
        .execute()
    )

    insurance = (
        supabase
        .table("insurance_leads")
        .select("*")
        .execute()
    )

    return {
        "success": True,
        "total_leads": len(leads.data or []),
        "total_contacts": len(contacts.data or []),
        "total_insurance": len(insurance.data or [])
    }
# GET ALL MUTUAL FUND LEADS
@router.get(
    "/mutual-fund-leads",
    dependencies=[Depends(verify_admin_token)]
)
def get_mutual_fund_leads():

    data = (
        supabase
        .table("mutual_fund_leads")
        .select("*")
        .execute()
    )

    return {
        "success": True,
        "data": data.data
    }
