import tkinter as tkinter
from tkinter import Button, ttk
from Styles import *
from Screens.Red_UI import *
from Screens.SeleccionPatron import *
from UI.FrameUI import *
from UI.Text import *


#Importamos librerias pandas y matplotlib
import pandas as pd 
import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tratamiento_datasets import errores_por_epoca


class GraficoErroresEntrenamiento():
    def __init__(self, window, frameRed = None, archivo_errores=None,dataRed = None):
        super().__init__()
        self.window = window
        self.frameRed = frameRed
        self.dataRed = dataRed
       

        self.frameContenedor = FrameUI(window, 0)
        self.frameContenedor.setLocation(100, 100)
        self.frameContenedor.config(width=1100, height=700)

        # Usamos la funcionalidad de TkAgg para acoplar a Tkinter
        matplotlib.use("TkAgg")

        # Creamos un figura
        self.figure = Figure(figsize=(10, 5))

        #Leer archivo de errores y obtenemos la data
        archivo = archivo_errores
        errores_epoca = errores_por_epoca.leer_archivo_errores(archivo)[0]
        exactitud_entrenamiento = errores_por_epoca.leer_archivo_errores(archivo)[1]
        exactitud_validacion = errores_por_epoca.leer_archivo_errores(archivo)[2]
    
        
        #Creamos un array para cada data
        epoca = []
        error_entrenamiento = []
        error_validacion = []
        for item in errores_epoca:
            epoca.append(str(item[0]))
            error_entrenamiento.append(item[1])
            error_validacion.append(item[2])

        #Creamos un Dataframe con los datos a renderizar
        self.df = pd.DataFrame({'Épocas': epoca, 'Entrenamiento': error_entrenamiento, 'Validación': error_validacion})
        self.ax = self.figure.subplots()
        self.df.plot(x = 'Épocas', y = 'Entrenamiento', ax = self.ax)
        self.df.plot(x = 'Épocas', y = 'Validación', ax = self.ax)

        # Agregamos un canvas para poder imprimir y generar el gráfico
        canvas = FigureCanvasTkAgg(self.figure, self.frameContenedor)
        canvas.get_tk_widget().grid(row=0, column=0)

        #Creamos un frame para mostrar información de la red
        self.frameRedInformacion = FrameUI(window, 0)
        self.frameRedInformacion.setLocation(1100, 100)
        self.frameRedInformacion.config(width=350, height=500, highlightbackground='white', highlightthickness=2)
        #Mostramos la información correspondiente
        self.textEntrenamiento = Text("Entrenamiento")
        self.textEntrenamiento.createUI(self.frameRedInformacion, ("Arial Bold", 13))
        self.textEntrenamiento.setLocation(20, 10)
        #Epocas
        self.textCantidadEpocas = Text("Cantidad de épocas:")
        self.textCantidadEpocas.createUI(self.frameRedInformacion, ("Arial Bold", 10))
        self.textCantidadEpocas.setLocation(30, 50)
        self.textValorEpocas = Text(str(len(epoca)))
        self.textValorEpocas.createUI(self.frameRedInformacion, ("Arial Bold", 10))
        self.textValorEpocas.setLocation(170, 50)
        #Exactitud entrenamiento
        self.textExactitudEntrenamiento = Text("Exactidud de entrenamiento:")
        self.textExactitudEntrenamiento.createUI(self.frameRedInformacion, ("Arial Bold", 10))
        self.textExactitudEntrenamiento.setLocation(30, 90)
        self.textValorEntrenamiento = Text(exactitud_entrenamiento)
        self.textValorEntrenamiento.createUI(self.frameRedInformacion, ("Arial Bold", 10))
        self.textValorEntrenamiento.setLocation(230, 90)
        self.textporcExactEntrenam = Text("%")
        self.textporcExactEntrenam.createUI(self.frameRedInformacion, ("Arial Bold", 10))
        self.textporcExactEntrenam.setLocation(265, 90)

        #Exactitud de validacion
        self.textExactitudValidacion = Text("Exactitud de validación:")
        self.textExactitudValidacion.createUI(self.frameRedInformacion, ("Arial Bold", 10))
        self.textExactitudValidacion.setLocation(30, 130)
        self.textValorValidacion = Text(exactitud_validacion)
        self.textValorValidacion.createUI(self.frameRedInformacion, ("Arial Bold", 10))
        self.textValorValidacion.setLocation(200, 130)
        self.textporcExactValid = Text("%")
        self.textporcExactValid.createUI(self.frameRedInformacion, ("Arial Bold", 10))
        self.textporcExactValid.setLocation(235, 130)


        self.botonClasificarPatrones = Button(self.window, text="Clasificar patrones", command=lambda: self.mostrarPantallaPatron() )
        self.botonClasificarPatrones.configure(width=20, bg=botonSeleccionPatronStyles["bg"])
        self.botonClasificarPatrones.place(x=900, y=650)
    
    
    
    def mostrarPantallaPatron(self):
        self.frameContenedor.destroy()
        self.frameRedInformacion.destroy()
        self.botonClasificarPatrones.destroy()
        pantallaPatron = SeleccionPatron(self.window, self.dataRed)
        
