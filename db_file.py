from flask_sqlalchemy import SQLAlchemy
import flask
import sqlite3
from flask_session import Session


app =flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite://LMAS.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFOCATIONS']= False

Session(app)

db=SQLAlchemy(app)

class LMAS(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    current_time = db.Column(db.String(64), index=True)
    own_city_id = db.Column(db.String(64), index=True)
    city = db.Column(db.String(64), index=True)
    latitude = db.Column(db.String(64), index=True)
    longitude = db.Column(db.String(64), index=True)
    temperature=db.Column(db.String(64),index=True)
    temperature_feel=db.Column(db.String(64),index=True)


with app.app_context():
 db.create_all()