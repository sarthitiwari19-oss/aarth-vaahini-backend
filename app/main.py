from fastapi import FastAPI
from app.core.database import supabase

# otp routes
from app.api.routes.otp import router as otp_router

# insurance routes
from app.api.routes.insurance import router as insurance_router

# contact routes
from app.api.routes.contact import router as contact_router

# loan routes
from app.api.routes.loan import router as loan_router

# cibil routes
from app.api.routes.cibil import router as cibil_router

# admin routes
from app.api.routes.admin import router as admin_router

# auth routes
from app.api.routes.auth import router as auth_router

# leads routes
from app.api.routes.leads import router as leads_router

# emi routes
from app.api.routes.emi import router as emi_router

# products routes
from app.api.routes.products import router as products_router

# mutual fund routes
from app.api.routes.mutual_fund import router as mutual_fund_router

# sip routes
from app.api.routes.sip import router as sip_router

app = FastAPI()

# SIP ROUTES
app.include_router(
    sip_router,
    prefix="/api/sip",
    tags=["SIP Calculator"]
)

# MUTUAL FUND ROUTES
app.include_router(
    mutual_fund_router,
    prefix="/api/mutual-fund",
    tags=["Mutual Fund"]
)

# PRODUCTS ROUTES
app.include_router(
    products_router,
    prefix="/api/products",
    tags=["Products"]
)


# OTP ROUTES
app.include_router(
    otp_router,
    prefix="/api/auth",
    tags=["OTP Auth"]
)


# INSURANCE ROUTES
app.include_router(
    insurance_router,
    prefix="/api/insurance",
    tags=["Insurance"]
)


# CONTACT ROUTES
app.include_router(
    contact_router,
    prefix="/api/contact",
    tags=["Contact"]
)


# LOAN ROUTES
app.include_router(
    loan_router,
    prefix="/api/loan",
    tags=["Loan"]
)


# CIBIL ROUTES
app.include_router(
    cibil_router,
    prefix="/api/cibil",
    tags=["CIBIL"]
)


# ADMIN ROUTES
app.include_router(
    admin_router,
    prefix="/api/admin",
    tags=["Admin"]
)


# AUTH ROUTES
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Auth"]
)


# LEADS ROUTES
app.include_router(
    leads_router,
    prefix="/api/leads",
    tags=["Leads"]
)


# EMI ROUTES
app.include_router(
    emi_router,
    prefix="/api/emi",
    tags=["EMI"]
)


@app.get("/")
def read_root():
    return {
        "message": "Aarth-Vaahini Backend is live!"
    }


@app.get("/test-db")
def test_db():

    try:
        data = (
            supabase
            .table("leads")
            .select("*")
            .execute()
        )

        return {
            "status": "Connected to Supabase successfully!",
            "data": data.data
        }

    except Exception as e:
        return {
            "status": "Connection failed",
            "error": str(e)
        }