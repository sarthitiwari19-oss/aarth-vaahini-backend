from fastapi import APIRouter
from app.models.user_model import RegisterUser, LoginUser
from app.core.database import supabase
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    verify_access_token
)

router = APIRouter()


# REGISTER API
@router.post("/register")
def register(user: RegisterUser):

    # check existing email
    existing_user = (
        supabase
        .table("users")
        .select("*")
        .eq("email", user.email)
        .execute()
    )

    if existing_user.data:
        return {
            "success": False,
            "message": "Email already exists"
        }

    # hash password
    hashed_password = hash_password(user.password)

    # save user
    data = {
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
        "password": hashed_password,
        "role": "user"
    }

    supabase.table("users").insert(data).execute()

    return {
        "success": True,
        "message": "User registered successfully"
    }


# LOGIN API
@router.post("/login")
def login(user: LoginUser):

    # find user by email
    existing_user = (
        supabase
        .table("users")
        .select("*")
        .eq("email", user.email)
        .execute()
    )

    # email check
    if not existing_user.data:
        return {
            "success": False,
            "message": "Invalid email"
        }

    db_user = existing_user.data[0]

    # password verify
    if not verify_password(
        user.password,
        db_user["password"]
    ):
        return {
            "success": False,
            "message": "Invalid password"
        }

    # create jwt token
    token = create_access_token({
        "email": db_user["email"]
    })

    return {
        "success": True,
        "message": "Login successful",
        "access_token": token,
        "token_type": "bearer"
    }


# PROTECTED ROUTE
@router.get("/me")
def get_current_user(token: str):

    payload = verify_access_token(token)

    if not payload:
        return {
            "success": False,
            "message": "Invalid token"
        }

    return {
        "success": True,
        "user": payload
    }