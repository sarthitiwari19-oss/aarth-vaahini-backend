from pydantic import BaseModel, EmailStr


class RegisterUser(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str