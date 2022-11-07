#matriz de pesos W
#se inicializa con valores aleatorioss

import random
from Core.funciones.lineal import lineal
from Core.funciones.sigmoidal import sigmoidal
from Core.modelos.red import Red
from tratamiento_datasets.dividir_dataset import dividir_dataset


funcion_sigmoidal = sigmoidal()
funcion_lineal = lineal()

capas_ocultas=[5]
funcion_salida=funcion_sigmoidal
funcion_capa_oculta=funcion_lineal
coef_aprendizaje=0.5
term_momento=0.5


red  = Red(capas_ocultas, funcion_salida, funcion_capa_oculta, coef_aprendizaje, term_momento)

porcentaje_testing = 0.2
porcentaje_validacion_1 = 0.1
porcentaje_validacion_2 = 0.2
porcentaje_validacion_3 = 0.3

archivo="dataset1000.txt"
tamanio_archivo= 1000
dataset_entrenamiento, dataset_testing, dataset_validacion=dividir_dataset(archivo, tamanio_archivo, porcentaje_testing, porcentaje_validacion_3)

                
random.shuffle(dataset_entrenamiento)
random.shuffle(dataset_validacion)

error_global_entrenamiento=9999
error_global_valid=[9999,9998,-1]

umbral=0.001

i=0
while(((error_global_valid[0]>=error_global_valid[1]) or (error_global_valid[1]>=error_global_valid[2])) and (error_global_entrenamiento>umbral)):
    error_global_entrenamiento=red.entrenar_red(dataset_entrenamiento)
    
    if (i>1):
        error_global_valid[0]=error_global_valid[1]
        error_global_valid[1]=error_global_valid[2]
        error_global_valid[2]=red.validar_red(dataset_validacion)
    elif(i>0):
        error_global_valid[1]=error_global_valid[2]
        error_global_valid[2]=red.validar_red(dataset_validacion)
    else:
        error_global_valid[2]=red.validar_red(dataset_validacion)
   
    print(str(error_global_entrenamiento) + " " +str(error_global_valid[2]))
    i+= 1

red.escribir_pesos()
  


print("")


def obtener_dataset_test():
    return dataset_testing

def obtener_configuracion_red():
    return capas_ocultas, funcion_salida, funcion_capa_oculta, coef_aprendizaje, term_momento