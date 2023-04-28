from flask import Response, make_response, jsonify


def http_error_message(message: str, status_code: int) -> Response:
    return make_response(jsonify({
        'message': message
    }), status_code)
