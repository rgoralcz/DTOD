# I don't actually understand the difference between the first two import items
import tkinter as tk
from tkinter import Tk, Menu, Text, TOP, BOTH, RIGHT, X, N, LEFT
from tkinter.ttk import Frame, Button, Style, Label, Entry


# test function
def DoSomething(req):
    print ("DoSomething called")


# function to toggle the relief state of a passed button
def togglebuttonrelief(btn):

    if btn.config('relief')[-1] == 'sunken':
        btn.config(relief="raised")
    else:
        btn.config(relief="sunken")


# the frame class?
class Example(Frame):

    # some shit that we do because it's the 'right' way to do things
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Using Buttons")
        # main window
        self.pack(fill=BOTH, expand=True,padx=5,pady=5)

        # frame to show intent
        frametemp = Frame(self, borderwidth=5, relief="solid")
        frametemp.pack(fill=X)
        labeltemp = Label(frametemp, text="Example", width=20, anchor="center")
        labeltemp.pack(padx=5, pady=5)
        # frame to show button calling function
        frame4 = Frame(self, borderwidth=5, relief="solid")
        frame4.pack(fill=X)
        frame4a = Frame(frame4, borderwidth=2, relief="solid")
        frame4a.pack(fill=X)
        label4 = Label(frame4a, text="Section Title:", width=20, anchor="center")
        label4.pack(side=LEFT, padx=5, pady=5)
        buttonStartRenaming = Button(frame4a, text="Test Function!", width=20,\
                command=lambda: DoSomething(False))
        buttonStartRenaming.pack(side=RIGHT)
        frame4b = Frame(frame4, borderwidth=2, relief="solid")
        frame4b.pack(fill=X)
        # start creating buttons for user to toggle rename functions
        buttontoggle = tk.Button(frame4b, text="Toggle Me Silly", relief="raised",\
                width=20, command=lambda: togglebuttonrelief(buttontoggle))
        buttontoggle.pack(side=RIGHT)


def main():

    # main window
    root = Tk()
    # set size of window
    root.geometry("600x200+300+200")
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
