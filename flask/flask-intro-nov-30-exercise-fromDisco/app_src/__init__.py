from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "postgresql+psycopg2://postgres:postgres@localhost:5432/flask_intro"
db = SQLAlchemy(app)

# prevent circular import
# models import db, 
# so import Reminder after db is instatiated
from app_src.models import Reminder

#with app.app_context():
#    db.create_all()
