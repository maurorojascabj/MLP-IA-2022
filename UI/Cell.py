from tkinter import Label, SOLID

class Cell(Label):
    
    def __init__(self, frame, widthCell, heightCell, color=None):
        super().__init__(
            master=frame,
            width=widthCell,
            height=heightCell,
            relief=SOLID,
            bd=1,
            bg=color
        )


    def setLocation(self, positionX, positionY):
        self.grid(row=positionX, column=positionY, sticky="nsew")
    