#matriz de pesos W
#se inicializa con valores aleatorioss

porcTesting=0.2
porcValidacion=0.1
porcEntrenam=0.7


with open("c:/Users/USER/Documents/ISI 5TO/INTELIGENCIA ARTIFICIAL/TPI/dataset1000.txt", mode="r") as archivo:
    for linea in archivo:
        linea1=linea.split()
        print(linea1)

