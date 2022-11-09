import tkinter as tkinter
from tkinter import Radiobutton, Button
from Styles import *
from UI.FrameUI import *
from UI.Pattern import *
from UI.SelectMultiple import *
from UI.Text import *
from utils import *

class Entrenamiento():
    def __init__(self, window):
        super().__init__()
        self.window = window
        
        self.textMenu = Text("Seleccione la configuración de la red")
        self.textMenu.createUI(self.window, ("Arial Bold", 14))
        self.textMenu.setLocation(textMenuStyles["coordenadaX"], textMenuStyles["coordenadaY"])
        self.textDistorsion = Text("Porcentaje de distorsión:")
        self.textDistorsion.createUI(self.window, ("Arial Bold", 12))
        self.textDistorsion.setLocation(titleDistorsionStyles["coordenadaX"], titleDistorsionStyles["coordenadaY"])
        self.comboBox = SelectMultiple(self.window)
        self.comboBox.setValues()
        self.comboBox.setLocation(comboboxDistorsionStyles["coordenadaX"], comboboxDistorsionStyles["coordenadaY"])

        self.textPatron = Text("Número de capas:")
        self.textPatron.createUI(self.window, ("Arial Bold", 12))
        self.textPatron.setLocation(titleCapasStyles["coordenadaX"], titleCapasStyles["coordenadaY"])

        valueCapas = tkinter.IntVar()
        self.radCapaUno = Radiobutton(self.window, text='1 (un) capa', value="1", variable=valueCapas)
        self.radCapaUno.place(x=radCapaUnoStyles["coordenadaX"], y=radCapaUnoStyles["coordenadaY"])
        self.radCapaDos = Radiobutton(self.window, text='2 (dos) capas', value="2", variable=valueCapas)
        self.radCapaDos.place(x=radCapaDosStyles["coordenadaX"], y=radCapaDosStyles["coordenadaY"])

        self.textComboboxNeuronas = Text("Número de neuronas:")
        self.textComboboxNeuronas.createUI(self.window, ("Arial Bold", 12))
        self.textComboboxNeuronas.setLocation(titleComboboxNeuronasStyles["coordenadaX"], titleComboboxNeuronasStyles["coordenadaY"])
        self.comboboxNeuronas = SelectMultiple(self.window)
        self.comboboxNeuronas.setValues(5,10, "neuronas")
        self.comboboxNeuronas.setLocation(comboboxNeuronasStyles["coordenadaX"], comboboxNeuronasStyles["coordenadaY"])
        
        self.textFuncionActivacion = Text("Tipo de función de activación:")
        self.textFuncionActivacion.createUI(self.window, ("Arial Bold", 12))
        self.textFuncionActivacion.setLocation(textFuncionActivacionStyles["coordenadaX"], textFuncionActivacionStyles["coordenadaY"])

        valueFuncionActivacion = tkinter.IntVar()
        self.radFunctionActivacionLineal = Radiobutton(self.window, text='Lineal', value="1", variable=valueFuncionActivacion)
        self.radFunctionActivacionLineal.place(x=radFunctionActivacionLinealStyles["coordenadaX"], y=radFunctionActivacionLinealStyles["coordenadaY"])
        self.radFunctionActivacionSigmoidal = Radiobutton(self.window, text='Sigmoidal', value="2", variable=valueFuncionActivacion)
        self.radFunctionActivacionSigmoidal.place(x=radFunctionActivacionSigmoidalStyles["coordenadaX"], y=radFunctionActivacionSigmoidalStyles["coordenadaY"])

        self.textCoeficienteAprendizaje = Text("Coeficiente de aprendizaje:")
        self.textCoeficienteAprendizaje.createUI(self.window, ("Arial Bold", 12))
        self.textCoeficienteAprendizaje.setLocation(textCoeficienteAprendizajeStyles["coordenadaX"], textCoeficienteAprendizajeStyles["coordenadaY"])

        valueCoeficienteAprendizaje = tkinter.IntVar()
        self.radCoeficienteAprendizajeCero = Radiobutton(self.window, text='0 (cero)', value="0", variable=valueCoeficienteAprendizaje)
        self.radCoeficienteAprendizajeCero.place(x=radCoeficienteAprendizajeCeroStyles["coordenadaX"], y=radCoeficienteAprendizajeCeroStyles["coordenadaY"])
        self.radCoeficienteAprendizajeUno = Radiobutton(self.window, text='1 (uno)', value="1", variable=valueCoeficienteAprendizaje)
        self.radCoeficienteAprendizajeUno.place(x=radCoeficienteAprendizajeUnoStyles["coordenadaX"], y=radCoeficienteAprendizajeUnoStyles["coordenadaY"])

        self.textTerminoMomento = Text("Término de momento:")
        self.textTerminoMomento.createUI(self.window, ("Arial Bold", 12))
        self.textTerminoMomento.setLocation(textTerminoMomentoStyles["coordenadaX"], textTerminoMomentoStyles["coordenadaY"])

        valueTerminoMomento = tkinter.IntVar()
        self.radTerminoMomentoUno = Radiobutton(self.window, text='1 (un) capa', value="1", variable=valueTerminoMomento)
        self.radTerminoMomentoUno.place(x=radTerminoMomentoUnoStyles["coordenadaX"], y=radTerminoMomentoUnoStyles["coordenadaY"])
        self.radTerminoMomentoDos = Radiobutton(self.window, text='2 (dos) capas', value="2", variable=valueTerminoMomento)
        self.radTerminoMomentoDos.place(x=radTerminoMomentoDosStyles["coordenadaX"], y=radTerminoMomentoDosStyles["coordenadaY"])

        self.botonGenerarRed = Button(self.window, text="Crear red") #generateDistorsion(comboBox.getValues(), matriz)
        self.botonGenerarRed.configure(width=botonGenerarRedStyles["width"], bg=botonGenerarRedStyles["bg"])
        self.botonGenerarRed.place(x=botonGenerarRedStyles["coordenadaX"], y=botonGenerarRedStyles["coordenadaY"])

    def setDistorsion(matriz, repetitions):
        newMatriz = matriz.copy()
        for x in range(repetitions):
            position = generateRandom(0,99)
            for y in range(len(newMatriz)):
                if y == position:
                    if newMatriz[y] == 0:
                        newMatriz[y] = 1
                    else:
                        newMatriz[y] = 0
        return newMatriz
                    
    def generateDistorsion(self, value, matriz):
        frame = FrameUI(self.window)
        frame.setLocation(frameDistorsionado["coordenadaX"], frameDistorsionado["coordenadaY"])
        pattern = Pattern()
        value = value[:-1] #Elimino el caracter %
        value = int(value)
        # print("value ", value)
        self.textPatronDistorsionado = Text("Patrón distorsionado")
        self.textPatronDistorsionado.createUI(self.window, ("Arial Bold", 15))
        self.textPatronDistorsionado.setLocation(titlePatronDistorsionadoStyles["coordenadaX"], titlePatronDistorsionadoStyles["coordenadaY"])
        newMatriz = []
        newMatriz = self.setDistorsion(matriz, value) #matriz B, valor 10
        # print("newMatriz ", newMatriz)
        pattern.drawPattern(frame, cellStyles["bgCell"], newMatriz)

    # def crearPantalla(self, matrizB = None, matrizC = None, matrizF = None ):
        # print(radioButtonSeleccionado)
        # if radioButtonSeleccionado == 1 or radioButtonSeleccionado == 2 or radioButtonSeleccionado == 3:
        #     matriz = []
        #     if radioButtonSeleccionado == 1:
        #         destroyElement(frameD)
        #         destroyElement(frameF)
        #         matriz = matrizB.copy()
        #         frameB.setLocation(frameSeleccionado["coordenadaX"], frameSeleccionado["coordenadaY"])
        #     elif radioButtonSeleccionado == 2:
        #         destroyElement(frameB)
        #         destroyElement(frameF)
        #         matriz = matrizC.copy()
        #         frameD.setLocation(frameSeleccionado["coordenadaX"], frameSeleccionado["coordenadaY"])
        #     elif radioButtonSeleccionado == 3:
        #         destroyElement(frameB)
        #         destroyElement(frameD)
        #         matriz = matrizF.copy()
        #         frameF.setLocation(frameSeleccionado["coordenadaX"], frameSeleccionado["coordenadaY"])

        #     self.textPatronOriginal = Text("Patrón original")
        #     self.textPatronOriginal.createUI(self.window, ("Arial Bold", 15))
        #     self.textPatronOriginal.setLocation(titlePatronSeleccionadoStyles["coordenadaX"], titlePatronSeleccionadoStyles["coordenadaY"])
            
        #     buttonMain.destroy()
        #     rad1.destroy()
        #     rad2.destroy()
        #     rad3.destroy()
