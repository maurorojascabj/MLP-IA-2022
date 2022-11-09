import tkinter as tkinter
from Styles import *
from UI.FrameUI import *
from UI.Pattern import *
from UI.SelectMultiple import *
from UI.Text import *
from utils import *

patterns = {
    "patternB": {
        "coordenadaX":[1,2,3,4,5,6,7,8,4,4,4,4,8,8,8,8,5,6,7],
        "coordenadaY":[2,2,2,2,2,2,2,2,3,4,5,6,3,4,5,6,7,7,7]
    },
    "patternD": {
        "coordenadaX":[1,2,3,4,5,6,7,8,4,4,4,4,8,8,8,8,5,6,7],
        "coordenadaY":[7,7,7,7,7,7,7,7,3,4,5,6,3,4,5,6,2,2,2]
    },
    "patternF":{
        "coordenadaX":[2,3,4,5,6,7,8,4,4,4,4,4,1,1,2],
        "coordenadaY":[4,4,4,4,4,4,4,2,3,4,5,6,5,6,7]
    }
}
matrizB="0000000000 0010000000 0010000000 0010000000 0011111000 0010000100 0010000100 0010000100 0011111000 0000000000"
matrizC="0000000000 0000000100 0000000100 0000000100 0001111100 0010000100 0010000100 0010000100 0001111100 0000000000"
matrizF="0000000000 0000011000 0000100100 0000100000 0011111000 0000100000 0000100000 0000100000 0000100000 0000000000"
matrizB=matrizStringToArrayInt(matrizB).copy()
matrizC=matrizStringToArrayInt(matrizC).copy()
matrizF=matrizStringToArrayInt(matrizF).copy()

class Resultado():
    def __init__(self, window, patronSeleccionado, distorsion):
        super().__init__()
        self.window = window

        valorDistorsion = distorsion[:-1] #Elimino el caracter %
        valorDistorsion = int(valorDistorsion)
        print("valorD: " + str(valorDistorsion))
        print("patronSeleccionado: " + str(patronSeleccionado))

        self.frameContenedor = FrameUI(window, 0)
        self.frameContenedor.setLocation(200, 100)
        self.frameContenedor.config(width=1100, height=700)

        self.textPatronOriginal = Text("Patrón original")
        self.textPatronOriginal.createUI(self.frameContenedor, ("Arial Bold", 15))
        self.textPatronOriginal.setLocation(titlePatronSeleccionadoStyles["coordenadaX"], titlePatronSeleccionadoStyles["coordenadaY"])

        self.frameSeleccionado = FrameUI(self.frameContenedor)
        self.frameSeleccionado.setLocation(frameSeleccionado["coordenadaX"], frameSeleccionado["coordenadaY"])
        self.patternSeleccionado = Pattern()

        self.textPatronDistorsionado = Text("Patrón distorsionado")
        self.textPatronDistorsionado.createUI(self.frameContenedor, ("Arial Bold", 15))
        self.textPatronDistorsionado.setLocation(titlePatronDistorsionadoStyles["coordenadaX"], titlePatronDistorsionadoStyles["coordenadaY"])
        
        self.frameDistorsionado = FrameUI(self.frameContenedor)
        self.frameDistorsionado.setLocation(frameDistorsionado["coordenadaX"], frameDistorsionado["coordenadaY"])
        self.patternDistorsionado = Pattern()
        ##Generamos la distorsion
        newMatriz = []
        if(patronSeleccionado == 1):
            self.patternSeleccionado.drawPattern(self.frameSeleccionado, cellStyles["bgCell"], matrizB)
            newMatriz = matrizB.copy()
            newMatriz = self.setDistorsion(newMatriz, valorDistorsion) #matriz B, valor 10
        elif(patronSeleccionado == 2):
            self.patternSeleccionado.drawPattern(self.frameSeleccionado, cellStyles["bgCell"], matrizC)
            newMatriz = matrizC.copy()
            newMatriz = self.setDistorsion(newMatriz, valorDistorsion)
        elif(patronSeleccionado == 3):
            self.patternSeleccionado.drawPattern(self.frameSeleccionado, cellStyles["bgCell"], matrizF)
            newMatriz = matrizF.copy()
            newMatriz = self.setDistorsion(newMatriz, valorDistorsion)

        self.patternDistorsionado.drawPattern(self.frameDistorsionado, cellStyles["bgCell"], newMatriz)     

    def setDistorsion(self, matriz, repetitions):
        newMatriz = matriz.copy()
        for x in range(repetitions):
            position = generateRandom(0,99)
            for y in range(len(newMatriz)):
                if y == position:
                    if newMatriz[y] == 0:
                        newMatriz[y] = 1
                    else:
                        newMatriz[y] = 0
        return newMatriz