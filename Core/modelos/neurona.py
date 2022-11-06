from random import random
import numpy as np

class Neurona():
    def __init__(self, funcion_transferencia, cant_neuronas_capa_anterior, coef_aprendizaje, term_momento, vector_w ):
        self._funcion_transferencia = funcion_transferencia
        self._cant_neuronas_capa_anterior = cant_neuronas_capa_anterior
        self._coef_aprendizaje = coef_aprendizaje
        self._term_momento = term_momento 

        self.vector_w = vector_w.copy()#vector de n pesos asociados a las n entradas (de capa anterior) de la neurona        
        
        self.net = 0
        self.salida = 0 #f(net)
        self.error = 0 #delta

        self.vector_delta_w = []

        self.vector_valores_entrada = []
      
    #Yn f(Net)
    #trata el string de entrada, donde cada dígito es la salida de una neurona de la capa anterior (en capa de entrada no, es una de las 100 entradas)
    def calcular_salida(self, vector_valores_entrada):
        #tratatar patron
       # print("vector entrada: ")
       # print(vector_valores_entrada)
        self.calcular_entrada_total( self._cant_neuronas_capa_anterior ,vector_valores_entrada)
       # print("net: "+ str(self.net))
        self.salida =  self._funcion_transferencia.calcular(self.net)
        return self.salida#plantear parametros

 
    #Netn    
    def calcular_entrada_total(self, cant_neuronas_capa_anterior, vector_valores_entrada):
        self.vector_valores_entrada = vector_valores_entrada
        if(cant_neuronas_capa_anterior==0):
            self.net = vector_valores_entrada #si es neurona de capa de entrada, net es igual a la unica entrada
        else:
            self.net=0
            for i in range(cant_neuronas_capa_anterior):
                self.net += self.vector_w[i+1] * vector_valores_entrada[i]
            self.net += self.vector_w[0] #ver si se suma o resta
     

    def calcular_error_en_capa_salida(self, salida_deseada): #error en neurona de salida
        self.error = (salida_deseada - self.salida) * self._funcion_transferencia.calcular_derivada(self.salida)
        return self.error


    def calcular_error_en_capa_oculta(self,pesos_capa_posterior, error_neuronas_capa_posterior):
        sumatoria = 0
        
        for i in range(len(pesos_capa_posterior)):
            sumatoria = sumatoria + (pesos_capa_posterior[i] * error_neuronas_capa_posterior[i])
           # self.mostrar(pesos_capa_posterior, error_neuronas_capa_posterior)
        self.error = self._funcion_transferencia.calcular_derivada(self.salida) * sumatoria
        return self.error

    def mostrar(self,pesos_capa_posterior, error_neuronas_capa_posterior):
        archivo="archivos_w\caso1.txt"
        with open(archivo, mode="a") as file:
            for i in range(len(pesos_capa_posterior)):
                file.write(str(pesos_capa_posterior[i])+"  "+str(error_neuronas_capa_posterior[i]))


    def actualizar_vector_pesos(self):
        #print(self.vector_w)
        #w_o se trata por separado con entrada = 1
        if self.vector_delta_w == []:
           w_0_siguiente = self.vector_w[0] + self._coef_aprendizaje * self.error * 1
           self.vector_delta_w.append(w_0_siguiente - self.vector_w[0]) 
        else:
            w_0_siguiente = self.vector_w[0] + self._coef_aprendizaje * self.error * 1 + self._term_momento * self.vector_delta_w[0]
            self.vector_delta_w[0] = w_0_siguiente - self.vector_w[0]

        self.vector_w[0] = w_0_siguiente
    
        #print(str(Decimal(w_0_siguiente))+"  "+str(self.vector_w[0])) 
        for i in range(1, len(self.vector_valores_entrada)):
            if self.vector_delta_w == [] or  len(self.vector_delta_w) != len(self.vector_w):
                w_siguiente = self.vector_w[i] + self._coef_aprendizaje * self.error * self.vector_valores_entrada[i-1] 
                self.vector_delta_w.append(w_siguiente - self.vector_w[i]) 
            else:
                w_siguiente = self.vector_w[i] + self._coef_aprendizaje * self.error * self.vector_valores_entrada[i-1] + self._term_momento * self.vector_delta_w[i]     
                self.vector_delta_w[i] =w_siguiente - self.vector_w[i] 
            #actualizo pesos para t+1

            self.vector_w[i] =  w_siguiente
 
        #print(self.vector_w)
        # print("Delta w")   
        # print(self.vector_delta_w)
        # print("w")  
        # print(self.vector_w)


        #actualizar pesos según la diferencia entre salida deseada y obtenida 
        # el vector_d es el vector de error proviene de la capa siguiente segun backpropagation
        # usar vector_w y vector_d para calcular el error_d en la neurona
        # desupués usar error_d para actualizar pesos 
       


