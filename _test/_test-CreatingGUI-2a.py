#fumbling around with someone else's example and trying to beat it into submission

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode Tkinter tutorial

In this example, we use the pack
manager to create a review example.

Author: Jan Bodnar
Last modified: July 2017
Website: www.zetcode.com

!!!! modified to learn how to use Frames
"""

# I don't actually understand the difference between the first two import items
import tkinter as tk
from tkinter import Tk, Menu, Text, TOP, BOTH, RIGHT, X, N, LEFT
from tkinter.ttk import Frame, Button, Style, Label, Entry
# library for browsing to file loctions
from tkinter import filedialog

# function to destroy a frame passed to it
def close_window(tempobj):
    tempobj.destroy()

# function for browsing to the pdf file locaitons
def BrowseFolder():
    # prompt user
    directory=filedialog.askdirectory()
    # set the global varriable to the filepath received
    # print ("directory = " + directory)
    folderPath.set(directory)


class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Review")
        # main window
        self.pack(fill=BOTH, expand=True,padx=5,pady=5)

        # first frame
        frame1 = Frame(self, borderwidth=10, relief="solid")
        frame1.pack(fill=X)
        lbl1a = Label(frame1, text="Click to the right to browse to your PDF file locations.", width=50)
        lbl1a.pack(side=LEFT, padx=5, pady=5)
        buttonBrowseFolder = Button(frame1, text="Browse to Folder", width=30, command=lambda: BrowseFolder())
        buttonBrowseFolder.pack(side=RIGHT)
        #lbl1b = Label(frame1, text="Title", width=10)
        #lbl1b.pack(side=RIGHT, padx=5, pady=5)
        #entry1 = Entry(frame1)
        #entry1.pack(fill=X, padx=5, expand=True)

        # second frame
        frame2 = Frame(self, borderwidth=20, relief="solid")
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Directory Selected:", width=20)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        lbl2a = Label(frame2, textvariable=folderPath)
        lbl2a.pack(fill=X, padx=5, expand=True)

        # third frame
        frame3 = Frame(self, borderwidth=30, relief="solid")
        frame3.pack(fill=BOTH, expand=True)
        lbl3 = Label(frame3, text="Review", width=10)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)
        #lbl3.pack(side=LEFT, padx=5, pady=5)
        revtxt = Text(frame3, height=5)
        revtxt.pack(fill=BOTH, expand=True, pady=5, padx=5)

        # fourth frame
        #frame4 = Frame(self, borderwidth=1, relief="solid")
        #frame4.pack(fill=X, expand=False, anchor=N)
        #lbl4 = Label(frame4, text="Close Button Frame", width=10)
        #lbl4.pack(side=LEFT, anchor=N, padx=5, pady=5)
        #buttonClose = Button(frame4, text="Close", width=30, command=self.destroy)
        #buttonClose = Button(frame4, text="Close", width=30, command=lambda: close_window(rootwindow))
        #buttonClose.pack(side=RIGHT)


def main():

    # main window
    root = Tk()
    # set size of window
    root.geometry("600x400")
    # declare global variable to make the data available
    global folderPath
    # This apparently needs to be here so that label2 can access the data
    folderPath = tk.StringVar()
    # create frame in root
    app = Example()
    # a button to close root
    button = tk.Button(root, text="Close", width=15, command=root.destroy)
    # tacking the close button to the end of root
    button.pack(pady=15)
    # end main
    root.mainloop()


if __name__ == '__main__':
    main()
