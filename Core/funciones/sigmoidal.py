

import math
from Core.funciones.derivada_1_sigmoidal import derivada_1_sigmoidal
import numpy as np

from Core.funciones.interfaz_funcion import interfaz_funcion
from decimal import *

class sigmoidal(interfaz_funcion): 
    def calcular(self,x):
        #print(x)
        #return 1 / (1+(Decimal(math.e)**(-x))) 
        if x >= 0:
            z = math.exp(-x)
            print(Decimal(1 / (1 + z)))
            return Decimal(np.round(1 / (1 + z),6))
        else:
            z = math.exp(x)
            print(Decimal(z / (1 + z) ))
            return Decimal(np.round(z / (1 + z) ,6))

    def calcular_derivada(self, x):
        resultado = derivada_1_sigmoidal.calcular(x)
        return resultado