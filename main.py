import tkinter as tkinter
from tkinter import *
from UI.Text import *
from Styles import *
from Screens.Inicio import *
from Screens.AcercaDe import *



window = tkinter.Tk()

def irInicio():
    inicio = Inicio(window)

def abrirAcercaDe():
    acercaDe = AcercaDe(window)


#MenuBar
menuBar = tkinter.Menu()
window.config(menu=menuBar)
menuPrincipal = tkinter.Menu(menuBar, tearoff=False)
menuAyuda = tkinter.Menu(menuBar, tearoff=False)

menuBar.add_cascade(menu=menuPrincipal, label="Menú")
menuBar.add_cascade(menu=menuAyuda, label="Ayuda")
##Submenues menu principal
menuPrincipal.add_command(label="Inicio", command=lambda: irInicio())
menuPrincipal.add_separator()
menuPrincipal.add_command(label="Salir", command=window.quit)
##Submenues menu ayuda
menuAyuda.add_command(label="Acerca de...", command=lambda: abrirAcercaDe())

title = Text("Perceptrón Multicapa")
title.createUI(window, ("Arial Bold", 30))
title.setLocation(titleMainStyles["coordenadaX"], titleMainStyles["coordenadaY"])

inicio = Inicio(window)

window.resizable(0,0)
window.title("Perceptrón multicapa")
window.geometry("1500x750")
window.mainloop()