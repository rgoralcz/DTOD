

# the frame class?
class Example(Frame):





    def initUI(self):








        # function to rename a list of files
        # will need booleans for insert before, insert after, replace, prefix, suffix
        # will need to access global file name/path lists
        def RenameStuff(sPrefix, sSuffix, sInsertB, sInsertA, sReplace, texttofind):
            # get directory again in case user is running renameStuff again without re-browsing to folders
            global userdirectory
            getfilelist(userdirectory)
            global tempfilepathlist
            global oldfilelist
            global oldfilepathlist
            global subdirlist
            global resavefile
            tempfilename = ""

            # if user selected to insert or replace text, need to find the provided string
            bFind = False
            if Example.bInsertB or Example.bInsertA or Example.bReplace:
                bFind = True
            # loop through all items in the file list
            for item in oldfilelist:
                # get index position of item in oldfilelist to crossreference with other file lists
                indexposn = oldfilelist.index(item)
                basefilename = os.path.splitext(item)[0]
                basefileext = os.path.splitext(item)[1]
                # if required to find text for replacement or insertion, do so
                tempfilename = basefilename
                tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
                if bFind:
                    textposn = item.find(texttofind)
                    # if the provided text was found, do replacement or insertion as necessary
                    if textposn > -1:
                        # if user chose to insert after text, do so
                        if Example.bInsertA:
                            textposn = tempfilename.find(texttofind)
                            textleft = tempfilename[0:textposn+len(texttofind)]
                            textposnend = textposn + len(texttofind)
                            textright = tempfilename[textposnend:len(tempfilename)]
                            tempfilename = textleft + sInsertA + textright
                            newfilelist[indexposn] = tempfilename
                            newfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
                            saveFile(indexposn)
                            tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext

                        # if user chose to insert before text, do so
                        if Example.bInsertB:
                            textposn = tempfilename.find(texttofind)
                            textleft = tempfilename[0:textposn]
                            textposnend = textposn
                            textright = tempfilename[textposnend:len(tempfilename)]
                            tempfilename = textleft + sInsertB + textright
                            newfilelist[indexposn] = tempfilename
                            newfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
                            saveFile(indexposn)
                            tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext

                        # if user chose to replace text, do so
                        if Example.bReplace:
                            textposn = tempfilename.find(texttofind)
                            textleft = tempfilename[0:textposn]
                            textposnend = textposn + len(texttofind)
                            textright = tempfilename[textposnend:len(tempfilename)]
                            tempfilename = textleft + sReplace + textright
                            newfilelist[indexposn] = tempfilename
                            newfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
                            saveFile(indexposn)
                            tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext

                # if user chose to add suffix, do so
                if Example.bSuffix:
                    tempfilename = tempfilename + sSuffix
                    newfilelist[indexposn] = tempfilename
                    newfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
                    saveFile(indexposn)
                    tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext

                # if user chose to add prefix, do so
                if Example.bPrefix:
                    tempfilename = sPrefix + tempfilename
                    newfilelist[indexposn] = tempfilename
                    newfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext
                    saveFile(indexposn)
                    tempfilepathlist[indexposn] = subdirlist[indexposn] + tempfilename + basefileext

                snewfilelist.set("\n".join(str(x) for x in newfilelist))








        def updatebody(bdy):
            bdy.update()














        # third frame to show file information
        frame3 = Frame(self, borderwidth=10, relief="groove", height=200)
        frame3.pack(fill=BOTH, expand=True, padx=10, pady=10)
        scrollable_body = Scrollable(frame3, width=32)
        # sub frame on the left to show filenames
        frame3a = Frame(scrollable_body, borderwidth=2, relief="sunken")
        frame3a.pack(side=LEFT, fill=BOTH, expand=True)
        label3a1 = Label(frame3a, text="Old File Name List", width=20, anchor="center", borderwidth=2, relief="solid")
        label3a1.pack(anchor="center", padx=5, pady=5)
        label3a2 = Label(frame3a, textvariable=soldfilelist)
        label3a2.pack(padx=2, pady=5)
        # sub frame in the middle to show new filenames
        frame3b = Frame(scrollable_body, borderwidth=2, relief="raised")
        frame3b.pack(side=LEFT, fill=BOTH, expand=True)
        label3b1 = Label(frame3b, text="New File Name", width=20, anchor="center", borderwidth=2, relief="solid")
        label3b1.pack(anchor="center", padx=5, pady=5)
        label3b2 = Label(frame3b, textvariable=snewfilelist)
        label3b2.pack(padx=2, pady=5)
        # sub frame on the right to show filenames with paths
        frame3c = Frame(scrollable_body, borderwidth=2, relief="solid")
        frame3c.pack(side=LEFT, fill=BOTH, expand=True)
        label3c1 = Label(frame3c, text="File Path List", width=15, anchor="center", borderwidth=2, relief="solid")
        label3c1.pack(anchor="center", padx=5, pady=5)
        label3c2 = Label(frame3c, textvariable=soldfilepathlist)
        label3c2.pack(padx=2, pady=5)


        scrollable_body.update()


class Scrollable(ttk.Frame):
    #"""
    #   Make a frame scrollable with scrollbar on the right.
    #   After adding or removing widgets to the scrollable frame,
    #   call the update() method to refresh the scrollable area.
    #"""

    def __init__(self, frame, width=30):

        scrollbar = tk.Scrollbar(frame, width=30)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame)

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)


    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)

    def update(self):
        "Update the canvas and the scrollregion"

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))


def main():


    # initialize a bunch of global variables




    # global variable to hold string list of files found
    global soldfilelist
    # this apparently needs to be here so that labels can access the data
    soldfilelist = tk.StringVar()
    # global variable to hold string list of files found
    global snewfilelist
    # this apparently needs to be here so that labels can access the data
    snewfilelist = tk.StringVar()
    # global variable to hold string list of files found
    global soldfilepathlist
    # this apparently needs to be here so that labels can access the data
    soldfilepathlist = tk.StringVar()
    # global variable to hold string list of files found
    global snewfilepathlist
    # this apparently needs to be here so that labels can access the data
    snewfilepathlist = tk.StringVar()
