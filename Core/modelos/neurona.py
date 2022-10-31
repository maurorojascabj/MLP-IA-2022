from random import random


class Neurona():
    def __init__(self, funcion_salida, cant_neuronas_capa_anterior, vector_w ):
        self._funcion_salida = funcion_salida
        self._cant_neuronas_capa_anterior = cant_neuronas_capa_anterior

        self.vector_w = vector_w#vector de n pesos asociados a las n entradas (de capa anterior) de la neurona        
        self.umbral_w_0 = self.vector_w[0]     
        self.valor_estado_activacion = 1 #self.calcular_estado_activacion()
      
    #Yn f(Net)
    #trata el string de entrada, donde cada dígito es la salida de una neurona de la capa anterior (en capa de entrada no, es una de las 100 entradas)
    def calcular_salida(self, vector_valores_entrada):
        #tratatar patron
        net = self.calcular_entrada_total( self._cant_neuronas_capa_anterior ,vector_valores_entrada)    
        return self._funcion_salida.calcular(net)#plantear parametros

        

    #a(t)n ALERTA: capaz hay que sacar porque no se usa
    def calcular_estado_activacion():
        pass

    #Netn    
    def calcular_entrada_total(self, cant_neuronas_capa_anterior, vector_valores_entrada):
        if(cant_neuronas_capa_anterior==0):
            net = vector_valores_entrada #si es neurona de capa de entrada, net es igual a la unica entrada
        else:
            net=0
            for i in range(cant_neuronas_capa_anterior):
                net = net + self.vector_w[i] * vector_valores_entrada[i]
            net =  net + self.umbral_w_0 #ver si se suma o resta
        return net

    #para darle valores aleatorios iniciales al vector w   
    def inicializar_pesos(self, cant_neuronas_capa_anterior):
        for entrada_capa_anterior in range(cant_neuronas_capa_anterior):#creo el vector w de largo igual a cantidad de neuronas de la capa anterior
            self.vector_w.append(random) # asigno a cada peso un valor aleatorio. ALERTA: ilustrativo -> mejorar valores iniciales    

 
    def actualizar_vector_pesos(vector_d_siguiente):
        #actualizar pesos según la diferencia entre salida deseada y obtenida 
        # el vector_d es el vector de error proviene de la capa siguiente segun backpropagation
        # usar vector_w y vector_d para calcular el error_d en la neurona
        # desupués usar error_d para actualizar pesos 
        pass


