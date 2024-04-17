from flask import Flask, make_response, jsonify, request, session, g
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import dotenv_values
from flask_bcrypt import Bcrypt
from models import db, Pitcher
import json

# load the .env file where our secrets are stored
config = dotenv_values(".env")

app = Flask(__name__)
app.debug = True
# get the flask secret key from the .env
# (this is how you'll store and retrieve api keys as well)
app.secret_key = config['FLASK_SECRET_KEY']
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.json.compact = False
bcrypt = Bcrypt(app)
migrate = Migrate(app, db)

db.init_app(app)
@app.route('/pitchers')
def get_pitchers():
    pitchers = Pitcher.query.all()
    return jsonify([p.to_dict() for p in pitchers]), 200


if __name__ == '__main__':
    app.run(port=5555, debug=True)