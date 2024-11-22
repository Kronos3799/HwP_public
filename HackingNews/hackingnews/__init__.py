from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

CORS(app)

# database configuration
DB_USER = 'api'
DB_PASS = 'hgE7r40dA79a'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'hackingnews'
DB_CLIENT_FLAG = 'CLIENT_MULTI_STATEMENTS'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# secret key for session management
SECRET_KEY = 'lzawrznrxngrsyftnjqbpktrpvgvozzs'

app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

from hackingnews import routes