#matriz de pesos W
#se inicializa con valores aleatorioss

from decimal import Decimal, getcontext
import random
from Core.funciones.lineal import lineal
from Core.funciones.sigmoidal import sigmoidal
from Core.modelos.red import Red
from tratamiento_datasets.dividir_dataset import dividir_dataset
from tratamiento_datasets.matrices_pesos_por_capa import obtener_pesos



funcion_sigmoidal = sigmoidal()
funcion_lineal = lineal()

#matriz_w = [[[ 0.0, 0.4 , 0.5],[ 0.0, 0.6 ,  0.8]],[[ 0.0, 0.7 , 0.2 ]]]

red  = Red([10,10], funcion_sigmoidal,funcion_sigmoidal,0.5,0.9)

porcentaje_testing = 0.2
porcentaje_validacion_1 = 0.1
porcentaje_validacion_2 = 0.2
porcentaje_validacion_3 = 0.3

archivo="dataset1000.txt"
tamanio_archivo= 1000
dataset_entrenamiento, dataset_testing, dataset_validacion=dividir_dataset(archivo, tamanio_archivo, porcentaje_testing, porcentaje_validacion_3)

# red.entrenar_red(dataset_entrenamiento)
# red.validar_red(dataset_validacion)

#obtener_pesos("archivos_w\caso1.txt")
                
random.shuffle(dataset_entrenamiento)
random.shuffle(dataset_validacion)

error_global_entrenamiento=9999
error_global_validacion_anterior=9999
error_global_validacion=-1
umbral=0.000001

i=0
while((error_global_entrenamiento>=error_global_validacion) and (error_global_entrenamiento>umbral)):
    error_global_entrenamiento=red.entrenar_red(dataset_entrenamiento)
    error_global_validacion= red.validar_red(dataset_validacion)
   

    print("error global entrenamiento: "+str(error_global_entrenamiento))
    print("error global validacion: "+str(error_global_validacion))
    
    print("epoca: "+str(i))
    i+= 1
    #print(red.error_global)


print("")



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
