import tkinter as tkinter
from tkinter.ttk import Button, Combobox, Label, Radiobutton
from tkinter import *
from UI.FrameUI import *
from UI.Cell import *
from UI.Pattern import *
from UI.Text import *
from UI.SelectMultiple import *
from Styles import *
from utils import matrizStringToArrayInt, generateRandom
from Menu.Configuracion import *
from Screens.Red import *
from Screens.Entrenamiento import *


window = tkinter.Tk()

def openPantallaRedDePrueba():
    red = Red(window)

#MenuBar
menuBar = tkinter.Menu()
window.config(menu=menuBar)
menuPrincipal = tkinter.Menu(menuBar, tearoff=False)
menuAyuda = tkinter.Menu(menuBar, tearoff=False)
menuEntrenamiento = tkinter.Menu(menuBar, tearoff=False)
menuRedDePrueba = tkinter.Menu(menuBar, tearoff=False)
menuBar.add_cascade(menu=menuPrincipal, label="Menú")
menuBar.add_cascade(menu=menuEntrenamiento, label="Entrenamiento")
menuBar.add_cascade(menu=menuRedDePrueba, label="Red de prueba")
menuRedDePrueba.add_command(label="Inicio", command=openPantallaRedDePrueba)
menuBar.add_cascade(menu=menuAyuda, label="Ayuda")
# config = Configuracion(menuBar)
##Submenues menu principal
menuPrincipal.add_command(label="Inicio")
menuPrincipal.add_separator()
menuPrincipal.add_command(label="Salir", command=window.quit)
##Submenues menu ayuda
menuAyuda.add_command(label="Acerca de...")

title = Text("Perceptron Multicapa")
title.createUI(window, ("Arial Bold", 30))
title.setLocation(titleMainStyles["coordenadaX"], titleMainStyles["coordenadaY"])

def mostrarPantallaUsarRed():
    botonUsarRed.destroy()
    botonCrearRed.destroy()
    red = Red(window)

def mostrarPantallaCrearRed():
    botonUsarRed.destroy()
    botonCrearRed.destroy()
    red = Entrenamiento(window)

botonUsarRed = Button(window, text="Utilizar red", command=lambda: mostrarPantallaUsarRed())
botonUsarRed.configure(width=botonUsarRedStyles["width"], height=botonUsarRedStyles["height"], bg=botonUsarRedStyles["bg"], font=("Arial Bold", 15))
botonUsarRed.place(x=botonUsarRedStyles["coordenadaX"], y=botonUsarRedStyles["coordenadaY"])     

botonCrearRed = Button(window, text="Crear red", command=lambda: mostrarPantallaCrearRed())
botonCrearRed.configure(width=botonCrearRedStyles["width"], height=botonUsarRedStyles["height"], bg=botonCrearRedStyles["bg"], font=("Arial Bold", 15))
botonCrearRed.place(x=botonCrearRedStyles["coordenadaX"], y=botonCrearRedStyles["coordenadaY"]) 


window.resizable(0,0)
window.title("Perceptrón multicapa")
window.geometry("1500x750")
window.mainloop()

# return [datosEntradas, nueva matriz distorsionada]
        #datosEntradas= []

        ##
        # Agregar campo validación 
        # Agregar selección dataset
        # Nueva pantalla para redes ya entrenadas
        # Ver de agregar un loading cuando la red está entrenando
        #
        ##