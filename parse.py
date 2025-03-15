import csv
from constants import *
from card_class import Card
import tkinter as tk
from tkinter import filedialog

def generate_csv(input_file_path, output_file_path, input_format, output_format): 
    import_csv_format = input_format
    export_format = output_format
    with open(input_file_path, 'r') as csv_input:
        reader = csv.DictReader(csv_input)
        # can turn this into a function that just requires the format type and maybe import/export
        if(export_format == FORMAT_MOXFIELD):
            with open(output_file_path, 'w') as csv_output:
                csv_output.write(join_headers(MOXFIELD_HEADERS) + "\n")
                for row in reader:
                    card = Card(row, import_csv_format)
                    #card.display_card(True)
                    csv_output.write(card.to_moxfield_format() + "\n")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
    title="Select a file",
    filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    if file_path:   
        generate_csv(file_path, './result.csv', FORMAT_MTGO_CSV, FORMAT_MOXFIELD)
    else: 
        print('No file path given :(')
