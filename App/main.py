import json
from flask import Flask, request, render_template
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from datetime import timedelta 

from models import db , User, Pokemon, MyPokemon

''' Begin boilerplate code '''
def create_app():
    app = Flask(__name__, static_url_path='')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SECRET_KEY'] = "MYSECRET"
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7) 
    db.init_app(app)
    return app

app = create_app()

app.app_context().push()

''' End Boilerplate Code '''

''' Set up JWT here '''
def authenticate(uname, password):
    user = User.query.filter_by(username=uname).first()

    if user and user.check_password(password):
        return user

def identity(payload):
    return User.query.get(payload['identity'])

jwt = JWT(app, authenticate, identity)
''' End JWT Setup '''

# edit to query 50 pokemon objects and send to template
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app')
def client_app():
    return app.send_static_file('app.html')

@app.route('/pokemon')
def listing():
    return json.dumps([poke.toDict() for poke in Pokemon.query.all()])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)