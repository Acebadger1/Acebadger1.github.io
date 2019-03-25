# Update menu for all files in the site
# Prints out a little funny. Can format docs with vs code by right clicking in it.

import os
from bs4 import BeautifulSoup 
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

"""---- Function that gets input file ----"""
root = tk.Tk(  )

#This is where we lauch the file manager bar.
def OpenFile():
    name = filedialog.askopenfilename(initialdir=".",
                           filetypes =(("HTML Files", "*.html"),("All Files","*.*")),
                           title = "Choose a file."
                           )
                           
    #Using try in case user types in unknown file or closes without choosing a file.
    try:
        with open(name,'r') as UseFile:
            #print(UseFile.read())
            return name
    except:
        print("No file exists")

#root.mainloop()
"""-------"""


# Make list of all html files
html_files = []
for file in os.listdir("."):
    if file.endswith(".html"):
        html_files.append(file)

# Find which is the input file:
messagebox.showinfo('File Input Helper', "Please select the file to copy from.")
in_file = OpenFile()

# Find the menu of input file
in_soup = BeautifulSoup( open(in_file) , 'html.parser')
in_menu = in_soup.find(id="menu")

# Remove input file from the html_files thing -- working 3/25/19
for file in html_files:
    if file in in_file:
        html_files.remove(file)

# Go through all files and update the menu
for out_file in html_files:

    # Open the file as soup
    out_soup = BeautifulSoup( open(out_file), 'html.parser')

    # Overwrite menu of the output file
    out_soup.find(id="menu").replace_with(in_menu)

    # Save the file
    with open(out_file, "w") as file:
        file.write(str(out_soup.prettify()))