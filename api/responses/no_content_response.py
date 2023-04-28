from pydantic import BaseModel, Field


class NoContentResponse(BaseModel):
    content: str = Field('no content', description='no content')
