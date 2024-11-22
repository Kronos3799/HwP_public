from datetime import timedelta

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

UPLOAD_FOLDER = './fishing/static/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
ACCESS_EXPIRES = timedelta(hours=1)

app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["JWT_SECRET_KEY"] = "klfjsalkefjslakfej"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['SESSION_COOKIE_SECURE'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Hochschule@127.0.0.1/fishing'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'sklfjelkösafjaölsekfjsaef'

db = SQLAlchemy(app)
CORS(app)
jwt = JWTManager(app)

from fishing import routes