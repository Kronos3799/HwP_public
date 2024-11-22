from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://testuser:Heute0000@127.0.0.1:3306/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] ='sdfsdfsdfsdfsdf'

db = SQLAlchemy(app)

from ticket import routes