import tkinter as tk
from tkinter import filedialog, ttk
import os
from constants import * 
from parse import generate_csv

def center_window(root, width=450, height=280):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")

def select_input_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("CSV & DEK files", "*.csv *.dek"), ("All files", "*.*"))
    )
    if file_path:
        input_entry.config(state="normal")
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)
        input_entry.config(state="readonly")
        update_status("Ready to convert.")

def select_output_directory():
    dir_path = filedialog.askdirectory(title="Select Output Directory")
    if dir_path:
        output_dir.set(dir_path) 
        

def convert_file():
    input_file = input_entry.get()
    output_dir_path = output_dir.get()
    input_format = input_format_var.get()
    output_format = output_format_var.get()

    if not input_file:
        update_status("Error: No input file selected.")
        return
    
    if not output_dir_path:
        update_status("Error: No output location specified.")
        return
    
    file_name, file_extension = os.path.splitext(input_file)

    if(file_extension != DEK and input_format == FORMAT_MTGO_DEK):
        update_status("Error: Mismatch between input format and file extension.")
        return

    if(file_extension != CSV and input_format == FORMAT_MTGO_CSV):
        update_status("Error: Mismatch between input format and file extension.")
        return

    # print(f'Input File: {input_file}\nOutput File: {output_dir_path}\nInput Format: {input_format}\nOutput Format: {output_format}')
    update_status(f"Converting from {input_format} to {output_format}...")
    full_output_path = output_dir_path + "/" + RESULT_FILE_NAME + CSV
    generate_csv(input_file, full_output_path, input_format, output_format)
    output_file.set(full_output_path)
    update_status("Conversion completed successfully!")
    
def update_status(message):
    status.set(message)

if __name__ == "__main__":
    # Create the main window
    root = tk.Tk()
    root.title(APP_NAME)
    root.resizable(False, False)
    
    # Center the window
    center_window(root, 450, 310)
    
    # Variables
    status = tk.StringVar()
    input_format_var = tk.StringVar(value=INPUT_FORMATS[0]) # use an array with index 1 in the constants for this
    output_format_var = tk.StringVar(value=OUTPUT_FORMATS[0])
    output_dir = tk.StringVar(value=os.getcwd())
    output_file = tk.StringVar()
    
    # Main frame with padding
    main_frame = ttk.Frame(root, padding="20 20 20 20")
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Input file selection
    ttk.Label(main_frame, text="Input File:").grid(row=0, column=0, sticky=tk.W, pady=(0, 10))
    input_entry = ttk.Entry(main_frame, width=30, state="readonly") 
    input_entry.grid(row=0, column=1, padx=5, pady=(0, 10), sticky=tk.EW)
    ttk.Button(main_frame, text="Browse...", command=select_input_file).grid(row=0, column=2, padx=(5, 0), pady=(0, 10))
    
    # Input format selection
    ttk.Label(main_frame, text="Input Format:").grid(row=1, column=0, sticky=tk.W, pady=(0, 10))
    input_format_options = INPUT_FORMATS
    input_format_dropdown = ttk.Combobox(main_frame, textvariable=input_format_var, values=input_format_options, state="readonly", width=10)
    input_format_dropdown.grid(row=1, column=1, sticky=tk.W, padx=5, pady=(0, 10))
    
    # Output directory selection
    ttk.Label(main_frame, text="Output Directory:").grid(row=3, column=0, sticky=tk.W, pady=(0, 10))
    output_dir_entry = ttk.Entry(main_frame, textvariable=output_dir, width=30, state="readonly")
    output_dir_entry.grid(row=3, column=1, padx=5, pady=(0, 10), sticky=tk.EW)
    ttk.Button(main_frame, text="Browse...", command=select_output_directory).grid(row=3, column=2, padx=(5, 0), pady=(0, 10))

    # Output format selection
    ttk.Label(main_frame, text="Output Format:").grid(row=4, column=0, sticky=tk.W, pady=(0, 10))
    output_format_options = OUTPUT_FORMATS
    output_format_dropdown = ttk.Combobox(main_frame, textvariable=output_format_var, values=output_format_options, state="readonly", width=10)
    output_format_dropdown.grid(row=4, column=1, sticky=tk.W, padx=5, pady=(0, 10))

    # Output filename preview 
    ttk.Label(main_frame, text="Output File:").grid(row=5, column=0, sticky=tk.W, pady=(0, 10))
    output_entry = ttk.Entry(main_frame, textvariable=output_file, width=30, state="readonly")
    output_entry.grid(row=5, column=1, padx=5, pady=(0, 10), sticky=tk.EW)

    # Space before buttons
    separator = ttk.Separator(main_frame, orient='horizontal')
    separator.grid(row=6, column=0, columnspan=3, sticky=tk.EW, pady=10)

    # Action buttons
    button_frame = ttk.Frame(main_frame)
    button_frame.grid(row=7, column=0, columnspan=3, pady=(10, 15))
    
    convert_button = ttk.Button(button_frame, text="Convert", command=convert_file, width=15)
    convert_button.pack(side=tk.LEFT, padx=5)
    
    exit_button = ttk.Button(button_frame, text="Exit", command=root.destroy, width=15)
    exit_button.pack(side=tk.LEFT, padx=5)
    
    # Status bar
    status_frame = ttk.Frame(root, relief=tk.SUNKEN, borderwidth=1)
    status_frame.pack(side=tk.BOTTOM, fill=tk.X)
    
    status_label = ttk.Label(status_frame, textvariable=status, anchor=tk.W, padding=(5, 2))
    status_label.pack(fill=tk.X)
    
    update_status("Ready. Please select an input file.")
    root.mainloop()