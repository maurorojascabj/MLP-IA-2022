

import math
from Core.funciones.interfaz_funcion import interfaz_funcion

class sigmoidal(interfaz_funcion): 
    def calcular(self,net):
        return 1 / (1+(math.e**(-net)))  