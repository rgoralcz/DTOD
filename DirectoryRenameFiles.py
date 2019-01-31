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
    # check if user cancelled prompt - this doesn't actually work (always returns folderPath <> None)
    if not folderPath is None:
        folderPath.set(directory)
        getoldfilelist(directory)
    else:
        folderPath.set("nothing selected")


# function for getting all files within a directories and its subs
def getoldfilelist(directory):
    subdirlist.clear()
    oldfilelist.clear()
    filepathlist.clear()
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            filepath = subdir + os.sep + file
            # unused line to match file types
            #if filepath.endswith(".asm"):
                #dosomethingheremaybe
            # add subdir + ending slash to global subdir variable
            subdirlist.append(subdir + os.sep)
            # add file to global list variable
            oldfilelist.append(file)
            # add filepath to global list variable
            #  this is returning mixed slashes, annoyingly
            #   while these don't affect function (I think), could do a find & replace for consistency
            filepathlist.append(filepath)
    # get string list of files to display to the user
    soldfilelist.set("\n".join(str(x) for x in oldfilelist))
    # get string list of filepaths to display to the user
    sfilepathlist.set("\n".join(str(x) for x in filepathlist))


# function to rename a list of files
# will need booleans for insert before, insert after, replace, prefix, suffix
# will need to access global file name/path lists
def RenameStuff(insertB, insertA, replace, prefix, suffix):
    #togglebuttonrelief(app.frame4.buttonStartRenaming)
    #if insertB:
        # find and insert text
    #if insertA:
        # find and insert text
    #if replace:
        # find and replace text
    #if prefix:
        # prefix fn with text
    #if suffix:
        # suffix fn with text
    print ("RenameStuff called")


# function to check if a string variable is not empty
def isNotBlank (myString):
    if myString and myString.strip():
        #myString is not None AND myString is not empty or blank
        return True
    #myString is None OR myString is empty or blank
    return False


# function to toggle the relief state of a passed button
def togglebuttonrelief(btn):
    if btn.config('relief')[-1] == 'sunken':
        btn.config(relief="raised")
    else:
        btn.config(relief="sunken")

# function to toggle bAddPrefix global boolean and button display state
def togglebAddPrefix(btn):
    global bAddPrefix
    #print("------------")
    #print (str(type(bAddPrefix)) + " - bAddPrefix was: " + str(bAddPrefix))
    togglebuttonrelief(btn)
    bAddPrefix = not bAddPrefix
    #if not bAddPrefix:
        #print("bAddPrefix was Not")
        #bAddPrefix = True
    #elif bAddPrefix:
        #print("bAddPrefix was")
        #bAddPrefix = False
    #print (str(type(bAddPrefix)) + " - bAddPrefix is now: " + str(bAddPrefix))
    #print("===========")

# function to toggle bAddPrefix global boolean and button display state
def togglebAddSuffix(btn):
    global bAddSuffix
    togglebuttonrelief(btn)
    bAddSuffix = not bAddSuffix

# function to toggle bAddPrefix global boolean and button display state
def togglebInsertB(btn):
    global bInsertB
    togglebuttonrelief(btn)
    bInsertB = not bInsertB

# function to toggle bAddPrefix global boolean and button display state
def togglebInsertA(btn):
    global bInsertA
    togglebuttonrelief(btn)
    bInsertA = not bInsertA


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

        # first frame, to prompt user for a directory
        frame1 = Frame(self, borderwidth=10, relief="raised")
        frame1.pack(fill=X)
        # instructions to the left of the frame
        label1a = Label(frame1,\
                text="Click to the right to browse to your desired directory.", width=50)
        label1a.pack(side=LEFT, padx=5, pady=5)
        # clickydothings to the right
        buttonBrowseFolder = Button(frame1, text="Browse to Folder", width=20,\
                command=lambda: BrowseFolder())
        buttonBrowseFolder.pack(side=RIGHT)

        # second frame, to show selected directory
        frame2 = Frame(self, borderwidth=2, relief="sunken")
        frame2.pack(fill=X)
        label2 = Label(frame2, text="Directory Selected:", width=20)
        label2.pack(side=LEFT, padx=5, pady=5)
        # list user selected directory to the right
        label2a = Label(frame2, textvariable=folderPath)
        label2a.pack(fill=X, padx=5, expand=True)

        # fourth frame to show options for renaming
        frame4 = Frame(self, borderwidth=5, relief="solid")
        frame4.pack(fill=X)
        frame4a = Frame(frame4, borderwidth=2, relief="solid")
        frame4a.pack(fill=X)
        label4a = Label(frame4a, text="Options:", width=20)
        label4a.pack(side=LEFT, padx=5, pady=5)
        buttonStartRenaming = Button(frame4a, text="Rename some shit!", width=20,\
                command=lambda: RenameStuff(False, False, False, False, True))
        buttonStartRenaming.pack(side=RIGHT)
        frame4b = Frame(frame4, borderwidth=2, relief="solid")
        frame4b.pack(fill=X)
        # start creating buttons for user to toggle rename functions
        buttonPrefix = tk.Button(frame4b, text="Add Prefix", width=12, relief="raised", command=lambda: togglebAddPrefix(buttonPrefix))
        buttonPrefix.pack(side=LEFT, padx=5)
        buttonSuffix = tk.Button(frame4b, text="Add Suffix", width=12, relief="raised", command=lambda: togglebuttonrelief(buttonSuffix))
        buttonSuffix.pack(side=LEFT, padx=5)
        buttonInsertB = tk.Button(frame4b, text="Insert Before", width=12, relief="raised", command=lambda: togglebInsertB(buttonInsertB))
        buttonInsertB.pack(side=LEFT, padx=5)
        buttonInsertA = tk.Button(frame4b, text="Insert After", width=12, relief="raised", command=lambda: togglebInsertB(buttonInsertA))
        buttonInsertA.pack(side=LEFT, padx=5)

        # third frame
        frame3 = Frame(self, borderwidth=10, relief="raised")
        frame3.pack(fill=BOTH, expand=True)
        # sub frame on the left to show filenames
        frame3a = Frame(frame3, borderwidth=2, relief="sunken")
        frame3a.pack(anchor=N, side=LEFT, fill=BOTH, expand=True)
        label3a1 = Label(frame3a, text="Old File Name List", width=20, anchor="center", borderwidth=2, relief="solid")
        label3a1.pack(anchor="center", padx=5, pady=5)
        label3a2 = Label(frame3a, textvariable=soldfilelist)
        label3a2.pack(padx=2, pady=5)
        # sub frame on the right to show filenames with paths
        #  before 3b because for reasons I don't understand it will only put it on the right if it is created first
        frame3c = Frame(frame3, borderwidth=2, relief="solid")
        frame3c.pack(anchor=N, side=RIGHT, fill=BOTH, expand=True)
        label3c1 = Label(frame3c, text="File Path List", width=15, anchor="center", borderwidth=2, relief="solid")
        label3c1.pack(anchor="center", padx=5, pady=5)
        label3c2 = Label(frame3c, textvariable=sfilepathlist)
        label3c2.pack(padx=2, pady=5)
        # sub frame in the middle to show new filenames
        #  after 3c because for reasons I don't understand it will only put it in the middle if it is created after
        frame3b = Frame(frame3, borderwidth=2, relief="raised")
        frame3b.pack(anchor=N, side=RIGHT, fill=BOTH, expand=True)
        label3b1 = Label(frame3b, text="New File Name List", width=20, anchor="center", borderwidth=2, relief="solid")
        label3b1.pack(anchor="center", padx=5, pady=5)
        label3b2 = Label(frame3b, textvariable=snewfilelist)
        label3b2.pack(padx=2, pady=5)


def main():

    # main window
    root = Tk()
    # set size of window
    root.geometry("800x400+300+200")
    # declare global variable to make the data available
    global folderPath
    # this apparently needs to be here so that labels can access the data
    folderPath = tk.StringVar()
    # global variable to hold list of files found
    global subdirlist
    # initialize as list type
    subdirlist = []
    # global variable to hold list of files found
    global oldfilelist
    # initialize as list type
    oldfilelist = []
    # global variable to hold string list of files found
    global soldfilelist
    # this apparently needs to be here so that labels can access the data
    soldfilelist = tk.StringVar()
    # global variable to hold list of files found
    global newfilelist
    # initialize as list type
    newfilelist = []
    # global variable to hold string list of files found
    global snewfilelist
    # this apparently needs to be here so that labels can access the data
    snewfilelist = tk.StringVar()
    # global variable to hold list of filepaths found
    global filepathlist
    # initialize as list type
    filepathlist = []
    # global variable to hold string list of files found
    global sfilepathlist
    # this apparently needs to be here so that labels can access the data
    sfilepathlist = tk.StringVar()
    # global variable to hold selected state of Add Prefix button
    global bAddPrefix
    bAddPrefix = False
    global bAddSuffix
    bAddSuffix = False
    global bInsertB
    bInsertB = False
    global bInsertA
    bInsertA = False
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
