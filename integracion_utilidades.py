import random
from Core.funciones.lineal import lineal
from Core.funciones.sigmoidal import sigmoidal
from Core.modelos.red import Red
from tratamiento_datasets.matrices_pesos_por_capa import obtener_pesos
from tratamiento_datasets.dividir_dataset import dividir_dataset
from tratamiento_datasets.errores_por_epoca import *
import os
os.system('cls||clear')


def obtener_red_precargada(dic):
    red, archivo_errores = seleccionar_archivo_y_generar_red(dic['tam_dataset'], dic['capas_config'], dic['term_momento'], dic['porc_validacion'])
    return red, archivo_errores


def entrenar_y_obtener_red(dic):
    with open("archivos_errores\errores_app.txt", 'r+') as f:
        f.truncate()

    if dic['func_de_transferencia'] == 0:
        funcion_transf_ocultas = lineal()
    else:
        funcion_transf_ocultas = sigmoidal() 

    red = Red(dic['capas_config'],sigmoidal(),funcion_transf_ocultas, dic['coef_aprendizaje'] ,dic['term_momento'])
    

    porcentaje_validacion = (dic['porc_validacion'])/100
    porcentaje_testing = 0.2
    if dic['tam_dataset'] == 100:
       archivo="tratamiento_datasets\dataset100.txt"
       tamanio_archivo= 100  
    elif dic['tam_dataset'] == 500:
        archivo="tratamiento_datasets\dataset500.txt"
        tamanio_archivo= 500  
    else:
        archivo="tratamiento_datasets\dataset1000.txt"  
        tamanio_archivo= 1000  

  
    dataset_entrenamiento, dataset_testing, dataset_validacion= dividir_dataset(archivo, tamanio_archivo, porcentaje_testing, porcentaje_validacion)

                
    random.shuffle(dataset_entrenamiento)
    random.shuffle(dataset_validacion)
    random.shuffle(dataset_testing)

    error_global_entrenamiento=9999
    error_global_valid=0
    umbral=0.001
    k=0
    exactitud_entrenamiento=0
    exactitud_validacion=0

    while(error_global_entrenamiento>umbral):  #se realizan epocas mientras no se llegue al umbral de error de entrenamiento
        error_global_entrenamiento, exactitud =red.entrenar_red(dataset_entrenamiento)
        error_global_valid,exactitud_val=red.validar_red(dataset_validacion)
    
        print(str(error_global_entrenamiento) + " " + str(error_global_valid ))
        k+= 1
   
        exactitud_entrenamiento = exactitud
        exactitud_validacion = exactitud_val

        print("cantidad de epocas:" + str(k))

        print("exactitud entrenamiento: "+str(exactitud_entrenamiento) +" - exactitud validacion: "+ str(exactitud_validacion)) 

        red.escribir_pesos("archivos_w\pesos_app.txt")
        guardar_errores("archivos_errores\errores_app.txt",k,error_global_entrenamiento,error_global_valid)
    guardar_exactitud("archivos_errores\errores_app.txt", exactitud_entrenamiento)
    guardar_exactitud("archivos_errores\errores_app.txt", exactitud_validacion)

    return red




# self.diccionarioDatos = {
#     "tam_dataset": "",
#     "capas_config": [],
#     "func_de_transferencia": "",
#     "coef_aprendizaje": "",
#     "term_momento": "",
#     "porc_validacion": ""
# }


def seleccionar_archivo_y_generar_red(tam_dataset, capas_confi, term_momento, porc_validacion ):
  
    funcion_salida = sigmoidal()
    funcion_ocultas = lineal()
    coef_aprend = 0.5
    archivo  = ""

    if tam_dataset == 100:

        if capas_confi == [5]:
            
            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_100_1.txt"
                   archivo_errores="archivos_errores\errores_caso_100_1.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_100_9.txt"
                    archivo_errores="archivos_errores\errores_caso_100_9.txt"
                else: #30
                    archivo = "archivos_w\caso_100_17.txt"
                    archivo_errores="archivos_errores\errores_caso_100_17.txt"       

            else:#0.9
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_100_5.txt"
                    archivo_errores="archivos_errores\errores_caso_100_5.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_100_13.txt"
                    archivo_errores="archivos_errores\errores_caso_100_13.txt"
                else: #30
                    archivo = "archivos_w\caso_100_21.txt"
                    archivo_errores="archivos_errores\errores_caso_100_21.txt"   

        elif capas_confi == [10]:

            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_100_2.txt"
                   archivo_errores="archivos_errores\errores_caso_100_2.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_100_10.txt"
                    archivo_errores="archivos_errores\errores_caso_100_10.txt"
                else: #30
                    archivo = "archivos_w\caso_100_18.txt"  
                    archivo_errores="archivos_errores\errores_caso_100_18.txt"     

            else:
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_100_6.txt"
                    archivo_errores="archivos_errores\errores_caso_100_6.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_100_14.txt"
                    archivo_errores="archivos_errores\errores_caso_100_14.txt"
                else: #30
                    archivo = "archivos_w\caso_100_22.txt"  
                    archivo_errores="archivos_errores\errores_caso_100_22.txt"

        elif capas_confi == [5,5]:

            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_100_3.txt"
                   archivo_errores="archivos_errores\errores_caso_100_3.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_100_11.txt"
                    archivo_errores="archivos_errores\errores_caso_100_11.txt"
                else: #30
                    archivo = "archivos_w\caso_100_19.txt"   
                    archivo_errores="archivos_errores\errores_caso_100_19.txt"    

            else:
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_100_7.txt"
                    archivo_errores="archivos_errores\errores_caso_100_7.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_100_15.txt"
                    archivo_errores="archivos_errores\errores_caso_100_15.txt"
                else: #30
                    archivo = "archivos_w\caso_100_23.txt"  
                    archivo_errores="archivos_errores\errores_caso_100_23.txt"
        else: #[10,10]

            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_100_4.txt"
                   archivo_errores="archivos_errores\errores_caso_100_4.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_100_12.txt"
                    archivo_errores="archivos_errores\errores_caso_100_12.txt"
                else: #30
                    archivo = "archivos_w\caso_100_20.txt"   
                    archivo_errores="archivos_errores\errores_caso_100_20.txt"    

            else:
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_100_8.txt"
                    archivo_errores="archivos_errores\errores_caso_100_8.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_100_16.txt"
                    archivo_errores="archivos_errores\errores_caso_100_16.txt"
                else: #30
                    archivo = "archivos_w\caso_100_24.txt"  
                    archivo_errores="archivos_errores\errores_caso_100_24.txt"

    elif tam_dataset == 500:
        if capas_confi == [5]:
            
            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_500_1.txt"
                   archivo_errores="archivos_errores\errores_caso_500_1.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_500_9.txt"
                    archivo_errores="archivos_errores\errores_caso_500_9.txt"
                else: #30
                    archivo = "archivos_w\caso_500_17.txt"       
                    archivo_errores="archivos_errores\errores_caso_500_17.txt"

            else:#0.9
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_500_5.txt"
                    archivo_errores="archivos_errores\errores_caso_500_5.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_500_13.txt"
                    archivo_errores="archivos_errores\errores_caso_500_13.txt"
                else: #30
                    archivo = "archivos_w\caso_500_21.txt"   
                    archivo_errores="archivos_errores\errores_caso_500_21.txt"

        elif capas_confi == [10]:

            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_500_2.txt"
                   archivo_errores="archivos_errores\errores_caso_500_2.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_500_10.txt"
                    archivo_errores="archivos_errores\errores_caso_500_10.txt"
                else: #30
                    archivo = "archivos_w\caso_500_18.txt"      
                    archivo_errores="archivos_errores\errores_caso_500_18.txt" 

            else:
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_500_6.txt"
                    archivo_errores="archivos_errores\errores_caso_500_6.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_500_14.txt"
                    archivo_errores="archivos_errores\errores_caso_500_14.txt"
                else: #30
                    archivo = "archivos_w\caso_500_22.txt"  
                    archivo_errores="archivos_errores\errores_caso_500_22.txt"

        elif capas_confi == [5,5]:

            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_500_3.txt"
                   archivo_errores="archivos_errores\errores_caso_500_3.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_500_11.txt"
                    archivo_errores="archivos_errores\errores_caso_500_11.txt"
                else: #30
                    archivo = "archivos_w\caso_500_19.txt"   
                    archivo_errores="archivos_errores\errores_caso_500_19.txt"    

            else:
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_500_7.txt"
                    archivo_errores="archivos_errores\errores_caso_500_7.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_500_15.txt"
                    archivo_errores="archivos_errores\errores_caso_500_15.txt"
                else: #30
                    archivo = "archivos_w\caso_500_23.txt"  
                    archivo_errores="archivos_errores\errores_caso_500_23.txt"
        else: #[10,10]

            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_500_4.txt"
                   archivo_errores="archivos_errores\errores_caso_500_4.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_500_12.txt"
                    archivo_errores="archivos_errores\errores_caso_500_12.txt"
                else: #30
                    archivo = "archivos_w\caso_500_20.txt"    
                    archivo_errores="archivos_errores\errores_caso_500_20.txt"   

            else:
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_500_8.txt"
                    archivo_errores="archivos_errores\errores_caso_500_8.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_500_16.txt"
                    archivo_errores="archivos_errores\errores_caso_500_16.txt"
                else: #30
                    archivo = "archivos_w\caso_500_24.txt"  
                    archivo_errores="archivos_errores\errores_caso_500_24.txt"
    else:# 1000
        if capas_confi == [5]:
            
            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_1000_1.txt"
                   archivo_errores="archivos_errores\errores_caso_1000_1.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_1000_9.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_9.txt"
                else: #30
                    archivo = "archivos_w\caso_1000_17.txt"     
                    archivo_errores="archivos_errores\errores_caso_1000_17.txt"  

            else:#0.9
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_1000_5.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_5.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_1000_13.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_13.txt"
                else: #30
                    archivo = "archivos_w\caso_1000_21.txt"   
                    archivo_errores="archivos_errores\errores_caso_1000_21.txt"

        elif capas_confi == [10]:

            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_1000_2.txt"
                   archivo_errores="archivos_errores\errores_caso_1000_2.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_1000_10.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_10.txt"
                else: #30
                    archivo = "archivos_w\caso_1000_18.txt"    
                    archivo_errores="archivos_errores\errores_caso_1000_18.txt"   

            else:
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_1000_6.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_6.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_1000_14.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_14.txt"
                else: #30
                    archivo = "archivos_w\caso_1000_22.txt"  
                    archivo_errores="archivos_errores\errores_caso_1000_22.txt"

        elif capas_confi == [5,5]:

            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_1000_3.txt"
                   archivo_errores="archivos_errores\errores_caso_1000_3.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_1000_11.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_11.txt"
                else: #30
                    archivo = "archivos_w\caso_1000_19.txt"       
                    archivo_errores="archivos_errores\errores_caso_1000_19.txt"

            else:
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_1000_7.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_7.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_1000_15.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_15.txt"
                else: #30
                    archivo = "archivos_w\caso_1000_23.txt"  
                    archivo_errores="archivos_errores\errores_caso_1000_23.txt"
        else: #[10,10]

            if term_momento == 0.5:
                
                if porc_validacion == 10:
                   archivo = "archivos_w\caso_1000_4.txt"
                   archivo_errores="archivos_errores\errores_caso_1000_4.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_1000_12.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_12.txt"
                else: #30
                    archivo = "archivos_w\caso_1000_20.txt"  
                    archivo_errores="archivos_errores\errores_caso_1000_20.txt"     

            else:
                if porc_validacion == 10:
                    archivo = "archivos_w\caso_1000_8.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_8.txt"
                elif porc_validacion == 20 :
                    archivo = "archivos_w\caso_1000_16.txt"
                    archivo_errores="archivos_errores\errores_caso_1000_16.txt"
                else: #30
                    archivo = "archivos_w\caso_1000_24.txt" 
                    archivo_errores="archivos_errores\errores_caso_1000_24.txt" 
    

    red  = Red(capas_confi, funcion_salida, funcion_ocultas, coef_aprend, term_momento, obtener_pesos(archivo)  )    

    return red, archivo_errores