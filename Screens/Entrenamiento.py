import tkinter as tkinter
from tkinter import Radiobutton, Button
from Styles import *
from UI.FrameUI import *
from UI.Dialog import *
from UI.Pattern import *
from UI.SelectMultiple import *
from UI.Text import *
from Screens.SeleccionPatron import *
from utils import *
from integracion_utilidades import *
from Core.modelos.red import Red


class Entrenamiento():
    def __init__(self, window):
        super().__init__()
        self.red = None
        self.window = window

        self.frameContenedor = FrameUI(window, 0)
        self.frameContenedor.setLocation(250, 120)
        self.frameContenedor.config(width=1000, height=600)
        
        self.textMenu = Text("Seleccione la configuración de la red")
        self.textMenu.createUI(self.frameContenedor, ("Arial Bold", 14))
        self.textMenu.setLocation(textMenuEntrenamientoStyles["coordenadaX"], textMenuEntrenamientoStyles["coordenadaY"])

        self.textPatron = Text("Número de capas:")
        self.textPatron.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textPatron.setLocation(titleCapasStyles["coordenadaX"], titleCapasStyles["coordenadaY"])

        self.valueCapas = tkinter.IntVar()
        self.radCapaUno = Radiobutton(self.frameContenedor, text='1 (un) capa', value=1, variable=self.valueCapas, command=lambda: self.quitarNeurona())
        self.radCapaUno.place(x=radCapaUnoStyles["coordenadaX"], y=radCapaUnoStyles["coordenadaY"])
        self.radCapaDos = Radiobutton(self.frameContenedor, text='2 (dos) capas', value=2, variable=self.valueCapas, command=lambda: self.agregarNeurona())
        self.radCapaDos.place(x=radCapaDosStyles["coordenadaX"], y=radCapaDosStyles["coordenadaY"])

        self.textComboboxNeuronas = Text("Número de neuronas - Capa 1:")
        self.textComboboxNeuronas.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textComboboxNeuronas.setLocation(titleComboboxNeuronasStyles["coordenadaX"], titleComboboxNeuronasStyles["coordenadaY"])
        self.comboboxNeuronas = SelectMultiple(self.frameContenedor)
        self.comboboxNeuronas.setValues(5,10, "neuronas")
        self.comboboxNeuronas.setLocation(comboboxNeuronasStyles["coordenadaX"], comboboxNeuronasStyles["coordenadaY"])

        ##Casos con dos capas
        self.textComboboxNeuronasDosCapas = Text("Número de neuronas - Capa 2:")
        self.textComboboxNeuronasDosCapas.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textComboboxNeuronasDosCapas.setLocation(textComboboxNeuronasDosCapasStyles["coordenadaX"], textComboboxNeuronasDosCapasStyles["coordenadaY"])

        self.comboboxNeuronasDosCapas = SelectMultiple(self.frameContenedor, "disabled")
        self.comboboxNeuronasDosCapas.setValues(5,10, "neuronas")
        self.comboboxNeuronasDosCapas.setLocation(comboboxNeuronasDosCapasStyles["coordenadaX"], comboboxNeuronasDosCapasStyles["coordenadaY"])
        self.valoresCantidadNeuronasPorCapa = []

        ##Fin

        self.textFuncionActivacion = Text("Tipo de función de activación:")
        self.textFuncionActivacion.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textFuncionActivacion.setLocation(textFuncionActivacionStyles["coordenadaX"], textFuncionActivacionStyles["coordenadaY"])

        self.valueFuncionActivacion = tkinter.IntVar()
        self.radFunctionActivacionLineal = Radiobutton(self.frameContenedor, text='Lineal', value=1, variable=self.valueFuncionActivacion)
        self.radFunctionActivacionLineal.place(x=radFunctionActivacionLinealStyles["coordenadaX"], y=radFunctionActivacionLinealStyles["coordenadaY"])
        self.radFunctionActivacionSigmoidal = Radiobutton(self.frameContenedor, text='Sigmoidal', value=2, variable=self.valueFuncionActivacion)
        self.radFunctionActivacionSigmoidal.place(x=radFunctionActivacionSigmoidalStyles["coordenadaX"], y=radFunctionActivacionSigmoidalStyles["coordenadaY"])

        self.textCoeficienteAprendizaje = Text("Coeficiente de aprendizaje:")
        self.textCoeficienteAprendizaje.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textCoeficienteAprendizaje.setLocation(textCoeficienteAprendizajeStyles["coordenadaX"], textCoeficienteAprendizajeStyles["coordenadaY"])

        valueCoeficienteAprendizaje = tkinter.IntVar()
        self.radCoeficienteAprendizajeCero = Radiobutton(self.frameContenedor, text='0 (cero)', value=1, variable=valueCoeficienteAprendizaje)
        self.radCoeficienteAprendizajeCero.place(x=radCoeficienteAprendizajeCeroStyles["coordenadaX"], y=radCoeficienteAprendizajeCeroStyles["coordenadaY"])
        self.radCoeficienteAprendizajeUno = Radiobutton(self.frameContenedor, text='1 (uno)', value=2, variable=valueCoeficienteAprendizaje)
        self.radCoeficienteAprendizajeUno.place(x=radCoeficienteAprendizajeUnoStyles["coordenadaX"], y=radCoeficienteAprendizajeUnoStyles["coordenadaY"])

        self.textTerminoMomento = Text("Término de momento:")
        self.textTerminoMomento.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textTerminoMomento.setLocation(textTerminoMomentoStyles["coordenadaX"], textTerminoMomentoStyles["coordenadaY"])

        valueTerminoMomento = tkinter.IntVar()
        self.radTerminoMomentoUno = Radiobutton(self.frameContenedor, text='0 (cero)', value=1, variable=valueTerminoMomento)
        self.radTerminoMomentoUno.place(x=radTerminoMomentoUnoStyles["coordenadaX"], y=radTerminoMomentoUnoStyles["coordenadaY"])
        self.radTerminoMomentoDos = Radiobutton(self.frameContenedor, text='1 (uno)', value=2, variable=valueTerminoMomento)
        self.radTerminoMomentoDos.place(x=radTerminoMomentoDosStyles["coordenadaX"], y=radTerminoMomentoDosStyles["coordenadaY"])

        self.botonGenerarRedEntrenamiento = Button(
            self.frameContenedor, text="Crear red",
            command=lambda: self.setDatos(
                self.radioDataset.get(),
                self.radioDatasetValidacion.get(),
                self.valueCapas.get(),
                self.valoresCantidadNeuronasPorCapa,
                self.valueFuncionActivacion.get(),
                valueCoeficienteAprendizaje.get(),
                valueTerminoMomento.get()
            )
        )
        self.botonGenerarRedEntrenamiento.configure(width=botonGenerarRedEntrenamientoStyles["width"], bg=botonGenerarRedEntrenamientoStyles["bg"])
        self.botonGenerarRedEntrenamiento.place(x=botonGenerarRedEntrenamientoStyles["coordenadaX"], y=botonGenerarRedEntrenamientoStyles["coordenadaY"])

        ##
        self.radioDataset = tkinter.IntVar()
        self.radioDatasetValidacion = tkinter.IntVar()
        def crearSeleccionDataset():
            self.text = Text("Tamaño del dataset:")
            self.text.createUI(self.frameContenedor, ("Arial Bold", 12))
            self.text.setLocation(200, 80)
            valoresDataset = [100, 500, 1000]
            posicionX = 490
            for item in valoresDataset:
                self.radioButton = Radiobutton(self.frameContenedor, text=str(item), value=item, variable=self.radioDataset)
                self.radioButton.place(x=posicionX, y=80)
                posicionX += 130
        crearSeleccionDataset()

        def crearSeleccionDatasetValidacion():
            self.text = Text("Porcentaje dataset de validación:")
            self.text.createUI(self.frameContenedor, ("Arial Bold", 12))
            self.text.setLocation(200, 130)
            valoresDatasetValidacion = [10, 20, 30]
            posicionX = 490
            for item in valoresDatasetValidacion:
                self.radioButton = Radiobutton(self.frameContenedor, text=str(item) + "%", value=item, variable=self.radioDatasetValidacion)
                self.radioButton.place(x=posicionX, y=130)
                posicionX += 130
        crearSeleccionDatasetValidacion()

        ## Creamos la estructura a devolver
        self.diccionarioDatos = {
            "tam_dataset": "",
            "capas_config": [],
            "func_de_transferencia": "",
            "coef_aprendizaje": "",
            "term_momento": "",
            "porc_validacion": ""
        }

    def quitarNeurona(self):
        self.comboboxNeuronasDosCapas.setDisabled()
        self.valoresCantidadNeuronasPorCapa = [int(self.comboboxNeuronas.getValues())]

    def agregarNeurona(self):
        self.comboboxNeuronasDosCapas.setNormal()
        self.valoresCantidadNeuronasPorCapa = [int(self.comboboxNeuronas.getValues()), int(self.comboboxNeuronasDosCapas.getValues())]

    def redirectPantalla(self, datos):
        self.frameContenedor.destroy()
        self.red = entrenar_y_obtener_red(datos) # self.red.clasificar_patron_maxarg(patron_distorsionado)
        pantallaPatron = SeleccionPatron(self.window, self.red)


    ##Seteamos el diccionario de datos
    def setDatos(self, tamañoDataset, porcentajeDatasetValidacion, valorNumeroCapas, arrayNeuronas, valorFuncActivacion, valorCoeficAprend, valorTermMomento):
        if(
            tamañoDataset != 0 and
            porcentajeDatasetValidacion != 0 and
            valorNumeroCapas != 0 and
            arrayNeuronas != [] and
            valorFuncActivacion != 0 and
            valorCoeficAprend != 0 and
            valorTermMomento != 0
        ):
            print(tamañoDataset, porcentajeDatasetValidacion, valorNumeroCapas, arrayNeuronas, valorFuncActivacion, valorCoeficAprend, valorTermMomento)
            valorNumeroCapas -= 1
            valorFuncActivacion -= 1
            valorCoeficAprend -= 1
            valorTermMomento -= 1
            self.diccionarioDatos["tam_dataset"] = tamañoDataset
            self.diccionarioDatos["capas_config"] = arrayNeuronas
            self.diccionarioDatos["func_de_transferencia"] = valorFuncActivacion
            self.diccionarioDatos["coef_aprendizaje"] = valorCoeficAprend
            self.diccionarioDatos["term_momento"] = valorTermMomento
            self.diccionarioDatos["porc_validacion"] = porcentajeDatasetValidacion
            self.redirectPantalla(self.diccionarioDatos)
        else:
            self.modalWarning = Dialog("warning", "¡Cuidado!", "Debe seleccionar una opción para cada caso")

        
