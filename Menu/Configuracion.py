from tkinter import Menu, IntVar

class Configuracion(Menu):
    def __init__(self, menubar):
        super().__init__()
        self.configuracion = Menu(menubar, tearoff=False)
        menubar.add_cascade(menu=self.configuracion, label="Confguración red")

        #Agrego submenu al menu principal
            #submenu distorsion
        opcionDistorsion = IntVar()
        self.distorsion = Menu(self.configuracion, tearoff=False)
        for x in range(1, 31): #Opciones menu distorsion
            self.distorsion.add_radiobutton(label=str(x)+"%", variable=opcionDistorsion, value=x)
        # self.distorsion.add_radiobutton(label="Opción 1", variable=opcionDistorsion, value=1)
        # self.distorsion.add_radiobutton(label="Opción 2", variable=opcionDistorsion, value=2)
            #submenu n° capa
        opcionCapa = IntVar()
        self.capas = Menu(self.configuracion, tearoff=False)
        self.capas.add_radiobutton(label="Opción 1", variable=opcionCapa, value=1)
        self.capas.add_radiobutton(label="Opción 2", variable=opcionCapa, value=2, command=self.habilitarNeuronasCapa2)
        
        self.neuronas = Menu(self.configuracion, tearoff=False)
            #submenu funcion activacion
        opcionFuncionActivacion = IntVar()
        self.funcionActivacion = Menu(self.configuracion, tearoff=False)
        self.funcionActivacion.add_radiobutton(label="Opción 1", variable=opcionFuncionActivacion, value=1)
        self.funcionActivacion.add_radiobutton(label="Opción 2", variable=opcionFuncionActivacion, value=2)
            #submenu coeficiente aprendizaje
        opcionCoeficienteAprendizaje = IntVar()
        self.coeficienteAprendizaje = Menu(self.configuracion, tearoff=False)
        self.coeficienteAprendizaje.add_radiobutton(label="Opción 1", variable=opcionCoeficienteAprendizaje, value=1)
        self.coeficienteAprendizaje.add_radiobutton(label="Opción 2", variable=opcionCoeficienteAprendizaje, value=2)
            #submenu termino momento
        opcionTerminoMomento = IntVar()
        self.terminoMomento = Menu(self.configuracion, tearoff=False)
        self.terminoMomento.add_radiobutton(label="Opción 1", variable=opcionTerminoMomento, value=1)
        self.terminoMomento.add_radiobutton(label="Opción 2", variable=opcionTerminoMomento, value=2)
        
        #Agrego cada submenu al menu principal
        self.configuracion.add_cascade(menu=self.distorsion, label="Distorsión")
        self.configuracion.add_cascade(menu=self.capas, label="Número capas")
        # self.configuracion.add_cascade(menu=self.capas, label="Número capas")
        self.configuracion.add_cascade(menu=self.neuronas, label="Número neuronas")
        self.configuracion.add_cascade(menu=self.funcionActivacion, label="Función de activación")
        self.configuracion.add_cascade(menu=self.coeficienteAprendizaje, label="Coeficiente de aprendizaje")
        self.configuracion.add_cascade(menu=self.terminoMomento, label="Término de momento")
        

        self.neuronaCapa1 = Menu(self.neuronas, tearoff=False)
        self.neuronaCapa2 = Menu(self.neuronas, tearoff=False)
        # self.neuronas.entryconfig(state="disabled")
        self.neuronas.add_cascade(menu=self.neuronaCapa1, label="Cantidad de neuronas - Capa 1")
        self.neuronas.add_cascade(menu=self.neuronaCapa2, label="Cantidad de neuronas - Capa 2")
        self.neuronas.entryconfig("Cantidad de neuronas - Capa 2", state="disabled")

        # self.capas.add_command(label="Dos capas", command=self.habilitarNeuronasCapa2)

        # self.neuronas.add_cascade(label="Capa 1")
        # if (self.cantidadCapa = 2):
        opcionNeuronaCapa1 = IntVar()
        opcionNeuronaCapa2 = IntVar()
        for x in range(5, 11): #Opciones menu distorsion
            self.neuronaCapa1.add_radiobutton(label=str(x), variable=opcionNeuronaCapa1, value=x)
            self.neuronaCapa2.add_radiobutton(label=str(x), variable=opcionNeuronaCapa2, value=x)
    
    def habilitarNeuronasCapa2(self):
        self.neuronas.entryconfig("Cantidad de neuronas - Capa 2", state="normal")
        
        






