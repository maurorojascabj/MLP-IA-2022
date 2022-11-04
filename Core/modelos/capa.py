from Core.enums.Tipo_de_capa import Tipo_de_capa
from Core.modelos.neurona import Neurona
import numpy as np

class Capa():
    def __init__ (self , cant_neuronas,  func_transferencia, capa_anterior, capa_siguiente, tipo, coef_aprendizaje, term_momento, matriz_w = None):
        self._func_transferencia = func_transferencia 
        self._coef_aprendizaje = coef_aprendizaje
        self._term_momento = term_momento 

        self.capa_anterior = capa_anterior
        self.capa_siguiente = capa_siguiente
        self.cant_neuronas = cant_neuronas
        self.tipo = tipo
        self.errores_capa=[]

        if(matriz_w != None):
            self.matriz_w =  matriz_w 
        else:    
            self.matriz_w =[]

        if (self.matriz_w == [] and self.tipo != Tipo_de_capa.entrada):
            #self.matriz_w = np.round(np.random.randn(self.cant_neuronas , capa_anterior.cant_neuronas + 1),3) #en pos 0 va el umbral 
            for i in range(self.cant_neuronas):
                for j in range(capa_anterior.cant_neuronas + 1):
                    self.matriz_w.append([])
                    self.matriz_w[i].append(np.round(np.random.uniform(-1.0, 1.0),3)         )
            print(self.matriz_w)
             
        
        
        self.neuronas = []
        if(self.tipo == Tipo_de_capa.entrada):
            for i in range(cant_neuronas):
                nueva_neurona = Neurona(self._func_transferencia, 0, self._coef_aprendizaje, self._term_momento,  [0])
                self.neuronas.append(nueva_neurona)
        else:    
            for i in range(cant_neuronas):
                nueva_neurona = Neurona(self._func_transferencia, self.capa_anterior.cant_neuronas, self._coef_aprendizaje, self._term_momento, self.matriz_w[i])
                self.neuronas.append(nueva_neurona)
                #for each neurona de la capa anterior voy acumulando Net
                #despues asigno la acumulacion a nueva_neurona.net


    def actualizar_pesos (self):
        self.matriz_w = []
        for i in range(len(self.neuronas)):            
            self.neuronas[i].actualizar_vector_pesos()        
            self.matriz_w.append(self.neuronas[i].vector_w) 
        
                

        # if(self.tipo != Tipo_de_capa.salida):
        #     matrices_w_actualizada_red.append(self.capa_siguiente.actualizar_pesos()) 
        #     return  matrices_w_actualizada_red.append(self.matriz_w) 
        # else:
        return  self.matriz_w     



    def calcular_error(self, salida_deseada, errores_capa_posterior = None):
        errores_capa=[]
        #para capa de salida
        if(self.tipo == Tipo_de_capa.salida):
            i=0
            for neurona in self.neuronas:
                salida_deseada_i = salida_deseada[i] 
                error_neurona_i = neurona.calcular_error_en_capa_salida( salida_deseada_i)
                errores_capa.append(error_neurona_i) 
                i+=1
        else:
            i=0
            for neurnona in self.neuronas:
                vector_pesos_capa_posterior= self.neurona_i_pesos_a_capa_posterior( i + 1 )
                error_neurona_i = neurnona.calcular_error_en_capa_oculta(vector_pesos_capa_posterior, errores_capa_posterior)
                errores_capa.append(error_neurona_i)
                i+=1       

        self.errores_capa = errores_capa
        
        return self.errores_capa
        # if (self.capa_anterior != Tipo_de_capa.entrada):
        #     self.capa_anterior.calcular_error(None, self.errores_capa) #se propaga hacia atras
        # else:  
        #     return   
            #matriz_w_actualizada_red = self.actualizar_pesos()  # cuando es capa de entrada dejo de propagar errores    


    def neurona_i_pesos_a_capa_posterior(self, pos_neurona ):
        vector_pesos = []
        for neurona in self.capa_siguiente.neuronas:
            vector_pesos.append(neurona.vector_w[pos_neurona])
        return vector_pesos    

 

    def entrenar_patron (self, vector_entradas): #estamos trabajando con 1 renglon del archivo = 1 patron de entrada
        salida_de_la_capa = [] 

        if(self.tipo  != Tipo_de_capa.entrada):
            for neurona in self.neuronas:
                salida_de_la_capa.append(neurona.calcular_salida(vector_entradas))
        else:           
            for i in range(len(vector_entradas)): # cuando es capa de entrada, este vector tiene 100 y a cada neurona sólo le interesa 1
                entrada_neurona_de_entrada = []
                entrada_neurona_de_entrada.append(vector_entradas[i])
                salida_de_la_capa.append(self.neuronas[i].calcular_salida([vector_entradas[i]]))    

        # una vez que tengo todas las salidas de la capa
        if self.tipo  != Tipo_de_capa.salida:
            salida_red = self.capa_siguiente.entrenar_patron(salida_de_la_capa)   
            return salida_red
        else:
            return salida_de_la_capa
            #calcular error del patron    
            #self.calcular_error(salida_deseada)
            #calcular error global - una variable de la red
         # es la salida de la capa de salida vector largo 3
        


