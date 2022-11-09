from tkinter import Button, Radiobutton
from UI.FrameUI import *
from UI.Text import *
from Styles import *
from Screens.SeleccionPatron import *

class Red(Button):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.frameContenedor = FrameUI(window, 0)
        self.frameContenedor.setLocation(250, 120)
        self.frameContenedor.config(width=1000, height=600)

        buttonMainRed = Button(self.frameContenedor, text="Guardar elección", command=lambda: self.setDatos(self.radioDataset.get(), self.radioDatasetValidacion.get(), self.radioValue.get()))
        buttonMainRed.configure(width=buttonMainRedStyles["width"], bg=buttonMainRedStyles["bg"])
        buttonMainRed.place(x=100, y=560)

        opcionCapa1 = [
            ["1 Capa", "5 neuronas", "Función de transferencia lineal", "Coeficiente de aprendizaje 0,5", "Término momento 0,5"],
            ["1 Capa", "10 neuronas", "Función de transferencia lineal", "Coeficiente de aprendizaje 0,5", "Término momento 0,5"],
            ["2 Capa", "Cada capa oculta de 5 neuronas", "Función de transferencia lineal", "Coeficiente de aprendizaje 0,5", "Término momento 0,5"],
            ["2 Capa", "Cada capa oculta de 10 neuronas", "Función de transferencia lineal", "Coeficiente de aprendizaje 0,5", "Término momento 0,5"],       
        ]
        opcionCapa2 = [
            ["1 Capa", "5 neuronas", "Función de transferencia lineal", "Coeficiente de aprendizaje 0,5", "Término momento 0,9"],
            ["1 Capa", "10 neuronas", "Función de transferencia lineal", "Coeficiente de aprendizaje 0,5", "Término momento 0,9"],
            ["2 Capa", "Cada capa oculta de 5 neuronas", "Función de transferencia lineal", "Coeficiente de aprendizaje 0,5", "Término momento 0,9"],
            ["2 Capa", "Cada capa oculta de 10 neuronas", "Función de transferencia lineal", "Coeficiente de aprendizaje 0,5", "Término momento 0,9"]
        ]

        ## Creamos el menu
        self.radioDataset = tkinter.IntVar()
        self.radioDatasetValidacion = tkinter.IntVar()
        self.radioValue = tkinter.IntVar()

        def crearSeleccionDataset():
            self.text = Text("Seleccione el tamaño del dataset:")
            self.text.createUI(self.frameContenedor)
            self.text.setLocation(0, 0)
            valoresDataset = [100, 500, 1000]
            idx = 1
            for item in valoresDataset:
                self.radioButton = Radiobutton(self.frameContenedor, text=str(item), value=item, variable=self.radioDataset)
                self.radioButton.place(x=200*idx, y=30)
                idx += 1
        crearSeleccionDataset()

        def crearSeleccionDatasetValidacion():
            self.text = Text("Seleccione el porcentaje para el dataset de validación:")
            self.text.createUI(self.frameContenedor)
            self.text.setLocation(0, 60)
            valoresDatasetValidacion = [10, 20, 30]
            idx = 1
            for item in valoresDatasetValidacion:
                self.radioButton = Radiobutton(self.frameContenedor, text=str(item) + "%", value=item, variable=self.radioDatasetValidacion)
                self.radioButton.place(x=200*idx, y=90)
                idx += 1
        crearSeleccionDatasetValidacion()

        def crearOpcionesPrueba():
            self.text = Text("Seleccione la configuración de la red adecuada:")
            self.text.createUI(self.frameContenedor)
            self.text.setLocation(0, 130)
            positionY = 180
            idx = 1
            for item in opcionCapa1:
                textoCompleto = str(idx) + ") " + item[0:1][0]
                elementos = item[1:5]
                for subitem in elementos:
                    textoCompleto = textoCompleto + " - " + subitem
                self.text = Text(textoCompleto)
                self.text.createUI(self.frameContenedor)
                self.text.setLocation(10, positionY)
                self.radioButton = Radiobutton(self.frameContenedor, text='', value=idx, variable=self.radioValue)
                self.radioButton.place(x=950, y=positionY)
                positionY += 50
                idx += 1
            for item in opcionCapa2:
                textoCompleto = str(idx) + ") " + item[0:1][0]
                elementos = item[1:5]
                for subitem in elementos:
                    textoCompleto = textoCompleto + " - " + subitem
                self.text = Text(textoCompleto)
                self.text.createUI(self.frameContenedor)
                self.text.setLocation(10, positionY)
                self.radioButton = Radiobutton(self.frameContenedor, text='', value=idx, variable=self.radioValue)
                self.radioButton.place(x=950, y=positionY)
                positionY += 50
                idx += 1
        crearOpcionesPrueba()

        ## Creamos la estructura a devolver
        self.diccionarioDatos = {
            "tam_dataset": "",
            "capas_config": [],
            "func_de_transferencia": "",
            "coef_aprendizaje": "",
            "term_momento": "",
            "porc_validacion": ""
        }
    
    def redirectPantalla(self, datos):
        self.frameContenedor.destroy()
        pantallaPatron = SeleccionPatron(self.window)

    ## setDatos()
    def setDatos(self, valorDataset, valorDatasetValidacion, valorCombinacionElegida):
        if (valorDataset != 0 and valorDatasetValidacion != 0 and valorCombinacionElegida != 0):
            self.diccionarioDatos["func_de_transferencia"] = 0
            self.diccionarioDatos["coef_aprendizaje"] = 0.5
            if (valorCombinacionElegida == 1):
                self.diccionarioDatos["tam_dataset"] = valorDataset
                self.diccionarioDatos["capas_config"] = [5]
                self.diccionarioDatos["term_momento"] = 0.5
                self.diccionarioDatos["porc_validacion"] = valorDatasetValidacion
            elif (valorCombinacionElegida == 2):
                self.diccionarioDatos["tam_dataset"] = valorDataset
                self.diccionarioDatos["capas_config"] = [10]
                self.diccionarioDatos["term_momento"] = 0.5
                self.diccionarioDatos["porc_validacion"] = valorDatasetValidacion
            elif (valorCombinacionElegida == 3):
                self.diccionarioDatos["tam_dataset"] = valorDataset
                self.diccionarioDatos["capas_config"] = [5,5]
                self.diccionarioDatos["term_momento"] = 0.5
                self.diccionarioDatos["porc_validacion"] = valorDatasetValidacion
            elif (valorCombinacionElegida == 4):
                self.diccionarioDatos["tam_dataset"] = valorDataset
                self.diccionarioDatos["capas_config"] = [10,10]
                self.diccionarioDatos["term_momento"] = 0.5
                self.diccionarioDatos["porc_validacion"] = valorDatasetValidacion
            elif (valorCombinacionElegida == 5):
                self.diccionarioDatos["tam_dataset"] = valorDataset
                self.diccionarioDatos["capas_config"] = [5]
                self.diccionarioDatos["term_momento"] = 0.9
                self.diccionarioDatos["porc_validacion"] = valorDatasetValidacion
            elif (valorCombinacionElegida == 6):
                self.diccionarioDatos["tam_dataset"] = valorDataset
                self.diccionarioDatos["capas_config"] = [10]
                self.diccionarioDatos["term_momento"] = 0.9
                self.diccionarioDatos["porc_validacion"] = valorDatasetValidacion
            elif (valorCombinacionElegida == 7):
                self.diccionarioDatos["tam_dataset"] = valorDataset
                self.diccionarioDatos["capas_config"] = [5,5]
                self.diccionarioDatos["term_momento"] = 0.9
                self.diccionarioDatos["porc_validacion"] = valorDatasetValidacion
            elif (valorCombinacionElegida == 8):
                self.diccionarioDatos["tam_dataset"] = valorDataset
                self.diccionarioDatos["capas_config"] = [10,10]
                self.diccionarioDatos["term_momento"] = 0.9
                self.diccionarioDatos["porc_validacion"] = valorDatasetValidacion
        
            self.redirectPantalla(self.diccionarioDatos)
