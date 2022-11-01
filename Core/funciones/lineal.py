
from Core.funciones import derivada_1_lineal
from Core.funciones.interfaz_funcion import interfaz_funcion

class lineal(interfaz_funcion):
    def calcular(self, x):
        return x

    def calcular_derivada(self, x):
        return derivada_1_lineal.calcular(x)    