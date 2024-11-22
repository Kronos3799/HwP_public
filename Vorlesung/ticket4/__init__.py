from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app. config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://testuser:Heute0000@127.0.0.1/testdb'
app.config['SQLAlchemy_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '579'

db = SQLAlchemy(app)

from ticket4 import routes