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

@app.get('/check_session')
def check_session():
    user = db.session.get(User, session.get('user_id'))
    print(f'check session {session.get("user_id")}')
    
    if user:
        return user.to_dict(rules=['-password_hash']), 200
    else:
        # The first time a user visits a page (i.e. is not logged in)
        # we will return this.
        return {"message": "No user logged in"}, 401
    
    @app.post('/login')
def login():
    # get the data from the post request (dict of username/password)
    data = request.json
    # get the user based on username
    user = User.query.filter(User.name == data.get('name')).first()

    # check that the hash of supplied password matches the hash stored in the db
    if user and bcrypt.check_password_hash(user.password_hash, data.get('password_hash')):
        # if successful, set a key in the session with the user id
        session["user_id"] = user.id
        print("success")
        
        return user.to_dict(), 200
    else:
        return { "error": "Invalid username or password" }, 401
    
    
    @app.post('/signup')
def signup():
    data = request.json
    try:
        # make a new object from the request json
        user = User(
            name=data.get("name"),
            password_hash=bcrypt.generate_password_hash(data.get("password"))
        )
        # add to the db
        db.session.add(user)
        db.session.commit()
        session["user_id"] = user.id
        # return object we just made
        return user.to_dict(), 201
    except IntegrityError as e:
        print("caught1")
        print(e)
        return {"error": f"username taken"}, 405
    except exc.IntegrityError as e:
        print("caught2")
        print(e)
        return {"error": f"username taken"}, 405

if __name__ == '__main__':
    app.run(port=5555, debug=True)