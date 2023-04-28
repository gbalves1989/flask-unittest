from pydantic import BaseModel, Field


class UnauthorizedResponse(BaseModel):
    message: str = Field('unauthorized', description="Credentials aren't valid.")
    