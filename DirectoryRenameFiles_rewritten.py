# I don't actually understand the difference between the first two import items
import tkinter as tk
from tkinter import Tk, ttk, Canvas, Scrollbar, Menu, Text, TOP, BOTH, RIGHT, X, N, LEFT
from tkinter.ttk import Frame, Button, Style, Label, Entry
# library for browsing to file loctions
from tkinter import filedialog
# library for directory things
import os


class FileRename(tk.Frame):

    global userDirectory
    global sUserDirectory
    # 'global' variables to hold selected state of buttons
    bIncludeSubdirs = False
    bPrefix = False
    bSuffix = False
    bInsertB = False
    bInsertA = False
    bReplace = False
    prefix = ""
    suffix = ""
    insertB = ""
    insertA = ""
    replace = ""
    findtext = ""
    # initialize as list types
    subDirList = []
    oldFileList = []
    newFileList = []
    oldFilePathList = []
    newFilePathList = []
    tempFilePathList = []

    # some shit that we do because it's the 'right' way to do things
    def __init__(self):
        super().__init__()

        self.initUI()

    # the main frame
    def initUI(self):

        # declare all functions first
        # function for browsing to a directory
        def BrowseFolder():
            # prompt user
            userDirectory=filedialog.askdirectory()
            sUserDirectory.set(userDirectory)
            # check if user cancelled prompt - this doesn't actually work - not sure what cancelled dialog returns
            if userDirectory is "":
                userDirectory = "nothing selected"
                sUserDirectory.set("")
            # debug print
            #print("userDirectory: " + self.userDirectory)

        # function for getting all files within a directories and its subs
        def getfilelist(directory):
            self.subDirList.clear()
            self.oldFileList.clear()
            self.oldFilePathList.clear()
            self.newFileList.clear()
            self.newFilePathList.clear()
            # clear new file name display
            #snewFileList.set("")
            for subdir, dirs, files in os.walk(directory):
                for file in files:
                    filepath = subdir + os.sep + file
                    # add subdir + ending slash to global subdir variable
                    self.subDirList.append(subdir + os.sep)
                    # add file to global list variable
                    self.oldFileList.append(file)
                    # append null string to keep list the same size
                    self.newFileList.append("")
                    self.oldFilePathList.append(filepath)
                    self.newFilePathList.append("")
                    self.tempFilePathList.append("")
                if not self.bIncludeSubdirs:
                    # if user selected not to include subdirectories,
                    #  break out of loop after going through files
                    break
            # get string list of files to display to the user




            #soldFileList.set("\n".join(str(x) for x in oldFileList))




            # get string list of filepaths to display to the user




            #soldFilePathList.set("\n".join(str(x) for x in oldFilePathList))




            #updatebody(scrollable_body)

        # functions that will get used to rename files
        def saveFile(i):
            os.rename(tempFilePathList[i], newFilePathList[i])

        # function to toggle the relief state of a passed button
        def togglebuttonrelief(btn):
            if btn.config('relief')[-1] == 'sunken':
                btn.config(relief="raised")
            else:
                btn.config(relief="sunken")

        # function to toggle bIncludeSubdirs global boolean and button display state
        def togglebIncludeSubdirs(btn):
            togglebuttonrelief(btn)
            self.bIncludeSubdirs = not self.bIncludeSubdirs
            getfilelist(self.userDirectory)

        # function to toggle bPrefix global boolean and button display state
        def togglebPrefix(btn):
            togglebuttonrelief(btn)
            self.bPrefix = not self.bPrefix

        # function to toggle bSuffix global boolean and button display state
        def togglebSuffix(btn):
            togglebuttonrelief(btn)
            self.bSuffix = not self.bSuffix

        # function to toggle bInsertB global boolean and button display state
        def togglebInsertB(btn):
            togglebuttonrelief(btn)
            self.bInsertB = not self.bInsertB

        # function to toggle bInsertA global boolean and button display state
        def togglebInsertA(btn):
            togglebuttonrelief(btn)
            self.bInsertA = not self.bInsertA

        # function to toggle bReplace global boolean and button display state
        def togglebReplace(btn):
            togglebuttonrelief(btn)
            self.bReplace = not self.bReplace

        def runRenameStuff():
            self.prefix = entryPrefix.get()
            self.suffix = entrySuffix.get()
            self.insertB = entryInsertB.get()
            self.insertA = entryInsertA.get()
            self.replace = entryReplace.get()
            self.findtext = entryFindText.get()
            RenameStuff(self.prefix, self.suffix, self.insertB, self.insertA, self.replace, self.findtext)


        # actual GUI
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
        label2a = Label(frame2, textvariable=sUserDirectory)    #this is not working
        label2a.pack(fill=X, padx=5, expand=True)

        # fourth frame to show options for renaming
        frame4 = Frame(self, borderwidth=50, relief="groove")
        frame4.pack(fill=X)
        frame4a = Frame(frame4, borderwidth=2, relief="solid")
        frame4a.pack(fill=X)
        label4a = Label(frame4a, text="Options:", width=20)
        label4a.pack(side=LEFT, padx=5, pady=5)
        buttonIncludeSubdirs = tk.Button(frame4a, text="Include subdirectories?", width=20, relief="raised",\
                command=lambda: togglebIncludeSubdirs(buttonIncludeSubdirs))
        buttonIncludeSubdirs.pack(side=LEFT)
        buttonStartRenaming = Button(frame4a, text="Rename some shit!", width=20,\
                command=lambda: runRenameStuff())
        buttonStartRenaming.pack(side=RIGHT)
        # create buttons for user to toggle rename functions and create entry boxes for user to provide matching text strings
        # Prefix
        frame4b = Frame(frame4, borderwidth=2, relief="solid")
        frame4b.pack(fill=X)
        buttonPrefix = tk.Button(frame4b, text="Add Prefix", width=12, relief="raised", command=lambda: togglebPrefix(buttonPrefix))
        buttonPrefix.pack(side=LEFT, padx=5)
        entryPrefix = Entry(frame4b)
        entryPrefix.pack(padx=5)
        # Suffix
        frame4c = Frame(frame4, borderwidth=2, relief="solid")
        frame4c.pack(fill=X)
        buttonSuffix = tk.Button(frame4c, text="Add Suffix", width=12, relief="raised", command=lambda: togglebSuffix(buttonSuffix))
        buttonSuffix.pack(side=LEFT, padx=5)
        entrySuffix = Entry(frame4c)
        entrySuffix.pack(padx=5)
        # Insert Before
        frame4d = Frame(frame4, borderwidth=2, relief="solid")
        frame4d.pack(fill=X)
        buttonInsertB = tk.Button(frame4d, text="Insert Before", width=12, relief="raised", command=lambda: togglebInsertB(buttonInsertB))
        buttonInsertB.pack(side=LEFT, padx=5)
        entryInsertB = Entry(frame4d)
        entryInsertB.pack(padx=5)
        # Insert After
        frame4e = Frame(frame4, borderwidth=2, relief="solid")
        frame4e.pack(fill=X)
        buttonInsertA = tk.Button(frame4e, text="Insert After", width=12, relief="raised", command=lambda: togglebInsertA(buttonInsertA))
        buttonInsertA.pack(side=LEFT, padx=5)
        entryInsertA = Entry(frame4e)
        entryInsertA.pack(padx=5)
        # Replace
        frame4f = Frame(frame4, borderwidth=2, relief="solid")
        frame4f.pack(fill=X)
        buttonReplace = tk.Button(frame4f, text="Replace", width=12, relief="raised", command=lambda: togglebReplace(buttonReplace))
        buttonReplace.pack(side=LEFT, padx=5)
        entryReplace = Entry(frame4f)
        entryReplace.pack(padx=5)
        # Text to Find
        frame4g = Frame(frame4, borderwidth=2, relief="solid")
        frame4g.pack(fill=X)
        labelFind = Label(frame4g, text="Text to find (for Insert Before, Insert After, and Replace):")
        labelFind.pack(side=LEFT,padx=5)
        entryFindText = Entry(frame4g)
        entryFindText.pack(padx=5)


def main():
    # main window
    root = Tk()
    # set size of window
    root.geometry("1000x800+300+200")

    #initialize any global variables
    global userDirectory
    # this apparently needs to be here so that labels can access the data
    userDirectory = tk.StringVar()
    #initialize any global variables
    global sUserDirectory
    # this apparently needs to be here so that labels can access the data
    sUserDirectory = tk.StringVar()

    # create frame in root
    app = FileRename()
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
