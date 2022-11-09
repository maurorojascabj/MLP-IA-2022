import tkinter as tkinter
from tkinter import Radiobutton, Button
from Styles import *
from UI.FrameUI import *
from UI.Pattern import *
from UI.SelectMultiple import *
from UI.Text import *
from Screens.Resultado import *
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

class SeleccionPatron():
    def __init__(self, window):
        super().__init__()
        self.window = window

        self.frameContenedor = FrameUI(window, 0)
        self.frameContenedor.setLocation(100, 100)
        self.frameContenedor.config(width=1100, height=700)

        self.textPrincipalSeleccionPatron = Text("¿Qué patrón desea clasificar?")
        self.textPrincipalSeleccionPatron.createUI(self.frameContenedor, ("Arial Bold", 15))
        self.textPrincipalSeleccionPatron.setLocation(textPrincipalSeleccionPatronStyles["coordenadaX"], textPrincipalSeleccionPatronStyles["coordenadaY"])

        radioValue = tkinter.IntVar()
        self.rad1 = Radiobutton(self.frameContenedor, text='Opción A', value=1, variable=radioValue)
        self.rad2 = Radiobutton(self.frameContenedor, text='Opción B', value=2, variable=radioValue)
        self.rad3 = Radiobutton(self.frameContenedor, text='Opción C', value=3, variable=radioValue)
        self.rad1.place(x=radioButtonBStyles["coordenadaX"], y=radioButtonBStyles["coordenadaY"])
        self.rad2.place(x=radioButtonDStyles["coordenadaX"], y=radioButtonDStyles["coordenadaY"])
        self.rad3.place(x=radioButtonFStyles["coordenadaX"], y=radioButtonFStyles["coordenadaY"])

        self.frameB = FrameUI(self.frameContenedor)
        self.frameD = FrameUI(self.frameContenedor)
        self.frameF = FrameUI(self.frameContenedor)
        self.frameB.setLocation(frameStyles["positionInitialX"], frameStyles["positionInitialY"])
        self.frameD.setLocation(frameDStyles["coordenadaX"], frameDStyles["coordenadaY"])
        self.frameF.setLocation(frameFStyles["coordenadaX"], frameFStyles["coordenadaY"])

        patternB = patternD = patternF = Pattern()

        patternB.drawPattern(self.frameB, cellStyles["bgCell"], matrizB)
        patternD.drawPattern(self.frameD, cellStyles["bgCell"], matrizC)
        patternF.drawPattern(self.frameF, cellStyles["bgCell"], matrizF)

        self.textDistorsion = Text("¿Qué distorsión desea agregar?")
        self.textDistorsion.createUI(self.frameContenedor, ("Arial Bold", 15))
        self.textDistorsion.setLocation(textDistorsionStyles["coordenadaX"], textDistorsionStyles["coordenadaY"])

        self.comboBoxDistorsion = SelectMultiple(self.frameContenedor)
        self.comboBoxDistorsion.setWidth(40)
        self.comboBoxDistorsion.setValues()
        self.comboBoxDistorsion.setLocation(comboBoxDistorsionStyles["coordenadaX"], comboBoxDistorsionStyles["coordenadaY"])

        self.botonGenerarRed = Button(self.frameContenedor, text="Guardar elección", command=lambda: self.redirectPantalla(radioValue.get(), self.comboBoxDistorsion.getValues()))
        self.botonGenerarRed.configure(width=botonGenerarRedStyles["width"], bg=botonGenerarRedStyles["bg"])
        self.botonGenerarRed.place(x=botonGenerarRedStyles["coordenadaX"], y=botonGenerarRedStyles["coordenadaY"])
    
    def redirectPantalla(self, patron, distorsion):
        if(patron in [1, 2, 3]):
            self.frameContenedor.destroy()
            resultado = Resultado(self.window, patron, distorsion)