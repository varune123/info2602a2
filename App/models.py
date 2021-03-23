from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class MyPokemon(db.Model):
  bid = db.Column('bid', db.Integer, primary_key=True)
  id = db.Column('id', db.Integer, db.ForeignKey('user.id'))
  pid = db.Column('pid', db.Integer, db.ForeignKey('pokemon.pid'))
  name = db.Column(db.String(50))
  pokemon = db.relationship('Pokemon')

  def toDict(self):
    return{
      'name':self.name,
      'stats':self.pokemon.toDict()
    }

## Create a User Model
## must have set_password, check_password and to Dict
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def toDict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password
        }


    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        return check_password_hash(self.password, password)

## Create a Pokemon Model
class Pokemon(db.Model):
    pid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    attack = db.Column(db.Float, nullable=False)
    defense = db.Column(db.Float, nullable=False)
    hp = db.Column(db.Float, nullable=False)
    height = db.Column(db.String(10), nullable=True)
    sp_attack = db.Column(db.Float, nullable=True)
    sp_defense = db.Column(db.Float, nullable=True)
    speed = db.Column(db.Integer, nullable=True)
    type1 = db.Column(db.String(50), nullable=True)
    type2 = db.Column(db.String(50), nullable=True)
    weight = db.Column(db.String(10), nullable=True)
    
    def toDict(self):
        return {
            'pid':self.pid,
            'name':self.name,
            'attack':self.attack,
            'defense':self.defense,
            'hp':self.hp,
            'height':self.height,
            'sp_attack':self.sp_attack,
            'sp_defense':self.sp_defense,
            'speed':self.speed,
            'type1':self.type1,
            'type2':self.type2,
            'weight':self.weight
        }
