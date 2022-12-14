#matriz de pesos W
#se inicializa con valores aleatorioss

import random
from Core.funciones.lineal import lineal
from Core.funciones.sigmoidal import sigmoidal
from Core.modelos.red import Red
from tratamiento_datasets.dividir_dataset import dividir_dataset
from tratamiento_datasets.matrices_pesos_por_capa import obtener_pesos
from tratamiento_datasets.errores_por_epoca import *
import os
os.system('cls||clear')

funcion_sigmoidal = sigmoidal()
funcion_lineal = lineal()

capas_ocultas=[10]
funcion_salida=funcion_sigmoidal
funcion_capa_oculta=funcion_lineal
coef_aprendizaje=0.5
term_momento=0.9


red  = Red(capas_ocultas, funcion_salida, funcion_capa_oculta, coef_aprendizaje, term_momento)

porcentaje_testing = 0.2
porcentaje_validacion_1 = 0.1
porcentaje_validacion_2 = 0.2
porcentaje_validacion_3 = 0.3

archivo_dataset="tratamiento_datasets\dataset1000.txt"
tamanio_archivo= 1000
dataset_entrenamiento, dataset_testing, dataset_validacion=dividir_dataset(archivo_dataset, tamanio_archivo, porcentaje_testing, porcentaje_validacion_2)

                
random.shuffle(dataset_entrenamiento)
random.shuffle(dataset_validacion)
random.shuffle(dataset_testing)

error_global_entrenamiento=9999
error_global_valid=0
umbral=0.001
k=0
exactitud_entrenamiento=0
exactitud_validacion=0

#paciencia=30 #se aplica early stopping si luego de 10 epocas no mejora el error global de validacion

archivo_pesos="archivos_w\pesos_app.txt"
archivo_errores="archivos_errores\errores_caso_100_1.txt"

while(error_global_entrenamiento>umbral):  #se realizan epocas mientras no se llegue al umbral de error de entrenamiento
    error_global_entrenamiento, exactitud =red.entrenar_red(dataset_entrenamiento)
    error_global_valid,exactitud_val=red.validar_red(dataset_validacion)
    
    print(str(error_global_entrenamiento) + " " + str(error_global_valid ))
    k+= 1
   
    exactitud_entrenamiento = exactitud
    exactitud_validacion = exactitud_val
    guardar_errores(archivo_errores,k,error_global_entrenamiento,error_global_valid)

print("cantidad de epocas:" + str(k))

# if(cont>=paciencia): #si se supera la paciencia, se aplica early stopping
#     print("se aplico early stopping")
#     red.aplicar_early_stopping

#print("exactitud entrenamiento: "+str(exactitud_entrenamiento) +" - exactitud validacion: "+ str(exactitud_validacion)) 
guardar_exactitud(archivo_errores, exactitud_entrenamiento)
guardar_exactitud(archivo_errores, exactitud_validacion)

red.escribir_pesos(archivo_pesos)
  



print("\n\n--------TESTING-------------")


red2  = Red(capas_ocultas, funcion_salida, funcion_capa_oculta, coef_aprendizaje, term_momento,obtener_pesos(archivo_pesos))
exactitud_test, precision_test= red2.test_red(dataset_testing)

#print("precision: ")
#print(precision_test)
#print("exactitud en testing:" + str(exactitud_test))
guardar_exactitud(archivo_errores, exactitud_test)
guardar_precision(archivo_errores, precision_test)

matriz_errores, exact_entrenamiento, exact_validacion, exact_test, precision=leer_archivo_errores(archivo_errores)

#print(matriz_errores)
print("exactitudes:"+ str(exact_entrenamiento)+" "+str(exact_validacion)+" "+str(exact_test))
print("precision test:"+str(precision_test[0])+" "+str(precision_test[1])+" "+str(precision_test[2])+" ")