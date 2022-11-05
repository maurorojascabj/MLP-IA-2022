def obtener_pesos(archivo):
    capas=[]

    with open(archivo, mode="r") as archivo:
        contenido=archivo.read()
        separar_capas=contenido.split(";")
        for i in range(len(separar_capas)):
            separar_neuronas=separar_capas[i].split(",")
            neuronas=[]

            for j in range(len(separar_neuronas)):
                neuronas.append([])
                separar_entradas=separar_neuronas[j].split(" ")
                for k in range(len(separar_entradas)):
                    neuronas[j].append(float(separar_entradas[k]))                    
               
            capas.append(neuronas)
    return capas

            

def guardar_pesos(archivo, matrices_w):
    with open(archivo, mode="a") as file:
        for i in range(len(matrices_w)):
            capa=matrices_w[i]
            for j in range(len(capa)):
                neurona=capa[j]
                for k in range(len(neurona)):
                    entrada=str(neurona[k])
                    file.write(entrada)
                    if(k!=(len(neurona)-1)):
                        file.write(" ")
                if(j!=(len(capa)-1)):
                    file.write(",")
            if(i!=(len(matrices_w)-1)):
                file.write(";")
        file.write("-     aca termina       -")
