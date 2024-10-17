from flask import Flask
from flask_cors import CORS

from src.utils.db_function import create_db_connection
from src.utils.db_function import db

app = Flask(__name__)
CORS(app)

db_url = create_db_connection()
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)



from src.routes import routes
