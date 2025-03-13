import csv

class Card: 
    def __init__(self, row_dict, format):
        if(format == 'MTGO'):
            self.init_MTGO_entry(row_dict)
        else:
            print('No recognized card format')
            exit(1)

        
    def init_MTGO_entry(self, row_dict):
        self.card_name = row_dict['Card Name']
        self.card_quantity = row_dict['Quantity']
        self.MTGO_ID = row_dict['ID #']
        self.rarity = row_dict['Rarity']
        self.set = row_dict['Set']
        self.collector_number = row_dict['Collector #']
    
    def display_card(self, newline):
        f = '\t'
        if(newline == True):
            f = '\n'
            
        print(
            f'Card Name: {self.card_name}{f}Card Quantity: {self.card_quantity}{f}MTGO ID: {self.MTGO_ID}{f}' +
            f'Rarity: {self.rarity}{f}'
        )


with open('./example_data/example_collection_2.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        card = Card(row, "MTGO")
        card.display_card(False)