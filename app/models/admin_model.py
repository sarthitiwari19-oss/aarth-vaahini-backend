from pydantic import BaseModel


class UpdateLeadStatus(BaseModel):
    status: str