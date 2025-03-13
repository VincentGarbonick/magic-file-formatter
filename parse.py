import csv

class Card: 
    def __init__(self, raw_row):
        print(raw_row[0])


with open('./example_data/example_collection_2.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader) # skip first row
    for raw_row in reader:
        card = Card(raw_row)
