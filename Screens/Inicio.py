import tkinter as tkinter
from tkinter.ttk import Button, Combobox, Label, Radiobutton
from tkinter import *
from UI.Text import *
from Styles import *
from Screens.Red import *
from Screens.Entrenamiento import *


class Inicio():
    def __init__(self, window):
        super().__init__()
        self.window = window    

        self.frameContenedor = FrameUI(window, 0)
        self.frameContenedor.setLocation(200, 100)
        self.frameContenedor.config(width=1100, height=700)

        self.botonUsarRed = Button(self.frameContenedor, text="Utilizar red", command=lambda: self.mostrarPantallaUsarRed())
        self.botonUsarRed.configure(width=botonUsarRedStyles["width"], height=botonUsarRedStyles["height"], bg=botonUsarRedStyles["bg"], font=("Arial Bold", 15))
        self.botonUsarRed.place(x=botonUsarRedStyles["coordenadaX"], y=botonUsarRedStyles["coordenadaY"])     

        self.botonCrearRed = Button(self.frameContenedor, text="Crear red", command=lambda: self.mostrarPantallaCrearRed())
        self.botonCrearRed.configure(width=botonCrearRedStyles["width"], height=botonUsarRedStyles["height"], bg=botonCrearRedStyles["bg"], font=("Arial Bold", 15))
        self.botonCrearRed.place(x=botonCrearRedStyles["coordenadaX"], y=botonCrearRedStyles["coordenadaY"]) 


    def mostrarPantallaUsarRed(self):
        self.botonUsarRed.destroy()
        self.botonCrearRed.destroy()
        red = Red_UI(self.window)

    def mostrarPantallaCrearRed(self):
        self.botonUsarRed.destroy()
        self.botonCrearRed.destroy()
        red = Entrenamiento(self.window)


