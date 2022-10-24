from random import random


class Neurona():
    def __init__(self, funcion_activacion, cant_neuronas_capa_anterior):
        self._funcion_activacion = funcion_activacion
        self.vector_w = [] #vector de n pesos asociados a las n entradas (de capa anterior) de la neurona
        self.inicializar_pesos(cant_neuronas_capa_anterior)
        self.umbral_w_0 = 0
        
        self.valor_estado_activacion
        

    #Yn
    def calcular_salida(self, vector_valores_entrada):
        pass

    #a(t)n
    def calcular_estado_activacion():
        pass

    #Netn    
    def calcular_entrada_total():
        pass

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


