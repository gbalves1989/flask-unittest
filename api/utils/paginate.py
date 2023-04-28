from api import ma
from flask import request, url_for, json
from flask_sqlalchemy import Model


def paginate(model: Model, schema: ma.SQLAlchemyAutoSchema, page_query: int, per_page_query: int) -> json:
    page: int = int(request.args.get('page', page_query))
    per_page: int = int(request.args.get('per_page', per_page_query))
    page_obj: Model = model.query.paginate(page=page, per_page=per_page)

    next_pg: str = url_for(
        request.endpoint,
        page=page_obj.next_num if page_obj.has_next else page_obj.page,
        per_page=per_page,
        **request.view_args
    )

    prev_pg: str = url_for(
        request.endpoint,
        page=page_obj.prev_num if page_obj.has_prev else page_obj.page,
        per_page=per_page,
        **request.view_args
    )

    return {
        'total': page_obj.total,
        'pages': page_obj.pages,
        'next': next_pg,
        'prev': prev_pg,
        'results': schema.dump(page_obj.items)
    }
