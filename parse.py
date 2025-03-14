import csv
from constants import *
from card_class import Card

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
                csv_output.write(card.to_moxfield_format() + "\n")
