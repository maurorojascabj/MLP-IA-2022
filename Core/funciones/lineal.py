
from Core.funciones.derivada_1_lineal import derivada_1_lineal
from Core.funciones.interfaz_funcion import interfaz_funcion

class lineal(interfaz_funcion):
    def calcular(self, x):
        return x

    def calcular_derivada(self, x):
        resultado= derivada_1_lineal.calcular(x)
        return resultado