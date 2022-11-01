def obtener_pesos(archivo):
    matrices_w=[]
    lineas=[]
    pesos=[]
    with open(archivo, mode="r") as archivo:
        contenido=archivo.read()
        separar_matrices=contenido.split(";")
        for i in range(len(separar_matrices)):
            separar_lineas=separar_matrices[i].split(",")
            for j in range(len(separar_lineas)):
                separar_pesos=separar_lineas[j].split(" ")
                for k in range(len(separar_pesos)):
                    pesos.append(float(separar_pesos[k]))
                lineas.append(pesos)
            matrices_w.append(lineas)
    return matrices_w
    #print(matrices_w)
                
            



def guardar_pesos(archivo, matrices_w):
    with open(archivo, mode="a") as file:
        for i in range(len(matrices_w)):
            matriz=matrices_w[i]
            for j in range(len(matriz)):
                linea=matriz[j]
                for k in range(len(linea)):
                    w=str(linea[k])
                    file.write(w)
                    if(k!=(len(linea)-1)):
                        file.write(" ")
                if(j!=(len(matriz)-1)):
                    file.write(",")
            if(i!=(len(matrices_w)-1)):
                file.write(";")
