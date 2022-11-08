#matriz de pesos W
#se inicializa con valores aleatorioss

import random
from Core.funciones.lineal import lineal
from Core.funciones.sigmoidal import sigmoidal
from Core.modelos.red import Red
from tratamiento_datasets.dividir_dataset import dividir_dataset
from tratamiento_datasets.matrices_pesos_por_capa import obtener_pesos


funcion_sigmoidal = sigmoidal()
funcion_lineal = lineal()

capas_ocultas=[5]
funcion_salida=funcion_sigmoidal
funcion_capa_oculta=funcion_lineal
coef_aprendizaje=0.5
term_momento=0.9


red  = Red(capas_ocultas, funcion_salida, funcion_capa_oculta, coef_aprendizaje, term_momento)

porcentaje_testing = 0.2
porcentaje_validacion_1 = 0.1
porcentaje_validacion_2 = 0.2
porcentaje_validacion_3 = 0.3

archivo="tratamiento_datasets\dataset1000.txt"
tamanio_archivo= 1000
dataset_entrenamiento, dataset_testing, dataset_validacion=dividir_dataset(archivo, tamanio_archivo, porcentaje_testing, porcentaje_validacion_3)

                
random.shuffle(dataset_entrenamiento)
random.shuffle(dataset_validacion)





error_global_entrenamiento=9999
error_global_valid=[9999,9998,-1]

umbral=0.001

i=0
exactitud_entrenamiento=0
exactitud_validacion=0
while(((error_global_valid[0]>=error_global_valid[1]) or (error_global_valid[1]>=error_global_valid[2])) and (error_global_entrenamiento>umbral)):
    error_global_entrenamiento, exactitud =red.entrenar_red(dataset_entrenamiento)
    
    if (i>1):
        error_global_valid[0]=error_global_valid[1]
        error_global_valid[1]=error_global_valid[2]
        error_global_valid[2],exactitud_val=red.validar_red(dataset_validacion)
    elif(i>0):
        error_global_valid[1]=error_global_valid[2]
        error_global_valid[2],exactitud_val=red.validar_red(dataset_validacion)
    else:
        error_global_valid[2],exactitud_val=red.validar_red(dataset_validacion)
   
    exactitud_entrenamiento = exactitud
    exactitud_validacion = exactitud_val
    print(str(error_global_entrenamiento) + " " + str(error_global_valid[2] ))
    i+= 1
    


print("cant epocas:" + str(i))
print("exactitud entrenamiento: "+str(exactitud_entrenamiento) +" exactitud validacion: "+ str(exactitud_validacion)) 

red.escribir_pesos()
  
# patron1 = '0000000000000001100000001001000000100000001111100000001000000000100000000010000000001000000000000000' #001 f
# patron2 = '0000000000001000000000100000000010000000001111100000100001000010000100001000010000111110000000000000' #100 b
# patron3 = '0000000000000000010000000001000000000100000111110000100001000010000100001000010000011111000000000000' #010 d
# vector_entrada=list(patron1) 
# list_salida_deseada=list('010') #se convierte el string que forma el patron ingresado en un vector
# salida_deseada =[int(x) for x in list_salida_deseada]
# ve=[int(x) for x in vector_entrada]

# red.clasificar_patron_maxarg(ve)


print("--------TESTING-------------")


red2  = Red(capas_ocultas, funcion_salida, funcion_capa_oculta, coef_aprendizaje, term_momento,obtener_pesos("archivos_w\caso2.txt"))
exactitud, precision= red2.test_red(dataset_testing)

print("precision: ")
print(precision)
print("exactitud en testing:" + str(exactitud))