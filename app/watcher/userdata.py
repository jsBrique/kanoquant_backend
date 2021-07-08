from flask import Flask
from flask_mongoalchemy import MongoAlchemy
import hashlib
from flask import session
import time

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'Users'
# app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://cout:loot@ds223268.mlab.com:23268/coutlootlogin'
db = MongoAlchemy(app)


class Account(db.Document):
    uid=db.IntField()
    username = db.StringField()
    password = db.StringField()
    apikey = db.StringField()  


class AccountData(db.Document):
    username = db.StringField()
    apikey = db.StringField()
    # profits=db.ListField(db.FloatField())
    # nowstock=db.ListField(db.ListField(db.StringField()))
    position=db.ListField(db.AnythingField())
