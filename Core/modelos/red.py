from Core.enums.Tipo_de_capa import Tipo_de_capa
from Core.modelos.capa import Capa


class Red():
    def __init__ (self, capas_ocultas, func_activacion_salida, func_activacion, coef_aprendizaje, term_momento):
        self._capas_ocultas =  capas_ocultas #vector con largo =  cantidad de capas y con cantidades de neurona por capa
        self._coef_aprendizaje =  coef_aprendizaje
        self._term_momento  = term_momento
        self._func_activacion_salida = func_activacion_salida # funcion de activación para la capa de entrada
        self._func_activacion =  func_activacion #funcion de activacion de clase "interfaz_funcion" para capas ocultas y de salida       

        self._cant_neuronas_entrada = 100
        self._cant_neuronas_salida =  3

        self.vector_de_activacion = []
        self.matriz_de_pesos = []
        self.capas = []
        self.inicializar_capas()

    
    #>>>TRATAMIENTO DE CAPAS 
    def inicializar_capas(self):

        capa_de_entrada =Capa(self._cant_neuronas_entrada, self._func_activacion, None, None, Tipo_de_capa.entrada)  
        self.capas.append(capa_de_entrada)         

        capa_ant  = capa_de_entrada
        for capa_i in range(len(self._capas_ocultas)): #solo trata capas ocultas
            nueva_capa  = Capa(self._capas_ocultas[capa_i],self._func_activacion, capa_ant, None, Tipo_de_capa.oculta)
            self.capas.append(nueva_capa)
            capa_ant.capa_siguiente = nueva_capa

            capa_ant =  nueva_capa

        capa_de_salida = Capa(self._cant_neuronas_salida, self._func_activacion_salida, capa_ant, None, Tipo_de_capa.salida)   
        self.capas.append(capa_de_salida)
 
      

    #>>>MECANISMOS DE ENTRENAMIENTO 
    #realiza una corrida (epoca) de entrenamiento con 1 dataset a especificar
    def entrenar_patron (self, vector_patron):
    #mandar el patron a capa de entrada
        self.capas[0].entrenar_partron(vector_patron)

    def entrenar_red (self,  dataset_entrenamiento, dataset_validacion ):  
        for renglon in range(dataset_entrenamiento):
            vector_entrada=list(renglon[0])  #se convierte el string que forma el patron ingresado en un vector
            salida = self.entrenar_patron([int(x) for x in vector_entrada]) #con esta salida, calculo el error, y despues corrijo
            #[int(x) for x in vector_entrada] convierte cada caracter (0 o 1) del vector en un entero



    #>>>MECANISMOS DE CLASIFICACION   
    #recive un patron y devuelve la clasificacion calculada por la red    
    def clasificar_patron():
        pass

    def clasificar_patron_devolver_error():
        pass

    #>>>MECANISMOS DE ACTUALIZACION DE VARIABLES
    def actualizar_vector_de_activacion():
        pass

    def calcular_error_global():
        pass