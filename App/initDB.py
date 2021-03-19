from main import db, app, Pokemon
import csv

db.create_all(app=app)

# add code to parse csv, create and save pokemon objects


with open('/workspace/info2602a2/App/pokemon.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter= ',')
    
    for row in reader:
        data = Pokemon(name= row['name'], attack= row['attack'], defense= row['defense'], 
        hp= row['hp'], height= row['height_m'], sp_attack= row['sp_attack'], 
        sp_defense= row['sp_defense'], speed= row['speed'], type1= row['type1'], 
        type2= row['type2'], weight= row['weight_kg'])
    
        if data.name =='':
            data.name ='None'
        if data.height =='':
            data.height =='None'
        if data.weight =='':
            data.weight ='None'
        if data.type1 =='':
            data.type1 ='None'
        if data.type2 =='':
            data.type2 ='None'

db.session.add(data)
db.session.commit()
# replace any null values with None to avoid db errors
