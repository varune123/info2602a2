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


class Pokemon(db.Model):
    pid = db.Column('pid', db.Integer, primary_key=True)
    abilities = db.Column(db.String(50))
    against_bug = db.Column(db.Float)
    against_dark = db.Column(db.Float)
    against_dragon = db.Column(db.Float)
    against_electric = db.Column(db.Float)
    against_fairy = db.Column(db.Float)
    against_fight = db.Column(db.Float)
    against_fire = db.Column(db.Float)
    against_flying = db.Column(db.Float)
    against_ghost = db.Column(db.Float)
    against_grass = db.Column(db.Float)
    against_ground = db.Column(db.Float)
    against_ice = db.Column(db.Float)
    against_normal = db.Column(db.Float)
    against_poison = db.Column(db.Float)
    against_psychic = db.Column(db.Float)
    against_rock = db.Column(db.Float)
    against_steel = db.Column(db.Float)
    against_water = db.Column(db.Float)
    attack = db.Column(db.Float)
    base_egg_steps = db.Column(db.Float)
    base_happiness = db.Column(db.Float)
    base_total = db.Column(db.Float)
    capture_rate = db.Column(db.Float)
    classfication = db.Column(db.String(50))
    defense = db.Column(db.Float)
    experience_growth = db.Column(db.Float)
    height = db.Column(db.Float)
    hp = db.Column(db.Float)
    japanese_name = db.Column(db.String(50))
    name = db.Column(db.String(50))
    percentage_male = db.Column(db.Float)
    pokedex_number = db.Column(db.Integer)
    sp_attack = db.Column(db.Float)
    sp_defense = db.Column(db.Float)
    speed = db.Column(db.Integer)
    type1 = db.Column(db.String(50))
    type2 = db.Column(db.String(50))
    weight = db.Column(db.Float)
    generation = db.Column(db.Float)
    is_legendary = db.Column(db.Float)
    
    
    
    
    
    
    
    
    
    
    

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
## Create a Pokemon Model