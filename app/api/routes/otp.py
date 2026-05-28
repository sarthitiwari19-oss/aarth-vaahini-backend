from fastapi import APIRouter
from app.models.otp_model import SendOTP, VerifyOTP
from app.core.database import supabase
import random
from datetime import datetime, timedelta

router = APIRouter()


# SEND OTP
@router.post("/send-otp")
def send_otp(data: SendOTP):

    otp = str(random.randint(100000, 999999))

    expires_at = datetime.utcnow() + timedelta(minutes=5)

    otp_data = {
        "email": data.email,
        "otp": otp,
        "expires_at": expires_at.isoformat()
    }

    supabase.table("otp_verifications").insert(otp_data).execute()

    return {
        "success": True,
        "message": "OTP sent successfully",
        "otp": otp
    }


# VERIFY OTP
@router.post("/verify-otp")
def verify_otp(data: VerifyOTP):

    response = (
        supabase
        .table("otp_verifications")
        .select("*")
        .eq("email", data.email)
        .eq("otp", data.otp)
        .execute()
    )

    if len(response.data) > 0:

        otp_record = response.data[0]

        expires_at = datetime.fromisoformat(
            otp_record["expires_at"].replace("Z", "")
        )

        # CHECK OTP EXPIRY
        if datetime.now(expires_at.tzinfo) > expires_at:

            return {
                "success": False,
                "message": "OTP expired"
            }

        # DELETE USED OTP
        supabase.table("otp_verifications")\
            .delete()\
            .eq("email", data.email)\
            .execute()

        return {
            "success": True,
            "message": "OTP verified successfully"
        }

    return {
        "success": False,
        "message": "Invalid OTP"
    }