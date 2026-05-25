from fastapi import FastAPI
from app.core.database import supabase

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

app = FastAPI()


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