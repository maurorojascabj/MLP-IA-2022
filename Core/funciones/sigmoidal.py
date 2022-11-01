

import math
from Core.funciones.derivada_1_sigmoidal import derivada_1_sigmoidal

from Core.funciones.interfaz_funcion import interfaz_funcion

class sigmoidal(interfaz_funcion): 
    def calcular(self,x):
        return 1 / (1+(math.e**(-x)))  

    def calcular_derivada(self, x):
        resultado = derivada_1_sigmoidal.calcular(x)
        return resultado