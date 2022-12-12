import tkinter as tkinter
from tkinter import Toplevel
from UI.Text import *
from Styles import *

class AcercaDe():
    def __init__(self, window):
        super().__init__()

        self.newWindow = Toplevel(window)
        self.newWindow.resizable(0,0)
        self.newWindow.title("Acerca de")
        self.newWindow.geometry("650x500")

        self.titulo = Text("Inteligencia Artificial - 2022")
        self.titulo.createUI(self.newWindow, ("Arial Bold", 25))
        self.titulo.setLocation(100, 40)

        self.subTitutlo = Text("Aplicación Perceptrón Multicapa")
        self.subTitutlo.createUI(self.newWindow, ("Arial Bold", 20))
        self.subTitutlo.setLocation(120, 120)

        self.texto = Text("Desarrollado por:")
        self.texto.createUI(self.newWindow, ("Arial Bold", 15))
        self.texto.setLocation(200, 200)

        integrantes = ["Perez, Antonella", "Perez, Estefania", "Quetglas, Victoria", "Rojas, Mauro"]
        posicionY = 260
        for item in integrantes:
            self.texto = Text("- " + item)
            self.texto.createUI(self.newWindow, ("Arial Bold", 12))
            self.texto.setLocation(200, posicionY)
            posicionY += 50
