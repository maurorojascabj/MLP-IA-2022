from tkinter import Frame, SUNKEN

class FrameUI(Frame):
    def __init__(self, window, border = 1):
        super().__init__(
            master=window,
            relief=SUNKEN,
            borderwidth=border
        )  # Initialize superclass
        self.master = window
        self.pack()
    
    def setLocation(self, positionX, positionY):
        self.place(x=positionX, y=positionY)