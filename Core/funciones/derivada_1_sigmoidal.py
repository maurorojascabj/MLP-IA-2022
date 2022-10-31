
import math

from Core.funciones.interfaz_funcion import interfaz_funcion

class derivada_1_sigmoidal(interfaz_funcion): 
    def calcular(self, x):
        return x * ( x - 1 )  #se espera recibir en x el resultado de haber aplicado una función sigmoidal