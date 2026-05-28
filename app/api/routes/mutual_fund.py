from fastapi import APIRouter
from app.models.mutual_fund_model import MutualFundInquiry
from app.core.database import supabase

router = APIRouter()


# MUTUAL FUND INQUIRY API
@router.post("/apply")
def apply_mutual_fund(data: MutualFundInquiry):

    mutual_fund_data = {
        "name": data.name,
        "email": data.email,
        "phone": data.phone,
        "investment_type": data.investment_type,
        "monthly_investment": data.monthly_investment,
        "message": data.message,
        "status": "new",
        "source": "mutual_fund"
    }

    supabase.table("mutual_fund_leads").insert(mutual_fund_data).execute()

    return {
        "success": True,
        "message": "Mutual fund inquiry submitted successfully"
    }


# GET ALL MUTUAL FUND TYPES
@router.get("/types")
def get_mutual_fund_types():

    return {
        "success": True,
        "types": [

            {
                "name": "Equity Funds",
                "value": "equity_funds"
            },

            {
                "name": "SIP Investment",
                "value": "sip_investment"
            },

            {
                "name": "ELSS Tax Saver",
                "value": "elss_tax_saver"
            },

            {
                "name": "Debt Funds",
                "value": "debt_funds"
            },

            {
                "name": "NPS",
                "value": "nps"
            },

            {
                "name": "Wealth Management",
                "value": "wealth_management"
            }

        ]
    }