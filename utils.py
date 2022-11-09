import random

def matrizStringToArrayInt(matriz):
    array = matriz.split()
    arrayFinal = []
    for x in range(len(array)):
        array2 = list(array[x])
        for y in range(len(array2)):
            arrayFinal.append(int(array2[y]))
    return arrayFinal

def generateRandom(init, final):
    return random.randint(init, final)

def destroyElement(element):
    element.destroy()