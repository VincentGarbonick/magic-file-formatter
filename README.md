## Magic File Formatter  
#### This software is provided as-is with no warranty. Use at your own risk.  
#### The full license is included in the repo.

The purpose of this application is to convert MTGO collections into a format that can be uploaded to Moxfield collections. If this project gains enough interest, I can easily extend the import/export functionality to support whatever formats y'all desire.

## Installation and Execution  
You have two options for running this application:

### Directly Run the .exe  
This option is for Windows users only (though I’m sure a Linux user won't need to read much further for this to work).

I've taken the liberty of compiling everything into a `.exe` file. You may have to right-click it and allow it to run under Security settings. After that, just double-click it, and it’ll launch like a normal app.

This is the simplest option, as the `.exe` is completely standalone.

### Run as a Script  
For those of you who are more security-minded, like myself, and would rather not run a random `.exe` from a Git repo, you can simply run this as a script from the terminal. This works on all operating systems. Except maybe Mac. Fuck Mac. You're on your own.

1. Make sure you have Python installed.  
2. Open a command prompt or terminal. Navigate to the directory where the script is located using `cd`.  
3. Type `python app.py` or `python3 app.py` and press Enter.  
   
If you can't run it as a script, it is highly likely your python is not installed. PM me and I can help debug when I have a moment. 

## Operation

### MTGO  
1. Navigate to your MTGO collection.  
2. Click on any card. Press **Ctrl + A** to select your entire collection.  
3. Right-click and select **Export Collection**.  
4. A file browser will pop up. By default, the file type will be `.dek`. This will work with my application, but it will **not** preserve card versions. If you wish to preserve versions, click the dropdown and select `.csv`.  
5. Save the file.

### Magic File Formatter  
1. Run the application as a script or directly launch the `.exe`.  
2. Use the **Browse** feature to find your input file.  
3. Choose the input format, either `.dek` or `.csv`, based on how you exported the file.  
4. Select the folder where you want the output to be saved. Leave it blank to output to the same folder the application is running from.  
5. The only available output format right now is **Moxfield**.  
6. Press **Convert**.  
7. Upload the resulting file to your Moxfield collection.

## For Those Too Lazy to Read (Like Me)  
I have a YouTube tutorial for all of this here:  
*Link coming soon.*
