

import math
from Core.funciones.derivada_1_sigmoidal import derivada_1_sigmoidal
import numpy as np


from Core.funciones.interfaz_funcion import interfaz_funcion
from decimal import *

class sigmoidal(interfaz_funcion): 
    def calcular(self,x):
        return 1 / (1+(Decimal(math.e)**(-x)))  

    def calcular_derivada(self, x):
        resultado = derivada_1_sigmoidal.calcular(x)
        return resultado