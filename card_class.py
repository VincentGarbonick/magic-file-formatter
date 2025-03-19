from constants import *
from moxfield_set_code_mapper import MoxfieldMapper
import xml.etree.ElementTree as ET

class Card: 
    def __init__(self, data, output_format):
        if(output_format == FORMAT_MTGO_CSV):
            self.input_format = FORMAT_MTGO_CSV
            self.output_format = FORMAT_MTGO_CSV
            self.init_MTGO_CSV_entry(data)
        elif(output_format == FORMAT_MTGO_DEK):
            self.input_format = FORMAT_MTGO_DEK
            self.output_format = FORMAT_MTGO_CSV
            self.init_MTGO_DEK_entry(data)
        else:
            print('No recognized card output format')
            exit(1)

    def init_MTGO_CSV_entry(self, row_dict):
        self.card_name = row_dict['Card Name']
        self.card_quantity = row_dict['Quantity']
        self.MTGO_ID = row_dict['ID #']
        self.rarity = row_dict['Rarity']
        self.set_code = MoxfieldMapper.update_code(row_dict['Set'])
        self.collector_number = row_dict['Collector #']
        self.premium = row_dict['Premium']
        self.sideboarded = row_dict['Sideboarded']
        self.annotation = row_dict['Annotation']

    def init_MTGO_DEK_entry(self, child):
        self.card_name = child['Name']
        self.card_quantity = child['Quantity']
        self.MTGO_ID = child['CatID']
        self.rarity = ""
        self.set_code = ""
        self.collector_number = ""
        self.premium = ""
        self.sideboarded = child['Sideboard']
        # annotation is not present in actual MTGO exported decks usually
        self.annotation = child.get('Annotation', "")
    
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
        if(self.output_format == FORMAT_MTGO_CSV):
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
