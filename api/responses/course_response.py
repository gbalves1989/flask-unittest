from pydantic import BaseModel, Field


class CourseResponse(BaseModel):
    id: int = Field(0, description='course id')
    name: str = Field('test', description='name of course')
    description: str = Field('test description', description='description of course')


class CourseListResponse(BaseModel):
    total: int = Field(1, description='total of courses')
    pages: int = Field(1, description='number of pages')
    next: int = Field(1, description='next page')
    prev: int = Field(1, description='preview page')
    results: list[CourseResponse]
    