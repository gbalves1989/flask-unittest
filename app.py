from api import app
from dotenv import load_dotenv
import os


load_dotenv()

if __name__ == '__main__':
    app.run(
        host=os.environ.get('APP_HOST'),
        port=os.environ.get('APP_PORT')
    )
