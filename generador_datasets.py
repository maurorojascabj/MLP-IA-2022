import random

def diferenciaEntrePatrones(patron,patronDistorsionado):  #para ver si se distorsiona correctamente en las posiciones correspondientes
    lista2=list()
    j=0
    while j < len(patron):
        if(patron[j]!=patronDistorsionado[j]):
            lista2.append((j+1-(j//10)))
        j+=1
    return lista2

def posicYaDistors(posicADistorsionar,lista):  #se recorre lista de posiciones distorsionadas para ver si la nueva posicion ya esta distorsionada
    for l in lista:
        if(l==posicADistorsionar):
            return True
    return False

def reemplazarCaracter(patron, posicion):
    posicion-=1 #para ir de 1 a 100 en lugar de 0 a 99
    nuevaPosic=posicion+ (posicion//10)  # posicion aleatoria a distorsionar considerando espacios en blanco del patron
    print("posic: "+str(nuevaPosic))
    if (patron[nuevaPosic]=="0"):
        cadena= patron[:nuevaPosic]+"1"+patron[nuevaPosic+1:]  #se reemplaza el caracter 0 por 1 
    else:
        cadena= patron[:nuevaPosic]+"0"+patron[nuevaPosic+1:]  #se reemplaza el caracter 1 por 0
    return cadena

def distorsionarEjemplo(patron, porcMin, porcMax):
    j=0
    nuevoPatron=patron
    distorsiones=list()  #lista que contiene posiciones ya distorsionadas (para no distorsionar una misma posicion varias veces) 
    porcDistorsion=random.randint(porcMin, porcMax)  #porcentaje de distorsion del ejemplo
    print(porcDistorsion)
    while j < porcDistorsion:
        posicADistorsionar=random.randint(1,100)
        while posicYaDistors(posicADistorsionar,distorsiones): #si la posicion random obtenida ya esta distorsionada, se busca otra posicion para distorsionar
            posicADistorsionar=random.randint(1,100)
        nuevoPatron=reemplazarCaracter(nuevoPatron,posicADistorsionar)
        distorsiones.append(posicADistorsionar)
        distorsiones.sort()
        print(distorsiones)
        j+=1
    distorsiones.clear()
    if(len(str(porcDistorsion))==2):
        nuevoPatron=nuevoPatron + " " + str(porcDistorsion)
    else:
        nuevoPatron=nuevoPatron + " 0" + str(porcDistorsion)    
    return nuevoPatron


def generarDataset(archivo,total):
    patronB="0000000000 0010000000 0010000000 0010000000 0011111000 0010000100 0010000100 0010000100 0011111000 0000000000"
    patronC="0000000000 0000000100 0000000100 0000000100 0001111100 0010000100 0010000100 0010000100 0001111100 0000000000"
    patronF="0000000000 0000011000 0000100100 0000100000 0011111000 0000100000 0000100000 0000100000 0000100000 0000000000"
    cantNoDistors=total // 10    # 10 % de ejemplos no deben tener distorsion
    cantPorLetraNoDistors=round(cantNoDistors/3)  #cantidad de ejemplos no distorsionados por letra
    cantPorLetraDistors=(total-cantNoDistors)//3  #cantidad de ejemplos distorsionados por letra


    i=0
    with open(archivo, mode="a") as file1:
        #escribir ejemplos sin distorsion
        while i < cantPorLetraNoDistors:
            file1.write(patronB+" 00 100\n")
            file1.write(patronC+" 00 010\n")
            i+=1

        i=0
        while i < (cantNoDistors-cantPorLetraNoDistors*2):
            file1.write(patronF+" 00 001\n")
            i+=1

        #escribir ejemplos con distorsion
        i=0
        while i < (cantPorLetraDistors//3):
            file1.write(distorsionarEjemplo(patronB,1,10)+" 100 " +"\n")
            file1.write(distorsionarEjemplo(patronC,1,10)+" 010 " +"\n")
            file1.write(distorsionarEjemplo(patronF,1,10)+" 001 " +"\n")

            file1.write(distorsionarEjemplo(patronB,11,20)+" 100 " +"\n")
            file1.write(distorsionarEjemplo(patronC,11,20)+" 010 " +"\n")
            file1.write(distorsionarEjemplo(patronF,11,20)+" 001 " +"\n")

            file1.write(distorsionarEjemplo(patronB,21,30)+" 100 " +"\n")
            file1.write(distorsionarEjemplo(patronC,21,30)+" 010 " +"\n")
            file1.write(distorsionarEjemplo(patronF,21,30)+" 001 " +"\n")

            i+=1

 
nDataset=1000
archivo="c:/Users/USER/Documents/ISI 5TO/INTELIGENCIA ARTIFICIAL/TPI/prueba1.txt"
generarDataset(archivo, nDataset)
 