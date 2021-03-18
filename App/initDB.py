from main import db, app #, Pokemon
import csv

db.create_all(app=app)

# add code to parse csv, create and save pokemon objects


with open('/workspace/info2602a2/App/pokemon.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        data = row
        #db.session.add(data)
    for key in data:
        print(key, "\t", data[key])
    
    #db.session.commit()
# replace any null values with None to avoid db errors
