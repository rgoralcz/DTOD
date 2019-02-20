# my own fumblings

import tkinter as tk
from tkinter import filedialog


# function for browsing to the pdf file locaitons
def BrowseFolder():
    # prompt user
    filename=filedialog.askdirectory()
    # declare global variable to make the data available
    global folderPath
    # put the file path in the global varriable
    folderPath.set(filename)

# declaire the main window
root =tk.Tk()

# This apparently needs to be here so that label2 can access the data
folderPath = tk.StringVar()

# set title
root.title("A test GUI")
root.Border = tk.Frame(root, relief='solid', borderwidth=4)
# header
label1 = tk.Label(root, text = "This is the header text...\n....filling up space"\
    ,width = 80, wraplength = 200, borderwidth=1, relief="solid")
# put header at the top
label1.grid(row=0, column=0, padx=5, pady=5)
# browsed path display
label2 = tk.Label(root, textvariable=folderPath)
# put below header
label2.grid(row=1)

# a button run BrowseFolder
button1 = tk.Button(root, text="Browse", width =15, command=BrowseFolder)
# positioning the browse button
button1.grid(row=1, column = 1)


# run main window
root.mainloop()
