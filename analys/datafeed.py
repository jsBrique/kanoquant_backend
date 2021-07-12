from flask import Flask
from flask_mongoalchemy import MongoAlchemy
import hashlib
from flask import session
import time

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'Quant'
# app.config['MONGOALCHEMY_CONNECTION_STRING'] = 'mongodb://cout:loot@ds223268.mlab.com:23268/coutlootlogin'
db = MongoAlchemy(app)

class ETFQuant(db.Document):
    ContinRise_3days=db.ListField(db.AnythingField())
    ContinRise_4days=db.ListField(db.AnythingField())
    ContinRise_5days=db.ListField(db.AnythingField())
    ContinRise_6days=db.ListField(db.AnythingField())