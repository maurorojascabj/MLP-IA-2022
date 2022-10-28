#matriz de pesos W
#se inicializa con valores aleatorioss

from core.funciones.lineal import lineal
from core.funciones.sigmoidal import sigmoidal
from core.modelos.Red import Red

#inputs
###dataset archivo
###porcentaje de conjunto de validacion

def inicializar_dataset_validacion(conjunto_inicial, porcentaje_de_validacion):

    return conjunto_inicial * porcentaje_de_validacion

porcentaje_testing = 0.2

porcentaje_validacion_1 = 0.1
porcentaje_validacion_2 = 0.2
porcentaje_validacion_3 = 0.3

funcion_sigmoidal  = sigmoidal()
funcion_lineal = lineal()



#tratar archivo: separar en 3 datasets
#llenar las 3 listas con los correspondientes patrones

red = Red(,funcion_sigmoidal,funcion_lineal,,)

# prueba con porcentaje_validacion_1
red.entrenar_red(dataset_entrenamiento_1, dataset_validacion_1)

# prueba con porcentaje_validacion_2
red.entrenar_red(dataset_entrenamiento_1, dataset_validacion_1)

# prueba con porcentaje_validacion_3

