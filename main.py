#matriz de pesos W
#se inicializa con valores aleatorioss

from Core.funciones.lineal import lineal
from Core.funciones.sigmoidal import sigmoidal
from Core.modelos.red import Red
from tratamiento_datasets.dividir_dataset import dividir_dataset

import numpy as np


funcion_sigmoidal = sigmoidal()

red  = Red([2,3,4],funcion_sigmoidal, funcion_sigmoidal,0.5,0.5)

#red.entrenar_red(dataset)

print('terminar')









porcentaje_testing = 0.2

porcentaje_validacion_1 = 0.1
porcentaje_validacion_2 = 0.2
porcentaje_validacion_3 = 0.3

funcion_sigmoidal  = sigmoidal()
funcion_lineal = lineal()

archivo="dataset1000.txt"
tamanio_archivo= 1000

dataset_entrenamiento, dataset_testing, dataset_validacion=dividir_dataset(archivo, tamanio_archivo, porcentaje_testing, porcentaje_validacion_1)

print(len(dataset_validacion))
print(dataset_entrenamiento[0][2])
print(len(dataset_testing))

red.entrenar_red(dataset_entrenamiento,dataset_validacion)

#print(dataset_validacion[5][0][15])
#print(list(dataset_entrenamiento[5][0]))
vector_entrada=list(dataset_entrenamiento[5][0])
print([int(x) for x in vector_entrada]) 

#tratar archivo: separar en 3 datasets
#llenar las 3 listas con los correspondientes patrones

#red = Red(,funcion_sigmoidal,funcion_lineal,,)

# prueba con porcentaje_validacion_1
#red.entrenar_red(dataset_entrenamiento_1, dataset_validacion_1)

# prueba con porcentaje_validacion_2
#red.entrenar_red(dataset_entrenamiento_1, dataset_validacion_1)

# prueba con porcentaje_validacion_3
