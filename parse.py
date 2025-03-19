import csv
from constants import *
from card_class import Card
import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
import os

def generate_csv(input_file_path, output_file_path, input_format, output_format):
    try:
        export_format = output_format
        if input_format == FORMAT_MTGO_CSV: 
            with open(input_file_path, 'r') as csv_input:
                reader = csv.DictReader(csv_input)
                # can turn this into a function that just requires the format type and maybe import/export
                if(export_format == FORMAT_MOXFIELD):
                    with open(output_file_path, 'w') as csv_output:
                        csv_output.write(join_headers(MOXFIELD_HEADERS) + "\n")
                        for row in reader:
                            card = Card(row, input_format)
                            #card.display_card(True)
                            csv_output.write(card.to_moxfield_format() + "\n")
        elif input_format == FORMAT_MTGO_DEK:
            with open(input_file_path, 'r') as file:
                xml_content = file.read()
                if(export_format == FORMAT_MOXFIELD):
                    with open(output_file_path, 'w') as csv_output:
                        csv_output.write(join_headers(MOXFIELD_HEADERS) + "\n")
                        root = ET.fromstring(xml_content)
                        for child in root:
                            if(child.tag == MTGO_CARD_TAG):
                                card = Card(child.attrib, input_format)
                                csv_output.write(card.to_moxfield_format() + "\n")
        return SUCCESS_CODE
    except Exception as e:
        return e
    

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    result = PASSTHROUGH_CODE
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("CSV & DEK files", "*.csv *.dek"), ("All files", "*.*"))
    )
    file_name, file_extension = os.path.splitext(file_path)
    if file_path:
        if(file_extension == CSV):
            result = generate_csv(file_path, './result.csv', FORMAT_MTGO_CSV, FORMAT_MOXFIELD)
        elif(file_extension == DEK):
            result = generate_csv(file_path, './result.csv', FORMAT_MTGO_DEK, FORMAT_MOXFIELD)
    
        if result != SUCCESS_CODE:
            if result == PASSTHROUGH_CODE:
                print("Passed through") 
            else:
                print(f'Exception: {result}')
        else: 
            print("Converted successfully...")

    else: 
        print('No file path given :(')
