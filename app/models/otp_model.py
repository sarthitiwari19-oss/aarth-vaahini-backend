from pydantic import BaseModel


from pydantic import BaseModel


class SendOTP(BaseModel):
    email: str


class VerifyOTP(BaseModel):
    email: str
    otp: str