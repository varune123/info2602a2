from main import db, app, Pokemon
import csv

db.create_all(app=app)

# add code to parse csv, create and save pokemon objects


with open('/workspace/info2602a2/App/pokemon.csv', 'r') as file:
    reader = csv.DictReader(file, delimiter= ',')
    
    for row in reader:
        data = Pokemon(name= row['name'], attack= row['attack'], defense= row[''], 
        hp= row['hp'], height= row['height'], sp_attack= row['sp_attack'], 
        sp_defense= row['sp_defense'], speed= row['speed'], type1= row['type1'], 
        type2= row['type2'], weight= row['weight'])
    

# replace any null values with None to avoid db errors
