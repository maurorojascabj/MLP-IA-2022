from Core.modelos.capa import capa


class red():
    def __init__ (self, cant_capas, cant_neuronas, func_activacion_entrada, func_activacion, coef_aprendizaje, term_momento, dataset):
        self._cant_capas = cant_capas
        self._cant_neuronas =  cant_neuronas
        self._func_activacion =  func_activacion
        self._coef_aprendizaje =  coef_aprendizaje
        self._term_momento  = term_momento
        self._func_activacion_entrada = func_activacion_entrada

        self.capas = []
        #tratar capa de entrada

        #tratar capa de salida
        for i in range(1, cant_capas - 1):
            self.capas.append(capa((cant_neuronas/cant_capas), (cant_neuronas/cant_capas), func_activacion))
