

class capa():
    def __init__ (self , cant_neuronas, capa_anterior, func_activacion, tipo):
        self._func_activacion = func_activacion
        self._cant_neuronas = cant_neuronas
        self._capa_anterior = capa_anterior
        self._tipo = tipo
        
        self.neuronas = []
        for i in range(cant_neuronas):
            self.neuronas.append(nueva_neurona)
            #for each neurona de la capa anterior voy acumulando Net
            #despues asigno la acumulacion a nueva_neurona.net
