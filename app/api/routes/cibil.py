from fastapi import APIRouter
from app.models.cibil_model import CIBILCheck

router = APIRouter()


# CIBIL CHECK API
@router.post("/check")
def check_cibil(data: CIBILCheck):

    # dummy cibil score
    score = 750

    return {
        "success": True,
        "message": "CIBIL fetched successfully",
        "cibil_score": score,
        "user": {
            "name": data.name,
            "pan_number": data.pan_number
        }
    }