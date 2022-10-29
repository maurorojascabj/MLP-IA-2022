#matriz de pesos W
#se inicializa con valores aleatorioss

#from core.funciones.lineal import lineal
#from core.funciones.sigmoidal import sigmoidal
#from core.modelos.Red import Red

#inputs
###dataset archivo
###porcentaje de conjunto de validacion

def inicializar_dataset_validacion(conjunto_inicial, porcentaje_de_validacion):

    return conjunto_inicial * porcentaje_de_validacion


def dividir_dataset(dataset, tamanio_dataset,porc_testing, porc_validacion):
    dataset_entrenamiento=list()
    dataset_validacion=list()
    dataset_testing=list()
    cantNoDistorsionada= tamanio_dataset // 10
    cantDistorsionada= tamanio_dataset - cantNoDistorsionada
    cant_validacion_distors= round(cantDistorsionada * porc_validacion)
    cant_testing_distors= round(cantDistorsionada * porc_testing)
    cant_validacion_no_distors= round(cantNoDistorsionada * porc_validacion)
    cant_testing_no_distors= round(cantNoDistorsionada * porc_testing)

    with open(dataset, mode="r") as archivo:
       for indice,linea in enumerate(archivo):
        ejemplo=linea.split()
        if (indice < cantNoDistorsionada):
            if(indice < cant_validacion_no_distors):
                dataset_validacion.append(ejemplo)
            elif (indice < cant_validacion_no_distors + cant_testing_no_distors):
                dataset_testing.append(ejemplo)
            else:
                dataset_entrenamiento.append(ejemplo)
        else:
            if(indice < cantNoDistorsionada + cant_validacion_distors):
                dataset_validacion.append(ejemplo)
            elif (indice < cantNoDistorsionada + cant_validacion_distors + cant_testing_distors):
                dataset_testing.append(ejemplo)
            else:
                dataset_entrenamiento.append(ejemplo)


    return dataset_entrenamiento,dataset_testing,dataset_validacion







porcentaje_testing = 0.2

porcentaje_validacion_1 = 0.1
porcentaje_validacion_2 = 0.2
porcentaje_validacion_3 = 0.3

#funcion_sigmoidal  = sigmoidal()
#funcion_lineal = lineal()

archivo="c:/Users/USER/Documents/ISI 5TO/INTELIGENCIA ARTIFICIAL/TPI/dataset1000.txt"
entr,test,val=dividir_dataset(archivo,1000,0.15,0.3)
print(len(entr))
print(len(test))
print(len(val))

print(val[5])


#tratar archivo: separar en 3 datasets
#llenar las 3 listas con los correspondientes patrones

#red = Red(,funcion_sigmoidal,funcion_lineal,,)

# prueba con porcentaje_validacion_1
#red.entrenar_red(dataset_entrenamiento_1, dataset_validacion_1)

# prueba con porcentaje_validacion_2
#red.entrenar_red(dataset_entrenamiento_1, dataset_validacion_1)

# prueba con porcentaje_validacion_3
