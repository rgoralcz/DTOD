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

from tkinter import Tk, Text, TOP, BOTH, RIGHT, X, N, LEFT
from tkinter.ttk import Frame, Button, Style, Label, Entry


def close_window():
    root.destroy()

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
        lbl1 = Label(frame1, text="Title", width=10)
        lbl1.pack(side=LEFT, padx=5, pady=5)
        entry1 = Entry(frame1)
        entry1.pack(fill=X, padx=5, expand=True)

        # second frame
        frame2 = Frame(self, borderwidth=20, relief="solid")
        frame2.pack(fill=X)
        lbl2 = Label(frame2, text="Author", width=10)
        lbl2.pack(side=LEFT, padx=5, pady=5)
        entry2 = Entry(frame2)
        entry2.pack(fill=X, padx=5, expand=True)

        # third frame
        frame3 = Frame(self, borderwidth=30, relief="solid")
        frame3.pack(fill=BOTH, expand=True)
        lbl3 = Label(frame3, text="Review", width=10)
        lbl3.pack(side=LEFT, anchor=N, padx=5, pady=5)
        #lbl3.pack(side=LEFT, padx=5, pady=5)
        revtxt = Text(frame3, height=5)
        revtxt.pack(fill=BOTH, expand=True, pady=5, padx=5)

        # fourth frame
        frame4 = Frame(self, borderwidth=1, relief="solid")
        frame4.pack(fill=X, expand=False, anchor=N)
        lbl4 = Label(frame4, text="Close Button Frame", width=10)
        lbl4.pack(side=LEFT, anchor=N, padx=5, pady=5)
        buttonClose = Button(frame4, text="Close", width=30, command=close_window)
        buttonClose.pack(side=RIGHT)

def main():

    root = Tk()
    #root.geometry("800x400+300+300")
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
