import tkinter as tk
from tkinter import Tk, Canvas, Scrollbar, Menu, Text, TOP, BOTH, RIGHT, X, N, LEFT
from tkinter import ttk
from tkinter.ttk import Frame, Button, Style, Label, Entry
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

        header = ttk.Frame(frame1)
        body = ttk.Frame(frame1)
        footer = ttk.Frame(frame1)
        header.pack()
        body.pack()
        footer.pack()

        ttk.Label(header, text="The header").pack()
        ttk.Label(footer, text="The Footer").pack()


        scrollable_body = Scrollable(body, width=32)

        for i in range(30):
            ttk.Button(scrollable_body, text="I'm a button in the scrollable frame" + str(i+1)).grid()

        scrollable_body.update()


class Scrollable(ttk.Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame,
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16):

        scrollbar = tk.Scrollbar(frame, width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=True)

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


root = tk.Tk()

# create frame in root
app = Example()


root.mainloop()
