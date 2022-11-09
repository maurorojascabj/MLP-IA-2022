import tkinter as tkinter

class Text(tkinter.Label):
    def __init__(self, text) -> None:
        tkinter.Label.__init__(self)
        self.title = text
    
    def createUI(self, window, font=None):
        self.textUI = tkinter.Label(window, text=self.title, font=font)

    def setLocation(self, positionX, positionY):
        self.place = self.textUI.place(x=positionX, y=positionY)