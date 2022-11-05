
import math

from Core.funciones.interfaz_funcion import interfaz_funcion
from decimal import *

getcontext().prec = 10

class derivada_1_sigmoidal(interfaz_funcion): 
    def calcular(x):
        return x * ( x - 1 )  #se espera recibir en x el resultado de haber aplicado una función sigmoidal