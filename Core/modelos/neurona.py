from random import random


class Neurona():
    def __init__(self, funcion_transferencia, cant_neuronas_capa_anterior, coef_aprendizaje, term_momento, vector_w ):
        self._funcion_transferencia = funcion_transferencia
        self._cant_neuronas_capa_anterior = cant_neuronas_capa_anterior
        self._coef_aprendizaje = coef_aprendizaje
        self._term_momento = term_momento 

        self.vector_w = vector_w#vector de n pesos asociados a las n entradas (de capa anterior) de la neurona        
        self.umbral_w_0 = self.vector_w[0]     
        self.valor_estado_activacion = 1 #self.calcular_estado_activacion()

        self.net = 0
        self.salida = 0 #f(net)
        self.error = 0 #delta
        self.vector_delta_w = self.vector_w 
        self.vector_valores_entrada = []
      
    #Yn f(Net)
    #trata el string de entrada, donde cada dígito es la salida de una neurona de la capa anterior (en capa de entrada no, es una de las 100 entradas)
    def calcular_salida(self, vector_valores_entrada):
        #tratatar patron
        self.calcular_entrada_total( self._cant_neuronas_capa_anterior ,vector_valores_entrada)
        self.salida =  self._funcion_transferencia.calcular(self.net)   
        return self.salida#plantear parametros

 
    #Netn    
    def calcular_entrada_total(self, cant_neuronas_capa_anterior, vector_valores_entrada):
        self.vector_valores_entrada = vector_valores_entrada
        if(cant_neuronas_capa_anterior==0):
            self.net = vector_valores_entrada[0] #si es neurona de capa de entrada, net es igual a la unica entrada
        else:
            self.net=0
            for i in range(cant_neuronas_capa_anterior):
                self.net =+ self.vector_w[i] * vector_valores_entrada[i]
            self.net =+ self.umbral_w_0 #ver si se suma o resta
     

    def calcular_error_en_capa_salida(self, salida_deseada): #error en neurona de salida
        self.error = (salida_deseada - self.salida) * self._funcion_transferencia.calcular_derivada(self.net)
        return self.error


    def calcular_error_en_capa_oculta(self,pesos_capa_posterior, error_neuronas_capa_posterior):
        sumatoria = 0
        for i in range(len(pesos_capa_posterior)):
            sumatoria += pesos_capa_posterior[i] * error_neuronas_capa_posterior[i]
        self.error = self._funcion_transferencia.calcular_derivada(self.net) * sumatoria
        return self.error


    def actualizar_vector_pesos(self):

        #w_o se trata por separado con entrada = 1
        w_0_siguiente = self.vector_w[0] + self._coef_aprendizaje * self.error * 1 + self._term_momento * self.vector_delta_w[0]
        self.vector_delta_w[0] = w_0_siguiente - self.vector_w[0] 
        self.vector_w[0] =  w_0_siguiente


        for i in range(1, len(self.vector_valores_entrada)):
            w_siguiente = self.vector_w[i] + self._coef_aprendizaje * self.error * self.vector_valores_entrada[i] + self._term_momento * self.vector_delta_w[i]            
            #actualizo pesos para t+1
            self.vector_delta_w[i] = w_siguiente - self.vector_w[i] 
            self.vector_w[i] =  w_siguiente
           



        #actualizar pesos según la diferencia entre salida deseada y obtenida 
        # el vector_d es el vector de error proviene de la capa siguiente segun backpropagation
        # usar vector_w y vector_d para calcular el error_d en la neurona
        # desupués usar error_d para actualizar pesos 
       


