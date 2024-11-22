from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

CORS(app)

# Datenbank Konfiguration
DB_USER = 'webuser'
DB_PASS = 'Heute0000'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'horseBuy'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] ='gfljhasefkashfmxhfuislf'

db = SQLAlchemy(app)

from HorseBuy import routes