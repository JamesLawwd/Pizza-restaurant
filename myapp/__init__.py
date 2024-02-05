from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app= Flask(__name__)

app.config['SECRET_KEY'] = 'fdf62dd0da698eea2cc004e6affd6172'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

    







