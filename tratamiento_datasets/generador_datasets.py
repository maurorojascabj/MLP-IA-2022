import random

def diferenciaEntrePatrones(patron,patronDistorsionado):  #para ver si se distorsiona correctamente en las posiciones correspondientes
    lista2=list()
    j=0
    while j < len(patron):
        if(patron[j]!=patronDistorsionado[j]):
            lista2.append(j+1)
        j+=1
    return lista2

def posicYaDistors(posicADistorsionar,lista):  #se recorre lista de posiciones distorsionadas para ver si la nueva posicion ya esta distorsionada
    for l in lista:
        if(l==posicADistorsionar):
            return True
    return False

def reemplazarCaracter(patron, posicion):
    posicion-=1 #para ir de 1 a 100 en lugar de 0 a 99
   # nuevaPosic=posicion+ (posicion//10)  # posicion aleatoria a distorsionar considerando espacios en blanco del patron
    if (patron[posicion]=="0"):
        cadena= patron[:posicion]+"1"+patron[posicion+1:]  #se reemplaza el caracter 0 por 1 
    else:
        cadena= patron[:posicion]+"0"+patron[posicion+1:]  #se reemplaza el caracter 1 por 0
    return cadena

def distorsionarEjemplo(patron, porcMin, porcMax):
    j=0
    nuevoPatron=patron
    distorsiones=list()  #lista que contiene posiciones ya distorsionadas (para no distorsionar una misma posicion varias veces) 
    porcDistorsion=random.randint(porcMin, porcMax)  #porcentaje de distorsion del ejemplo
    
    while j < porcDistorsion:
        posicADistorsionar=random.randint(1,100)
        while posicYaDistors(posicADistorsionar,distorsiones): #si la posicion random obtenida ya esta distorsionada, se busca otra posicion para distorsionar
            posicADistorsionar=random.randint(1,100)
        nuevoPatron=reemplazarCaracter(nuevoPatron,posicADistorsionar)
        distorsiones.append(posicADistorsionar)
        distorsiones.sort()
        j+=1
   # print("posic"+str(porcDistorsion))
    #print(distorsiones)
    distorsiones.clear()
    if(len(str(porcDistorsion))==2):
        nuevoPatron=nuevoPatron + " " + str(porcDistorsion)
    else:
        nuevoPatron=nuevoPatron + " 0" + str(porcDistorsion)    
    return nuevoPatron


def generarDataset(archivo,total):
    patronB="0000000000001000000000100000000010000000001111100000100001000010000100001000010000111110000000000000"
    patronD="0000000000000000010000000001000000000100000111110000100001000010000100001000010000011111000000000000"
    patronF="0000000000000001100000001001000000100000001111100000001000000000100000000010000000001000000000000000"
    cantNoDistors=total // 10    # 10 % de ejemplos no deben tener distorsion
    cantPorLetraNoDistors=cantNoDistors//3  #cantidad de ejemplos no distorsionados por letra
    cantPorLetraDistors=(total-cantNoDistors)//3  #cantidad de ejemplos distorsionados por letra


    i=0
    with open(archivo, mode="w") as file1:
        #escribir ejemplos sin distorsion
        while i < cantPorLetraNoDistors:
            file1.write(patronB+" 00 100\n")
            file1.write(patronD+" 00 010\n")
            file1.write(patronF+" 00 001\n")
            i+=1

        i=0
        while i < (cantNoDistors-cantPorLetraNoDistors*3):
            file1.write(patronF+" 00 001\n")
            i+=1
            

        #escribir ejemplos con distorsion
        i=0
        while i < (cantPorLetraDistors//3):
            file1.write(distorsionarEjemplo(patronB,1,10)+" 100 " +"\n")
            file1.write(distorsionarEjemplo(patronD,1,10)+" 010 " +"\n")
            file1.write(distorsionarEjemplo(patronF,1,10)+" 001 " +"\n")

            file1.write(distorsionarEjemplo(patronB,11,20)+" 100 " +"\n")
            file1.write(distorsionarEjemplo(patronD,11,20)+" 010 " +"\n")          
            file1.write(distorsionarEjemplo(patronF,11,20)+" 001 " +"\n")

            file1.write(distorsionarEjemplo(patronB,21,30)+" 100 " +"\n")          
            file1.write(distorsionarEjemplo(patronD,21,30)+" 010 " +"\n")
            file1.write(distorsionarEjemplo(patronF,21,30)+" 001 " +"\n")

            i+=1

 
nDataset=500
archivo="tratamiento_datasets\dataset500.txt"
generarDataset(archivo, nDataset)

 