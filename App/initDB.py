from main import db, app #, Pokemon
import csv

db.create_all(app=app)

# add code to parse csv, create and save pokemon objects
data = []

with open('/workspace/info2602a2/App/pokemon.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        data.append(row)
print(data[0])
# replace any null values with None to avoid db errors
