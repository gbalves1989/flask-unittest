from pydantic import BaseModel, Field


class ErrorsResponse(BaseModel):
    message: str = Field('error message', description='error message')
    