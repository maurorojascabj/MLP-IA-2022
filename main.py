#matriz de pesos W
#se inicializa con valores aleatorioss

from Core.funciones.lineal import lineal
from Core.funciones.sigmoidal import sigmoidal
from Core.modelos.red import Red
from tratamiento_datasets.dividir_dataset import dividir_dataset
from tratamiento_datasets.matrices_pesos_por_capa import obtener_pesos

import numpy as np


funcion_sigmoidal = sigmoidal()

#red  = Red([2,3,4],funcion_sigmoidal, funcion_sigmoidal,0.5,0.5,obtener_pesos("archivos_w\caso1.txt"))

red  = Red([5,8],funcion_sigmoidal, funcion_sigmoidal,0.7,0.7)


print('terminar')









porcentaje_testing = 0.2

porcentaje_validacion_1 = 0.1
porcentaje_validacion_2 = 0.2
porcentaje_validacion_3 = 0.3

funcion_sigmoidal  = sigmoidal()
funcion_lineal = lineal()

archivo="dataset1000.txt"
tamanio_archivo= 1000

dataset_entrenamiento, dataset_testing, dataset_validacion=dividir_dataset(archivo, tamanio_archivo, porcentaje_testing, porcentaje_validacion_3)





#obtener_pesos("archivos_w\caso1.txt")
                


for i in range(45):
    red.entrenar_red(dataset_entrenamiento,dataset_validacion)  
    print(red.error_global)


#red.clasificar(patron)
#print(dataset_validacion[5][0][15])
#print(list(dataset_entrenamiento[5][0]))


#tratar archivo: separar en 3 datasets
#llenar las 3 listas con los correspondientes patrones

#red = Red(,funcion_sigmoidal,funcion_lineal,,)

# prueba con porcentaje_validacion_1
#red.entrenar_red(dataset_entrenamiento_1, dataset_validacion_1)

# prueba con porcentaje_validacion_2
#red.entrenar_red(dataset_entrenamiento_1, dataset_validacion_1)

# prueba con porcentaje_validacion_3
