from Core.enums.Tipo_de_capa import Tipo_de_capa
from Core.modelos.capa import Capa
from Core.funciones.lineal import lineal
from tratamiento_datasets.matrices_pesos_por_capa import guardar_pesos


class Red():
    def __init__ (self, capas_ocultas, func_activacion_salida, func_activacion, coef_aprendizaje, term_momento, matrices_w = []):
        self._capas_ocultas =  capas_ocultas #vector con largo =  cantidad de capas y con cantidades de neurona por capa
        self._coef_aprendizaje =  coef_aprendizaje
        self._term_momento  = term_momento
        self._func_activacion_salida = func_activacion_salida # funcion de activación para la capa de entrada
        self._func_activacion =  func_activacion #funcion de activacion de clase "interfaz_funcion" para capas ocultas y de salida       

        self._cant_neuronas_entrada = 100
        self._cant_neuronas_salida =  3

        self.vector_de_activacion = []
        self.matrices_w = matrices_w
        self.capas = []
        self.error_patron = 0
        
        if (matrices_w == []):
            self.inicializar_capas()
        else:
            self.inicializar_capas_con_w()

    
    #>>>TRATAMIENTO DE CAPAS 
    def inicializar_capas(self):

        capa_de_entrada =Capa(self._cant_neuronas_entrada, lineal(), None, None, Tipo_de_capa.entrada, self._coef_aprendizaje, self._term_momento)  
        self.capas.append(capa_de_entrada)         

        capa_ant  = capa_de_entrada
        for capa_i in range(len(self._capas_ocultas)): #solo trata capas ocultas
            nueva_capa  = Capa(self._capas_ocultas[capa_i],self._func_activacion, capa_ant, None, Tipo_de_capa.oculta, self._coef_aprendizaje, self._term_momento)
            self.capas.append(nueva_capa)
            capa_ant.capa_siguiente = nueva_capa
            capa_ant =  nueva_capa
        

        capa_de_salida = Capa(self._cant_neuronas_salida, self._func_activacion_salida, capa_ant, None, Tipo_de_capa.salida, self._coef_aprendizaje, self._term_momento)          
        capa_ant.capa_siguiente = capa_de_salida
        self.capas.append(capa_de_salida)
 

    def inicializar_capas_con_w(self):

        capa_de_entrada = Capa(self._cant_neuronas_entrada, lineal(), None, None, Tipo_de_capa.entrada, self._coef_aprendizaje, self._term_momento)  
        self.capas.append(capa_de_entrada)         

        capa_ant  = capa_de_entrada
        for capa_i in range(len(self._capas_ocultas)): #solo trata capas ocultas
            nueva_capa  = Capa(self._capas_ocultas[capa_i],self._func_activacion, capa_ant, None, Tipo_de_capa.oculta, self._coef_aprendizaje, self._term_momento, self.matrices_w[capa_i])
            self.capas.append(nueva_capa)
            capa_ant.capa_siguiente = nueva_capa

            capa_ant =  nueva_capa

       

        capa_de_salida = Capa(self._cant_neuronas_salida, self._func_activacion_salida, capa_ant, None, Tipo_de_capa.salida, self._coef_aprendizaje, self._term_momento, self.matrices_w[len(self.matrices_w) - 1])   
        self.capas.append(capa_de_salida)
      

    #>>>MECANISMOS DE ENTRENAMIENTO 
    #realiza una corrida (epoca) de entrenamiento con 1 dataset a especificar
    def entrenar_patron (self, vector_patron):
    #mandar el patron a capa de entrada
        return self.capas[0].entrenar_patron(vector_patron)

    def entrenar_red (self,  dataset_entrenamiento, dataset_validacion):  
        i=0
        for renglon in dataset_entrenamiento:
            vector_entrada=list(renglon[0]) 
            list_salida_deseada=list(renglon[2]) #se convierte el string que forma el patron ingresado en un vector
            salida_deseada =[int(x) for x in list_salida_deseada]
            salida_obtenida = self.entrenar_patron([int(x) for x in vector_entrada]) 
            self.error_patron = self.calcular_error_patron(salida_obtenida, salida_deseada)        
            self.calculo_y_propagacion_de_errores(salida_deseada)
            self.matrices_w = self.actualizar_pesos()
             #con esta salida, calculo el error, y despues corrijo
            #[int(x) for x in vector_entrada] convierte cada caracter (0 o 1) del vector en un entero
            i+=1
            #print( str(i) +''+ str(salida))
       
        guardar_pesos("archivos_w\caso1.txt",self.matrices_w)

    def calculo_y_propagacion_de_errores(self, salida_deseada):
        errores_capa_posterior = None
        for i in range(len(self.capas)-1, 0, -1):
            capa = self.capas[i]
            if (capa.capa_anterior != Tipo_de_capa.entrada):
                errores_capa = capa.calcular_error(salida_deseada, errores_capa_posterior)
                errores_capa_posterior = errores_capa

    def actualizar_pesos(self):
        matrices_w_actualizada = []     
        for capa in self.capas:
            if capa.tipo != Tipo_de_capa.entrada:
                matrices_w_actualizada.append(capa.actualizar_pesos())
        return matrices_w_actualizada    
    



    def calcular_error_patron(self,salida_obtenida, salida_desada):
        sumatoria = 0
        for i in range(len(salida_obtenida)):
            sumatoria +=((salida_obtenida[i]-salida_desada[i]) * self._func_activacion_salida.calcular_derivada(salida_obtenida[i]))**2
        return sumatoria/2        


    #>>>MECANISMOS DE CLASIFICACION   
    #recive un patron y devuelve la clasificacion calculada por la red    
    def clasificar_patron():
        pass

    def clasificar_patron_devolver_error():
        pass

    #>>>MECANISMOS DE ACTUALIZACION DE VARIABLES
    def actualizar_vector_de_activacion():
        pass

    def calcular_error_global():
        pass


    #matriz W tiene un vector de longitud = (100 + 1 por el umbral) por cada neurona de capa oculta


