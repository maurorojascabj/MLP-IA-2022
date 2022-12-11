
from Core.enums.Tipo_de_capa import Tipo_de_capa
from Core.modelos.capa import Capa
from Core.funciones.lineal import lineal
from Core.funciones.identidad import identidad
from tratamiento_datasets.matrices_pesos_por_capa import guardar_pesos
import numpy as np


class Red():
    def __init__ (self, capas_ocultas, func_transferencia_salida, func_transferencia_ocultas, coef_aprendizaje, term_momento, matrices_w = []):
        self._capas_ocultas =  capas_ocultas #vector con largo =  cantidad de capas y con cantidades de neurona por capa
        self._coef_aprendizaje =  coef_aprendizaje
        self._term_momento  = term_momento
        self._func_transferencia_salida = func_transferencia_salida # funcion de activación para la capa de entrada
        self._func_transferencia_ocultas=  func_transferencia_ocultas #funcion de activacion de clase "interfaz_funcion" para capas ocultas y de salida       

        self._cant_neuronas_entrada = 100
        self._cant_neuronas_salida =  3

        self.vector_de_activacion = []
        self.matrices_w = matrices_w.copy()
        #self.matriz_early_stopping=[]
        self.capas = []
        self.acumulacion_i_errores_entrenamiento = 0
        self.acumulacion_i_patrones_entrenamiento = 0
        self.error_global_entrenamiento = 0

        self.acumulacion_i_errores_validacion = 0
        self.acumulacion_i_patrones_validacion = 0
        self.error_global_validacion = 0

        self.acumulacion_i_patrones_test=0
        self.exactitud_test=0
        self.verdaderos_positivos=[0,0,0]
        self.falsos_positivos=[0,0,0]
        self.precision_test=[0,0,0]

        self.exactitud_entrenamiento = 0
        self.exactitud_validacion = 0

        
        if (matrices_w == []):
            self.inicializar_capas()
        else:
            self.inicializar_capas_con_w()

    
    #>>>TRATAMIENTO DE CAPAS 
    def inicializar_capas(self): #se inicializa capas con pesos aleatorios, cuando se empieza a entrenar la red

        capa_de_entrada =Capa(self._cant_neuronas_entrada, lineal(), None, None, Tipo_de_capa.entrada, self._coef_aprendizaje, self._term_momento)  
        self.capas.append(capa_de_entrada)         

        capa_ant  = capa_de_entrada
        for capa_i in range(len(self._capas_ocultas)): #solo trata capas ocultas
            nueva_capa  = Capa(self._capas_ocultas[capa_i],self._func_transferencia_ocultas, capa_ant, None, Tipo_de_capa.oculta, self._coef_aprendizaje, self._term_momento)
            self.capas.append(nueva_capa)
            capa_ant.capa_siguiente = nueva_capa
            capa_ant =  nueva_capa
        

        capa_de_salida = Capa(self._cant_neuronas_salida, self._func_transferencia_salida, capa_ant, None, Tipo_de_capa.salida, self._coef_aprendizaje, self._term_momento)          
        capa_ant.capa_siguiente = capa_de_salida
        self.capas.append(capa_de_salida)
 

    def inicializar_capas_con_w(self): #se inicializa capas con pesos almacenados en archivos obtenidos del previo entrenamiento, para etapa de test

        capa_de_entrada = Capa(self._cant_neuronas_entrada, lineal(), None, None, Tipo_de_capa.entrada, self._coef_aprendizaje, self._term_momento)  
        self.capas.append(capa_de_entrada)         

        capa_ant  = capa_de_entrada
        for capa_i in range(len(self._capas_ocultas)): #solo trata capas ocultas
            nueva_capa  = Capa(self._capas_ocultas[capa_i],self._func_transferencia_ocultas, capa_ant, None, Tipo_de_capa.oculta, self._coef_aprendizaje, self._term_momento, self.matrices_w[capa_i])
            self.capas.append(nueva_capa)
            capa_ant.capa_siguiente = nueva_capa

            capa_ant =  nueva_capa       

        capa_de_salida = Capa(self._cant_neuronas_salida, self._func_transferencia_salida, capa_ant, None, Tipo_de_capa.salida, self._coef_aprendizaje, self._term_momento, self.matrices_w[len(self.matrices_w) - 1])   
        capa_ant.capa_siguiente = capa_de_salida
        self.capas.append(capa_de_salida)
      

    #>>>MECANISMOS DE ENTRENAMIENTO 
    #realiza una corrida (epoca) de entrenamiento con 1 dataset a especificar
    
    def entrenar_patron (self, vector_patron):
    #mandar el patron a capa de entrada
        return self.capas[0].entrenar_patron(vector_patron)

    def entrenar_red (self,  dataset_entrenamiento):  
        i=0
        desaciertos_entrenamiento = 0
        for renglon in dataset_entrenamiento:
            vector_entrada=list(renglon[0]) 
            list_salida_deseada=list(renglon[2]) #se convierte el string que forma el patron ingresado en un vector
            salida_deseada =[int(x) for x in list_salida_deseada] #para convertir cada caracter (0 o 1) del vector en un entero
            ve=[int(x) for x in vector_entrada]
            salida_obtenida = self.entrenar_patron(ve) 
            salida_codificada = self.codificar_salida(salida_obtenida)
            self.acumulacion_i_errores_entrenamiento += self.calcular_error_patron(salida_obtenida, salida_deseada)      
            self.calculo_y_propagacion_de_errores(salida_deseada)            
            self.matrices_w = self.actualizar_pesos()

            if(salida_codificada!=salida_deseada):
                desaciertos_entrenamiento+= 1

            i+=1
            self.acumulacion_i_patrones_entrenamiento+=1           
            
        self.error_global_entrenamiento=self.calcular_error_global(self.acumulacion_i_errores_entrenamiento, self.acumulacion_i_patrones_entrenamiento)
        self.exactitud_entrenamiento = (len(dataset_entrenamiento) - desaciertos_entrenamiento) /len(dataset_entrenamiento)*100
        return self.error_global_entrenamiento, self.exactitud_entrenamiento
       
    # def epoca_minimo_error_validacion(self):
    #     self.matriz_early_stopping=self.matrices_w.copy()

    # def aplicar_early_stopping(self):
    #     self.matrices_w=self.matriz_early_stopping

    def escribir_pesos(self):    #se escribe los pesos wi obtenidos del entrenamiento en archivo
        guardar_pesos("archivos_w\casos.txt",self.matrices_w) 


    
    #>>>MECANISMOS DE CLASIFICACION   
    #recive un patron y devuelve la clasificacion calculada por la red    
 
    def clasificar_patron_umbral(self, patron):
        pass



    def clasificar_patron_maxarg(self, patron):

        salida = {
                "0": [1,0,0],
                "1": [0,1,0],
                "2": [0,0,1]
                }

        salida_obtenida = self.entrenar_patron(patron)     	
        	
        max = np.argmax(salida_obtenida)

        return salida[str(max.T)]


     

    def codificar_salida(self, salida_obtenida):

        salida = {
                "0": [1,0,0],
                "1": [0,1,0],
                "2": [0,0,1]
                } 	
        	
        max = np.argmax(salida_obtenida)

        return salida[str(max.T)]   

    #>>>MECANISMOS DE ACTUALIZACION DE VARIABLES
    def calculo_y_propagacion_de_errores(self, salida_deseada): #se calcula los errores desde la capa de salida hacia atras
        errores_capa_posterior = None
        for i in range(len(self.capas)-1, 0, -1):
            capa = self.capas[i]
            if (capa.tipo != Tipo_de_capa.entrada):#
                errores_capa = capa.calcular_error(salida_deseada, errores_capa_posterior)            
                errores_capa_posterior = errores_capa.copy()  

    def actualizar_pesos(self): #se actualizan los pesos de neuronas que no sean de la capa de entrada
        matrices_w_actualizada = []     
        for capa in self.capas:
            if capa.tipo != Tipo_de_capa.entrada:
                matrices_w_actualizada.append(capa.actualizar_pesos())
        return matrices_w_actualizada    
    
    
    def calcular_error_patron(self,salida_obtenida, salida_deseada): #se calcula el error obtenido en cada patron presentado a la red
        sumatoria = 0
        for i in range(len(salida_obtenida)):
            sumatoria +=((salida_deseada[i]-salida_obtenida[i]) * self._func_transferencia_salida.calcular_derivada(salida_obtenida[i]))**2
        return sumatoria/2  


    def calcular_error_global(self, acumulacion_i_errores, acumulacion_i_patrones): #se calcula error global a partir de errores de patrones
        error_global = acumulacion_i_errores / acumulacion_i_patrones
        
        return error_global


    #matriz W tiene un vector de longitud = (100 + 1 por el umbral) por cada neurona de capa oculta

    #>>>MECANISMOS DE VALIDACION 
    #realiza una corrida (epoca) de validacion con 1 dataset a especificar
    #mismo mecanismo que el entrenamiento para calcular la salida obtenida y errores pero sin actualizar pesos
    def validar_red (self,  dataset_validacion):  
        i=0
        desaciertos_validacion = 0 
        for renglon in dataset_validacion:
            vector_entrada=list(renglon[0]) 
            list_salida_deseada=list(renglon[2]) #se convierte el string que forma el patron ingresado en un vector
            salida_deseada =[int(x) for x in list_salida_deseada]
            ve=[int(x) for x in vector_entrada]
            salida_obtenida = self.entrenar_patron(ve) 
            salida_codificada = self.codificar_salida(salida_obtenida)
            self.acumulacion_i_errores_validacion += self.calcular_error_patron(salida_obtenida, salida_deseada)  

            if(salida_codificada!=salida_deseada):
                desaciertos_validacion+= 1

            i+=1
            self.acumulacion_i_patrones_validacion+=1

        self.error_global_validacion=self.calcular_error_global(self.acumulacion_i_errores_validacion, self.acumulacion_i_patrones_validacion)
        self.exactitud_validacion = (len(dataset_validacion) - desaciertos_validacion)/len(dataset_validacion)*100
        return self.error_global_validacion, self.exactitud_validacion 


    #>>>MECANISMOS DE TESTING 
    #realiza una corrida (epoca) de entrenamiento con 1 dataset a especificar
    #mismo mecanismo que el entrenamiento y validacion para calcular la salida obtenida pero sin actualizar pesos ni calcular errores
    def test_red (self,  dataset_test):  
        i=0
        aciertos=0
        for renglon in dataset_test:
            vector_entrada=list(renglon[0]) 
            list_salida_deseada=list(renglon[2]) #se convierte el string que forma el patron ingresado en un vector
            salida_deseada =[int(x) for x in list_salida_deseada]
            ve=[int(x) for x in vector_entrada]           
            salida_maxarg = self.clasificar_patron_maxarg(ve)
            k=0

            if(salida_maxarg==salida_deseada):
                aciertos+= 1
            else:     
                print("deseada ",str(salida_deseada)+" - obtenida "+str(salida_maxarg))
                print(vector_entrada)
                print("porcentaje distorsion: "+renglon[1])
            
            i+=1
            self.acumulacion_i_patrones_test+=1
            self.calcular_positivos_precision_red(salida_maxarg, salida_deseada)
        self.exactitud_test=aciertos / self.acumulacion_i_patrones_test
        self.obtener_precision_por_letra()
           
        return self.exactitud_test, self.precision_test
    
    def calcular_positivos_precision_red(self, salida_obtenida, salida_deseada):
        if(salida_obtenida[0]==1 and salida_obtenida[1]==0 and salida_obtenida[2]==0):
            if(salida_obtenida==salida_deseada):
                self.verdaderos_positivos[0]+=1
            else:
                self.falsos_positivos[0]+=1
        elif(salida_obtenida[0]==0 and salida_obtenida[1]==1 and salida_obtenida[2]==0):
            if(salida_obtenida==salida_deseada):
                self.verdaderos_positivos[1]+=1
            else:
                self.falsos_positivos[1]+=1
        elif(salida_obtenida[0]==0 and salida_obtenida[1]==0 and salida_obtenida[2]==1):
            if(salida_obtenida==salida_deseada):
                self.verdaderos_positivos[2]+=1
            else:
                self.falsos_positivos[2]+=1

    def obtener_precision_por_letra(self):
        for i in range(3):
            if(self.verdaderos_positivos[i]>0 or self.falsos_positivos[i]>0):
                self.precision_test[i]=self.verdaderos_positivos[i]/(self.verdaderos_positivos[i]+self.falsos_positivos[i])
            else:
                self.precision_test[i]=0
