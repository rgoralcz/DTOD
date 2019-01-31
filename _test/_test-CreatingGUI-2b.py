# I don't actually understand the difference between the first two import items
import tkinter as tk
from tkinter import Tk, Menu, Text, TOP, BOTH, RIGHT, X, N, LEFT
from tkinter.ttk import Frame, Button, Style, Label, Entry
# library for browsing to file loctions
from tkinter import filedialog
# library for directory things
import os


# function to destroy a frame passed to it
def close_window(tempobj):
    tempobj.destroy()

# function for browsing to a directory
def BrowseFolder():
    # prompt user
    directory=filedialog.askdirectory()
    # try to force received directory to string
    #sfolderPath = str(directory)
    # debug msg
    #print ("directory type: " + type(directory))
    #print ("sfolderPath type: " + type(sfolderPath))
    #print ("folderPath type: " + type(folderPath))
    # set the global variable to the directory received
    #if folderPath.strip():
    #if isNotBlank(folderPath):
    if not folderPath is None:
        folderPath.set(directory)
        getfilelist(directory)
        # debug msg
        #print ("directory = " + directory)
    else:
        folderPath.set("nothing selected")
        # debug msg
        #print ("directory selection cancelled")


# function for getting all files within a directories and its subs
def getfilelist(directory):
    filelist.clear()
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            # add file to global list variable
            filelist.append(file)
            # unused line to match file types
            #if filepath.endswith(".asm"):
            # debug print os.path.join(subdir, file)
            filepath = subdir + os.sep + file
            #print (filepath)
            #print (file)
    # debug msg
    #print (filelist)
    # debug msg
    #print("\n".join(str(x) for x in filelist))
    # get string list of files to display to the user
    sfilelist.set("\n".join(str(x) for x in filelist))
    # debug msg
    #print(sfilelist)
    #for item in filelist:
        #print (item)


# function to check if a string variable is not empty
def isNotBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return True
    #myString is None OR myString is empty or blank
    return False

# the frame class?
class Example(Frame):

    # some shit that we do because it's the 'right' way to do things
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Directory Info")
        # main window
        self.pack(fill=BOTH, expand=True,padx=5,pady=5)

        # first frame
        frame1 = Frame(self, borderwidth=10, relief="solid")
        frame1.pack(fill=X)
        # instructions to the left of the frame
        label1a = Label(frame1,\
                text="Click to the right to browse to your desired directory.", width=50)
        label1a.pack(side=LEFT, padx=5, pady=5)
        # clickydothings to the right
        buttonBrowseFolder = Button(frame1, text="Browse to Folder", width=20,\
                command=lambda: BrowseFolder())
        buttonBrowseFolder.pack(side=RIGHT)

        # second frame
        frame2 = Frame(self, borderwidth=10, relief="solid")
        frame2.pack(fill=X)
        label2 = Label(frame2, text="Directory Selected:", width=20)
        label2.pack(side=LEFT, padx=5, pady=5)
        # list user selected directory to the right
        label2a = Label(frame2, textvariable=folderPath)
        label2a.pack(fill=X, padx=5, expand=True)

        # third frame
        frame3 = Frame(self, borderwidth=10, relief="solid")
        frame3.pack(fill=BOTH, expand=True)
        # sub frame on the left to show all files found matching criteria
        frame3a = Frame(frame3, borderwidth=2, relief="solid")
        frame3a.pack(side=LEFT, fill=BOTH, expand=True)
        label3a = Label(frame3a, text="File List", width=10)
        label3a.pack(anchor=N, padx=5, pady=5)
        label3a1 = Label(frame3a, width=20, textvariable=sfilelist)
        label3a1.pack(fill=BOTH, padx=5, pady=2)
        # sub frame on the right to show.. nothing, yet
        frame3b = Frame(frame3, borderwidth=2, relief="solid")
        frame3b.pack(side=RIGHT, fill=BOTH, expand=True)
        label3b = Label(frame3b, text="Other List", width=10)
        label3b.pack(side=TOP, anchor=N, padx=5, pady=5)
        #revtxt = Text(frame3, height=5)
        #revtxt.pack(fill=BOTH, expand=True, pady=5, padx=5)


def main():

    # main window
    root = Tk()
    # set size of window
    root.geometry("600x400")
    # declare global variable to make the data available
    global folderPath
    # this apparently needs to be here so that labels can access the data
    folderPath = tk.StringVar()
    # global variable to hold list of files found
    global filelist
    filelist = []
    # global variable to hold string list of files found
    global sfilelist
    sfilelist = tk.StringVar()
    # create frame in root
    app = Example()
    # a button to close root
    button = tk.Button(root, text="Close", width=15,\
            command=root.destroy, borderwidth=5, relief="solid")
    # tacking the close button to the end of root
    button.pack(pady=15)
    # end main
    root.mainloop()

# just here for reasons, to get things started
if __name__ == '__main__':
    main()
