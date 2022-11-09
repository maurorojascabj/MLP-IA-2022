import tkinter as tkinter
from tkinter.ttk import Combobox

class SelectMultiple(Combobox):
    def __init__(self, window) -> None:
        self.currentValue = tkinter.StringVar()
        Combobox.__init__(self)
        self.comboBox = Combobox(window)
        self.config(textvariable = self.currentValue)
        self.textvariable = self.currentValue
    
    def setWidth(self, valor):
        self.comboBox.config(width=valor)


    def generateValues(self, inicialValue, finalValue, type):
        self.values = []
        for x in range(inicialValue, finalValue+1):
            if type == "percent":
                self.values.append(str(x)+'%')
            else:
                self.values.append(str(x))

        return self.values
    
    def setValues(self, inicialValue=1, finalValue=30, type="percent"):
        self.comboBox['values'] = self.generateValues(inicialValue, finalValue, type)
        self.comboBox.current(0)
    
    def setLocation(self, positionX, positionY):
        self.place = self.comboBox.place(x=positionX, y=positionY)

    def getValues(self):
        return self.comboBox.get()
    
