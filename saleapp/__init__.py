from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = '\xf4\x13{\xe4v\xbb\xd3\xbb\x87\n\xc4\x9f\x96\xbd\xc7<'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456789@localhost/hocsinhdb?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)

admin = Admin(app=app, name="IT82 SHOP", template_mode='bootstrap4')
login = LoginManager(app=app)