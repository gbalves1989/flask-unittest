from flask_openapi3 import OpenAPI, APIBlueprint, Info, HTTPBearer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS


info = Info(
    title='Flask Unittest API',
    version='1.0.0',
    termsOfService='http://example.com/terms/',
    contact={
        'name': 'API Support',
        'url': 'http://www.example.com/support',
        'email': 'support@example.com'
    },
    license={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html'
    }
)

security_schemes = {"jwt": HTTPBearer(bearerFormat="JWT")}
security = [{"jwt": []}]

app = OpenAPI(
    __name__,
    info=info,
    servers=[{'url': 'http://localhost:5000'}]
)
app.config.from_object('config')

CORS(app, origins=[
    'http://localhost:5000/api/v1',
    'http://localhost:5000/openapi'
])

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

api = APIBlueprint('flask-unittest', __name__, url_prefix='/api/v1')

from api.routes import course_route

app.register_api(api)
