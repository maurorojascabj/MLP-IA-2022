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