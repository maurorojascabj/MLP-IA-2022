import tkinter as tkinter
from tkinter import messagebox


class Dialog():
    def __init__(self, tipo, titulo, cuerpo):
        super().__init__()
        self.tipo = tipo
        self.titulo = titulo
        self.cuerpo = cuerpo

        if(self.tipo == "warning"):
            self.warning = messagebox.showwarning(self.titulo, self.cuerpo)
        elif(self.tipo == "info"):
            self.info = messagebox.showinfo(self.titulo, self.cuerpo)
        elif(self.tipo == "error"):
            self.error = messagebox.showerror(self.titulo, self.cuerpo)
    
    
    def getDialog(self):
        if(self.tipo == "warning"):
            return self.warning
        elif(self.tipo == "info"):
            return self.info
        elif(self.tipo == "error"):
            return self.error