
import math

from Core.funciones.interfaz_funcion import interfaz_funcion
from decimal import *

class derivada_1_sigmoidal(interfaz_funcion): 
    def calcular(x):
        return (x * ( 1 - x ))  #se espera recibir en x el resultado de haber aplicado una función sigmoidal