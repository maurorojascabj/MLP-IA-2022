def guardar_errores(archivo, epoca, mse, error_validacion):
    with open(archivo, mode="a") as file:
        file.write(str(epoca)+",")
        file.write(str(mse)+",")
        file.write(str(error_validacion)+";")

def guardar_exactitud(archivo, exactitud):
    with open(archivo, mode="a") as file:
        file.write("\n"+str(exactitud))

def guardar_precision(archivo, precision):
    with open(archivo, mode="a") as file:
        file.write("\n"+str(precision[0])+","+str(precision[1])+","+str(precision[2]))

def leer_archivo_errores(archivo):
    matriz_errores=[]
    exactitud_entrenamiento=0
    exactitud_validacion=0
    exactitud_test=0
    precision_test=[]
    with open(archivo, mode="r") as file:
        for indice,linea in enumerate(file):
            renglon=linea.split()
            if(indice==0):  #primer linea del archivo corresponde a los errores de entrenamiento y validacion obtenidos por epoca
                separar_epocas=renglon[0].split(";")
                separar_epocas.pop()
                for i in range(len(separar_epocas)):
                    separar_errores=separar_epocas[i].split(",")
                    convertir_errores =[float(x) for x in separar_errores]
                    matriz_errores.append(convertir_errores)
            
            elif(indice==1):
                exactitud_entrenamiento=float(renglon[0])
            elif(indice==2):
                exactitud_validacion=float(renglon[0])
            elif(indice==3):
                exactitud_test=float(renglon[0])
            else:
                precision_por_letra=renglon[0].split(",")
                convertir_precision=[float(x) for x in precision_por_letra]
                for j in range(len(convertir_precision)):
                    precision_test.append(convertir_precision[j])
       # print(precision_test)

    return matriz_errores, exactitud_entrenamiento, exactitud_validacion,exactitud_test, precision_test



archivo_errores="archivos_errores\errores_caso_1000_22.txt"
matriz_errores, exact_entrenamiento, exact_validacion, exact_test, precision=leer_archivo_errores(archivo_errores)

#print(matriz_errores)
print("exactitudes:"+ str(exact_entrenamiento)+" "+str(exact_validacion)+" "+str(exact_test))
print("precision test:"+str(precision[0])+" "+str(precision[1])+" "+str(precision[2]))


        