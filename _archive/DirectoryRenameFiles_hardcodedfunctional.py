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
    global directory
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
    oldfilepathlist.clear()
    newfilelist.clear()
    newfilepathlist.clear()
    resavefile.clear()
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
            # append null string to keep list the same siez
            newfilelist.append("")
            # add filepath to global list variable
            #  this is returning mixed slashes, annoyingly
            #   while these don't affect function (I think), could do a find & replace for consistency
            oldfilepathlist.append(filepath)
            newfilepathlist.append("")
            tempfilepathlist.append("")
            # add new list entry for resavefile
            resavefile.append(False)
    # get string list of files to display to the user
    soldfilelist.set("\n".join(str(x) for x in oldfilelist))
    # get string list of filepaths to display to the user
    soldfilepathlist.set("\n".join(str(x) for x in oldfilepathlist))


# function to rename a list of files
# will need booleans for insert before, insert after, replace, prefix, suffix
# will need to access global file name/path lists
def RenameStuff():
    global getoldfilelist
    # get directory again in case user is running renameStuff again without re-browsing to folders
    global directory
    getoldfilelist(directory)
    #debug message
    print ("RenameStuff called\n")
    global bPrefix
    global bSuffix
    global bInsertB
    global bInsertA
    global bReplace
    global texttofind
    global Prefix

    global tempfilepathlist
    global oldfilelist
    global oldfilepathlist
    global subdirlist
    global resavefile
    # testing hardcoded value
    texttofind = "frame"
    # testing suffix
    sSuffix = "_TESTSUFFIX"
    # testing prefix
    sPrefix = "TESTPREFIX_"
    # testing insert
    sInsertA = "-InsertedAfter-"
    # testing insert
    sInsertB = "-InsertedBefore-"
    # testing replace
    sReplace = "-ReplacedText-"
    # initialize tempfilename as string
    tempfilename = ""

    # if user selected to insert or replace text, need to find the provided string
    bFind = False
    print ("bFind: " + str(bFind))
    if bInsertB or bInsertA or bReplace:
        bFind = True
    print ("bFind: " + str(bFind))
    # loop through all items in the file list
    for item in oldfilelist:
        print ()
        # get index position of item in oldfilelist to crossreference with other file lists
        indexposn = oldfilelist.index(item)
        basefilename = os.path.splitext(item)[0]
        basefileext = os.path.splitext(item)[1]
        #debug message
        print ("On item number " + str(indexposn) + " which is " + basefilename)
        # if required to find text for replacement or insertion, do so
        tempfilename = basefilename
        tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
        if bFind:
            textposn = item.find(texttofind)
            # if the provided text was found, do replacement or insertion as necessary
            if textposn > -1:
                #debug messages
                #print ("Found : " + texttofind + " in " + basefilename + " at position " + str(textposn))
                #print (oldfilepathlist[int(indexposn)])
                #print (subdirlist[int(indexposn)])
                #set boolean for whether or not to resave the file
                resavefile[indexposn] = True
                # if user chose to insert after text, do so
                if bInsertA:
                    textposn = tempfilename.find(texttofind)
                    #debug messages
                    #print ("inserting text after " + texttofind + " in " + basefilename)
                    textleft = tempfilename[0:textposn+len(texttofind)]
                    textposnend = textposn + len(texttofind)
                    textright = tempfilename[textposnend:len(tempfilename)]
                    #print ("textleft: " + textleft + " || adding: " + sInsertA + " || textright: " + textright)
                    tempfilename = textleft + sInsertA + textright
                    #print (basefilename + " is now " + tempfilename)
                    newfilelist[indexposn] = tempfilename
                    #print ("newfilelist[indexposn]: " + str(newfilelist[indexposn]))
                    newfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
                    #print ("newfilepathlist[indexposn]: " + str(newfilepathlist[indexposn]))
                    saveFile(indexposn)
                    #os.rename(oldfilepathlist[indexposn], newfilepathlist[indexposn])
                    tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext

                # if user chose to insert before text, do so
                if bInsertB:
                    textposn = tempfilename.find(texttofind)
                    #debug messages
                    #print ("inserting text before " + texttofind + " in " + basefilename)
                    textleft = tempfilename[0:textposn]
                    textposnend = textposn
                    textright = tempfilename[textposnend:len(tempfilename)]
                    #print ("textleft: " + textleft + " || adding: " + sInsertB + " || textright: " + textright)
                    tempfilename = textleft + sInsertB + textright
                    #print (basefilename + " is now " + tempfilename)
                    newfilelist[indexposn] = tempfilename
                    #print ("newfilelist[indexposn]: " + str(newfilelist[indexposn]))
                    newfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
                    #print ("newfilepathlist[indexposn]: " + str(newfilepathlist[indexposn]))
                    saveFile(indexposn)
                    #os.rename(oldfilepathlist[indexposn], newfilepathlist[indexposn])
                    tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext

                # if user chose to replace text, do so
                if bReplace:
                    textposn = tempfilename.find(texttofind)
                    #debug messages
                    #print ("replacing text " + texttofind + " in " + basefilename)
                    textleft = tempfilename[0:textposn]
                    textposnend = textposn + len(texttofind)
                    textright = tempfilename[textposnend:len(tempfilename)]
                    #print ("textleft: " + textleft + " || adding: " + sReplace + " || textright: " + textright)
                    tempfilename = textleft + sReplace + textright
                    #print (basefilename + " is now " + tempfilename)
                    newfilelist[indexposn] = tempfilename
                    #print ("newfilelist[indexposn]: " + str(newfilelist[indexposn]))
                    newfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
                    #print ("newfilepathlist[indexposn]: " + str(newfilepathlist[indexposn]))
                    saveFile(indexposn)
                    #os.rename(oldfilepathlist[indexposn], newfilepathlist[indexposn])
                    tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext

        # if user chose to add suffix, do so
        if bSuffix:
            # mark file posn to be resaved
            resavefile[indexposn] = True
            #debug messages
            #print (oldfilepathlist[indexposn])
            #print ("adding suffix to " + basefilename)
            tempfilename = tempfilename + sSuffix
            #print (basefilename + " is now " + tempfilename)
            newfilelist[indexposn] = tempfilename
            #print ("newfilelist[indexposn]: " + str(newfilelist[indexposn]))
            newfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
            #print ("newfilepathlist[indexposn]: " + str(newfilepathlist[indexposn]))
            saveFile(indexposn)
            #os.rename(oldfilepathlist[indexposn], newfilepathlist[indexposn])
            tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext

        # if user chose to add prefix, do so
        if bPrefix:
            # mark file posn to be resaved
            resavefile[indexposn] = True
            #debug messages
            #print ("adding prefix to " + basefilename)
            tempfilename = sPrefix + tempfilename
            newfilelist[indexposn] = tempfilename
            #print ("newfilelist[indexposn]: " + str(newfilelist[indexposn]))
            newfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
            #print ("newfilepathlist[indexposn]: " + str(newfilepathlist[indexposn]))
            saveFile(indexposn)
            #os.rename(oldfilepathlist[indexposn], newfilepathlist[indexposn])
            tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext

        #debug message
        #print ("resavefile is " + str(resavefile[indexposn]) + " for " + str(item))
        # finally, save file with new filename
        #if resavefile[indexposn]:
            #os.rename(src, dst)

        snewfilelist.set("\n".join(str(x) for x in newfilelist))
        # update string list of filepaths that is displayed to the user
        #soldfilepathlist.set("\n".join(str(x) for x in newfilepathlist))

    print()
    print("done renaming stuff")


def saveFile(i):
    global oldfilepathlist
    global newfilepathlist
    os.rename(tempfilepathlist[i], newfilepathlist[i])

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


# function to toggle bPrefix global boolean and button display state
def togglebPrefix(btn):
    global bPrefix
    togglebuttonrelief(btn)
    bPrefix = not bPrefix
    #print (str(type(bPrefix)) + " - bPrefix is now: " + str(bPrefix))

# function to toggle bSuffix global boolean and button display state
def togglebSuffix(btn):
    global bSuffix
    togglebuttonrelief(btn)
    bSuffix = not bSuffix
    #print (str(type(bSuffix)) + " - bSuffix is now: " + str(bSuffix))

# function to toggle bInsertB global boolean and button display state
def togglebInsertB(btn):
    global bInsertB
    togglebuttonrelief(btn)
    bInsertB = not bInsertB
    #print (str(type(bInsertB)) + " - bInsertB is now: " + str(bInsertB))

# function to toggle bInsertA global boolean and button display state
def togglebInsertA(btn):
    global bInsertA
    togglebuttonrelief(btn)
    bInsertA = not bInsertA
    #print (str(type(bInsertA)) + " - bInsertA is now: " + str(bInsertA))

# function to toggle bReplace global boolean and button display state
def togglebReplace(btn):
    global bReplace
    togglebuttonrelief(btn)
    bReplace = not bReplace
    #print (str(type(bReplace)) + " - bReplace is now: " + str(bReplace))


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
        frame4 = Frame(self, borderwidth=50, relief="groove")
        frame4.pack(fill=X)
        frame4a = Frame(frame4, borderwidth=2, relief="solid")
        frame4a.pack(fill=X)
        label4a = Label(frame4a, text="Options:", width=20)
        label4a.pack(side=LEFT, padx=5, pady=5)
        buttonStartRenaming = Button(frame4a, text="Rename some shit!", width=20,\
                command=lambda: RenameStuff())
        buttonStartRenaming.pack(side=RIGHT)
        frame4b = Frame(frame4, borderwidth=2, relief="solid")
        frame4b.pack(fill=X)
        frame4c = Frame(frame4, borderwidth=2, relief="solid")
        frame4c.pack(fill=X)
        frame4d = Frame(frame4, borderwidth=2, relief="solid")
        frame4d.pack(fill=X)
        frame4e = Frame(frame4, borderwidth=2, relief="solid")
        frame4e.pack(fill=X)
        frame4f = Frame(frame4, borderwidth=2, relief="solid")
        frame4f.pack(fill=X)
        # start creating buttons for user to toggle rename functions
        buttonPrefix = tk.Button(frame4b, text="Add Prefix", width=12, relief="raised", command=lambda: togglebPrefix(buttonPrefix))
        buttonPrefix.pack(side=LEFT, padx=5)
        buttonSuffix = tk.Button(frame4c, text="Add Suffix", width=12, relief="raised", command=lambda: togglebSuffix(buttonSuffix))
        buttonSuffix.pack(side=LEFT, padx=5)
        buttonInsertB = tk.Button(frame4d, text="Insert Before", width=12, relief="raised", command=lambda: togglebInsertB(buttonInsertB))
        buttonInsertB.pack(side=LEFT, padx=5)
        buttonInsertA = tk.Button(frame4e, text="Insert After", width=12, relief="raised", command=lambda: togglebInsertA(buttonInsertA))
        buttonInsertA.pack(side=LEFT, padx=5)
        buttonReplace = tk.Button(frame4f, text="Replace", width=12, relief="raised", command=lambda: togglebReplace(buttonReplace))
        buttonReplace.pack(side=LEFT, padx=5)

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
        label3c2 = Label(frame3c, textvariable=soldfilepathlist)
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
    root.geometry("800x600+300+200")

    # initialize a bunch of global variables

    # declare global directory to make it available in the rename function
    global directory
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
    global oldfilepathlist
    # initialize as list type
    oldfilepathlist = []
    # global variable to hold string list of files found
    global soldfilepathlist
    # this apparently needs to be here so that labels can access the data
    soldfilepathlist = tk.StringVar()
    global newfilepathlist
    # initialize as list type
    newfilepathlist = []
    # global variable to hold string list of files found
    global snewfilepathlist
    # this apparently needs to be here so that labels can access the data
    snewfilepathlist = tk.StringVar()
    # global variable to hold temporary list of file paths as files are renamed
    global tempfilepathlist
    tempfilepathlist = []

    # global variable to hold selected state of Add Prefix button
    global bPrefix
    bPrefix = False
    global bSuffix
    bSuffix = False
    global bInsertB
    bInsertB = False
    global bInsertA
    bInsertA = False
    global bReplace
    bReplace = False

    # global variable to hold booleans for whether or not to resave a file
    global resavefile
    # initialize as list type
    resavefile = []


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
