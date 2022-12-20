import tkinter as tkinter
from tkinter import Button
from Styles import *
from UI.FrameUI import *
from UI.Pattern import *
from UI.SelectMultiple import *
from UI.Text import *
from utils import *
from tktooltip import ToolTip

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
    def __init__(self, window, patronSeleccionado, distorsion, red, pantallaPatron = None):
        super().__init__()
        self.window = window
        self.red = red
        self.pantallaPatron = pantallaPatron

        valorDistorsion = distorsion[:-1] #Elimino el caracter %
        valorDistorsion = int(valorDistorsion)

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
        
        self.getClassPatron = Button(self.frameContenedor, text="Clasificar patrón", command=lambda: self.clasificar(newMatriz))
        self.getClassPatron.configure(width=botonGetClassPatronStyles["width"], height=botonGetClassPatronStyles["height"], bg=botonGetClassPatronStyles["bg"], font=("Arial Bold", 12))
        self.getClassPatron.place(x=botonGetClassPatronStyles["coordenadaX"], y=botonGetClassPatronStyles["coordenadaY"])
        ToolTip(self.getClassPatron, msg="Obtener letra a la que corresponde el patrón de acuerdo al modelo", follow=True, delay=0.5)

        self.botonVolver = Button(self.frameContenedor, text="Volver", command=lambda: self.redirectPantalla())
        self.botonVolver.configure(bg=botonGetClassPatronStyles["bg"], font=("Arial Bold", 12))
        self.botonVolver.place(x=200, y=400)

        self.textResultado = Text("Letra obtenida")
        self.textResultado.createUI(self.frameContenedor, ("Arial Bold", 15))
        self.textResultado.setLocation(textResultadoStyles["coordenadaX"], textResultadoStyles["coordenadaY"])
        
        self.frameResultado = FrameUI(self.frameContenedor, 0)
        self.frameResultado.setLocation(900, 120)
        self.frameResultado.config(width=200, height=210, highlightbackground='white', highlightthickness=2)



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
    
    def clasificar(self, matriz):
        patronClasificado, probabilidadSalida = self.red.clasificar_patron_maxarg(matriz)
        letra = ''
        if patronClasificado == [0,1,0]:
            letra = 'd'
        elif patronClasificado == [1,0,0]:
            letra = 'b'
        elif patronClasificado == [0,0,1]:
            letra = 'f'
        
        self.textResultadoObtenido = Text(letra)
        self.textResultadoObtenido.createUI(self.frameResultado, ("Arial Bold", 100))
        self.textResultadoObtenido.setLocation(textResultadoObtenidoStyles["coordenadaX"], textResultadoObtenidoStyles["coordenadaY"])


        self.textProbab = Text("Probabilidad de que el Patrón sea:")
        self.textProbab.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textProbab.setLocation(220,480)

        self.textB = Text("● Letra B:")
        self.textB.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textB.setLocation(250,515)

        self.textProbB = Text(probabilidadSalida[0])
        self.textProbB.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textProbB.setLocation(330,515)

        self.textPorcB = Text("%")
        self.textPorcB.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textPorcB.setLocation(375,515)

        self.textB = Text("● Letra D:")
        self.textB.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textB.setLocation(250,545)

        self.textProbB = Text(probabilidadSalida[1])
        self.textProbB.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textProbB.setLocation(330,545)

        self.textPorcB = Text("%")
        self.textPorcB.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textPorcB.setLocation(375,545)

        self.textB = Text("● Letra F:")
        self.textB.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textB.setLocation(250,575)

        self.textProbB = Text(probabilidadSalida[2])
        self.textProbB.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textProbB.setLocation(330,575)

        self.textPorcB = Text("%")
        self.textPorcB.createUI(self.frameContenedor, ("Arial Bold", 12))
        self.textPorcB.setLocation(375,575)
    def redirectPantalla(self):
        self.frameContenedor.hideFrame()
        self.pantallaPatron.setLocation(100, 100)
        self.pantallaPatron.config(width=1100, height=700)
