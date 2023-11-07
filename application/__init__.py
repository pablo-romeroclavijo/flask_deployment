from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bgursgni:f6xj-sDbv9CLuVT1qwUgShVmypKMHnnr@tai.db.elephantsql.com/bgursgni'
db = SQLAlchemy(app)

from application import routes

