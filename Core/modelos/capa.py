from core.enums.Tipo_de_capa import Tipo_de_capa
from core.modelos.Neurona import Neurona

class Capa():
    def __init__ (self , cant_neuronas,  func_activacion, capa_anterior, capa_siguiente, tipo):
        self._func_activacion = func_activacion
        self._cant_neuronas = cant_neuronas
        self._capa_anterior = capa_anterior
        self._capa_siguiente = capa_siguiente

        self.tipo = tipo
        self.vector_de_activacion = []
        
        self.neuronas = []
        for i in range(cant_neuronas):
            nueva_neurona = Neurona(func_activacion)
            self.neuronas.append(nueva_neurona)
            #for each neurona de la capa anterior voy acumulando Net
            #despues asigno la acumulacion a nueva_neurona.net


    def entrenar_partron (self, vector_entradas): #estamos trabajando con 1 renglon
        salida_de_la_capa = [] 
        for neurona in self.neuronas:
            salida_de_la_capa.append(neurona.calcular_salida(self, vector_entradas))

        # una vez que tengo todas las salidas de la capa
        if self.tipo  != Tipo_de_capa.salida:
            self._capa_siguiente.entrenar_patron(salida_de_la_capa)   
        else:
            return salida_de_la_capa # es la salida de la capa de salida


