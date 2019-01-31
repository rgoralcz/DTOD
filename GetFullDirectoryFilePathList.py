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
        getfilelist(directory)
    else:
        folderPath.set("nothing selected")


# function for getting all files within a directories and its subs
def getfilelist(directory):
    subdirlist.clear()
    filelist.clear()
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
            filelist.append(file)
            # add filepath to global list variable
            #  this is returning mixed slashes, annoyingly
            #   while these don't affect function (I think), could do a find & replace for consistency
            filepathlist.append(filepath)
    # get string list of files to display to the user
    sfilelist.set("\n".join(str(x) for x in filelist))
    # get string list of filepaths to display to the user
    sfilepathlist.set("\n".join(str(x) for x in filepathlist))


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

        # second frame
        frame2 = Frame(self, borderwidth=10, relief="sunken")
        frame2.pack(fill=X)
        label2 = Label(frame2, text="Directory Selected:", width=20)
        label2.pack(side=LEFT, padx=5, pady=5)
        # list user selected directory to the right
        label2a = Label(frame2, textvariable=folderPath)
        label2a.pack(fill=X, padx=5, expand=True)

        # third frame
        frame3 = Frame(self, borderwidth=10, relief="raised")
        frame3.pack(fill=BOTH, expand=True)
        # sub frame on the left to show filenames
        frame3a = Frame(frame3, borderwidth=2, relief="solid")
        frame3a.pack(side=LEFT, fill=BOTH, expand=True)
        label3a1 = Label(frame3a, text="File Name List", width=15, anchor="center", borderwidth=2, relief="solid")
        label3a1.pack(anchor="center", padx=5, pady=5)
        label3a2 = Label(frame3a, textvariable=sfilelist)
        label3a2.pack(anchor="w", padx=2, pady=5)
        # sub frame on the right to show filenames wth paths
        frame3b = Frame(frame3, borderwidth=2, relief="solid")
        frame3b.pack(side=RIGHT, fill=BOTH, expand=True)
        label3b1 = Label(frame3b, text="File Path List", width=15, anchor="center", borderwidth=2, relief="solid")
        label3b1.pack(anchor="center", padx=5, pady=5)
        label3b2 = Label(frame3b, textvariable=sfilepathlist)
        label3b2.pack(anchor="w", padx=2, pady=5)


def main():

    # main window
    root = Tk()
    # set size of window
    root.geometry("600x400+300+200")
    # declare global variable to make the data available
    global folderPath
    # this apparently needs to be here so that labels can access the data
    folderPath = tk.StringVar()
    # global variable to hold list of files found
    global subdirlist
    # initialize as list type
    subdirlist = []
    # global variable to hold list of files found
    global filelist
    # initialize as list type
    filelist = []
    # global variable to hold string list of files found
    global sfilelist
    # this apparently needs to be here so that labels can access the data
    sfilelist = tk.StringVar()
    # global variable to hold list of filepaths found
    global filepathlist
    # initialize as list type
    filepathlist = []
    # global variable to hold string list of files found
    global sfilepathlist
    # this apparently needs to be here so that labels can access the data
    sfilepathlist = tk.StringVar()
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
