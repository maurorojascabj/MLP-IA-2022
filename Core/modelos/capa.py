from Core.enums.Tipo_de_capa import Tipo_de_capa
from Core.modelos.neurona import Neurona
import numpy as np

class Capa():
    def __init__ (self , cant_neuronas,  func_transferencia, capa_anterior, capa_siguiente, tipo, matriz_w = None):
        self._func_transferencia = func_transferencia  

        self.capa_anterior = capa_anterior
        self.capa_siguiente = capa_siguiente
        self.cant_neuronas = cant_neuronas
        self.tipo = tipo
        self.errores_capa=[]

        self.matriz_w = matriz_w  

        if (self.matriz_w == None and self.tipo != Tipo_de_capa.entrada):
            self.matriz_w = np.round(np.random.randn(self.cant_neuronas , capa_anterior.cant_neuronas + 1),3) #en pos 0 va el umbral          
             
        
        
        self.neuronas = []
        if(self.tipo == Tipo_de_capa.entrada):
            for i in range(cant_neuronas):
                nueva_neurona = Neurona(self._func_transferencia, 0, [0])
                self.neuronas.append(nueva_neurona)
        else:    
            for i in range(cant_neuronas):
                nueva_neurona = Neurona(self._func_transferencia, self.capa_anterior.cant_neuronas, self.matriz_w[i-1])
                self.neuronas.append(nueva_neurona)
                #for each neurona de la capa anterior voy acumulando Net
                #despues asigno la acumulacion a nueva_neurona.net





    def calcular_error( self, salida_de_la_capa, salida_deseada, errores_capa_siguiente = None):
        errores_capa=[]
        #para capa de salida
        if(self.tipo == Tipo_de_capa.salida):
            for i in range(len(self.neuronas)):
                salida_deseada_i = salida_deseada[i]
                salida_capa_i = salida_de_la_capa[i]
                error_neurona_i = self.neuronas[i].calcular_error_salida(salida_capa_i, salida_deseada_i)
                errores_capa.append(error_neurona_i)  
        else:
            for i in range(len(self.neuronas)):
                error_neurona_i = self.neuronas[i].calcular_error(errores_capa_siguiente)
                vector_pesos_capa_siguiente = self.neurona_i_pesos_a_capa_siguiente( i + 1 )
                errores_capa.append(error_neurona_i)       

        self.errores_capa = errores_capa
        
        if (self.capa_anterior != Tipo_de_capa.entrada):
            self.capa_anterior.calcular_error(None, None, self.errores_capa) 
        else:    
            self.capa_anterior.actualizar_pesos()     


    def neurona_i_pesos_a_capa_siguiente(self, pos_neurona ):
        vector_pesos = []
        for neurona in self.capa_siguiente.neuronas:
            vector_pesos.append(neurona.vector_w[pos_neurona])





    def entrenar_patron (self, vector_entradas, salida_deseada): #estamos trabajando con 1 renglon
        salida_de_la_capa = [] 

        if(self.tipo  != Tipo_de_capa.entrada):
            for neurona in self.neuronas:
                salida_de_la_capa.append(neurona.calcular_salida(vector_entradas))
        else:           
            for i in range(len(vector_entradas)): # cuando es capa de entrada, este vector tiene 100 y a cada neurona sólo le interesa 1
                entrada_neurona_de_entrada = []
                entrada_neurona_de_entrada.append(vector_entradas[i])
                salida_de_la_capa.append(self.neuronas[i].calcular_salida(vector_entradas[i]))    

        # una vez que tengo todas las salidas de la capa
        if self.tipo  != Tipo_de_capa.salida:
            self.capa_siguiente.entrenar_patron(salida_de_la_capa)   
        else:

            self.calcular_error(salida_de_la_capa, salida_deseada)

            return salida_de_la_capa # es la salida de la capa de salida vector largo 3


