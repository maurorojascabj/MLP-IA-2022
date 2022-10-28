from core.enums.Tipo_de_capa import Tipo_de_capa
from core.modelos.Capa import Capa


class Red():
    def __init__ (self, capas_ocultas, func_activacion_salida, func_activacion, coef_aprendizaje, term_momento):
        self._capas_ocultas =  capas_ocultas #topologia de las capas ocultas   
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
        self.inicializar_capa_de_entrada()
        self.inicializar_capas_ocultas()
        self.inicializar_capa_de_salida()

    def inicializar_capa_de_entrada(self):
        self.capas.append(Capa(self._cant_neuronas_entrada, self._func_activacion, 0, Tipo_de_capa.entrada))    

    def inicializar_capas_ocultas(self):
        #la primer capa se inicializa vinculando a la capa de entrada
        self.capas.append(Capa(self._capas_ocultas[0], self.func_activacion, Tipo_de_capa.oculta))   
        for capa_i in range(1, len(self._capas_ocultas)):
            self.capas.append(Capa(self._capas_ocultas[capa_i], self._capas_ocultas[capa_i - 1], self.func_activacion, Tipo_de_capa.oculta))

    def inicializar_capa_de_salida(self):
        self.capas.append(Capa(self._cant_neuronas_salida, self._capas_ocultas[len(self._capas_ocultas) - 1], self._func_activacion_salida, Tipo_de_capa.salida))    
      

    #>>>MECANISMOS DE ENTRENAMIENTO 
    #realiza una corrida (epoca) de entrenamiento con 1 dataset a especificar
    def entrenar_patron (self, vector_patron):
    #mandar el patron a capa de entrada
        self.capas[0].entrenar_partron(vector_patron)

    def entrenar_red (self,  dataset_entrenamiento, dataset_validacion ):  
        for renglon in range(dataset_entrenamiento):
           salida = self.entrenar_patron(renglon[0]) #con esta salida, calculo el error, y despues corrijo



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