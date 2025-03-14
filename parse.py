import csv
from constants import *

class Card: 
    def __init__(self, row_dict, format):
        if(format == FORMAT_MTGO):
            self.format = FORMAT_MTGO
            self.init_MTGO_entry(row_dict)
        else:
            print('No recognized card format')
            exit(1)

    def init_MTGO_entry(self, row_dict):
        self.card_name = row_dict['Card Name']
        self.card_quantity = row_dict['Quantity']
        self.MTGO_ID = row_dict['ID #']
        self.rarity = row_dict['Rarity']
        self.set_code = row_dict['Set']
        self.collector_number = row_dict['Collector #']
        self.premium = row_dict['Premium']
        self.sideboarded = row_dict['Sideboarded']
        self.annotation = row_dict['Annotation']
    
    def display_card(self, newline):
        f = '\t'
        if(newline == True):
            f = '\n'
            
        print(
            f'Card Name: {self.card_name}{f}Card Quantity: {self.card_quantity}{f}MTGO ID: {self.MTGO_ID}{f}' +
            f'Rarity: {self.rarity}{f}Set: {self.set_code}{f}Collector Number: {self.collector_number}{f}' + 
            f'Premium: {self.premium}{f}Sideboarded: {self.sideboarded}{f}Annotation: {self.annotation}'
        )
        print('-------------------------------------------------------------------------')

    def to_moxfield_format(self):
        if(self.format == FORMAT_MTGO):
            card_dict = {
                "Count": self.card_quantity,
                "Name": self.card_name,
                "Edition": self.set_code,
                "Condition": MOXFIELD_DEFAULT_CONDITION,
                "Language": MOXFIELD_DEFAULT_LANGUAGE,
                #TODO: Get foiling working
                #"Foil": "foil" if self.premium else "",
                "Foil": "",
                "Collector Number": self.collector_number,
                "Alter": MOXFIELD_FALSE,
                "Playtest Card": MOXFIELD_FALSE,
                "Purchase Price": MOXFIELD_DEFAULT_PRICE 
            }   
            return ",".join(f'"{str(card_dict[header])}"' for header in MOXFIELD_HEADERS)

        else: 
            print('Cannot export card, something catestrophic has happened')
            exit(1)

import_csv_format = FORMAT_MTGO
export_format = FORMAT_MOXFIELD
with open('./example_data/foil_example.csv', 'r') as csv_input:
    reader = csv.DictReader(csv_input)
    # can turn this into a function that just requires the format type and maybe import/export
    if(export_format == FORMAT_MOXFIELD):
        with open('./result.csv', 'w') as csv_output:
            csv_output.write(join_headers(MOXFIELD_HEADERS) + "\n")
            for row in reader:
                card = Card(row, import_csv_format)
