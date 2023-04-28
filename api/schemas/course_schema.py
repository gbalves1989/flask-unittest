from api import ma
from ..models.course_model import CourseModel
from marshmallow import fields


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model: CourseModel = CourseModel
        load_instance: bool = True
        fields: tuple = ('id', 'name', 'description')

    name: str = fields.String(required=True)
    description: str = fields.String(required=True)
