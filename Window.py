from tkinter import *
from UI.Text import *
from UI.FrameUI import *
from UI.Pattern import *
from UI.SelectMultiple import *


from Styles import *

class Window(tkinter.Tk):

    def __init__(self, matrizB, matrizC, matrizF) -> None:
        super().__init__()
        self.windowTitle = self.title("Perceptrón Multicapa - Inteligencia Artificial 2022")
        self.windowGeometry = self.geometry("1250x750")
        self.windowResizable = self.resizable(0,0)
    
        #Título principal
        self.mainTitle = Text("Perceptron Multicapa")
        self.mainTitle.createUI(self, ("Arial Bold", 30))
        self.mainTitle.setLocation(titleStyles["coordenadasX"], titleStyles["coordenadasY"])

        #Radiobuttons
        radioValue = tkinter.IntVar()
        self.radioButton1 = Radiobutton(self, text='Opción A', value=1, variable=radioValue)
        self.radioButton2 = Radiobutton(self, text='Opción B', value=2, variable=radioValue)
        self.radioButton3 = Radiobutton(self, text='Opción C', value=3, variable=radioValue)
        self.radioButton1.place(x=radioButtonBStyles["coordenadasX"], y=radioButtonBStyles["coordenadasY"])
        self.radioButton2.place(x=radioButtonDStyles["coordenadasX"], y=radioButtonDStyles["coordenadasY"])
        self.radioButton3.place(x=radioButtonFStyles["coordenadasX"], y=radioButtonFStyles["coordenadasY"])

        #Frames
        self.frameB = FrameUI(self)
        self.frameD = FrameUI(self)
        self.frameF = FrameUI(self)
        self.frameB.setLocation(frameStyles["positionInitialX"], frameStyles["positionInitialY"])
        self.frameD.setLocation(frameDStyles["coordenadasX"], frameDStyles["coordenadasY"])
        self.frameF.setLocation(frameFStyles["coordenadasX"], frameFStyles["coordenadasY"])

        #Patterns
        self.patternB = self.patternD = self.patternF = Pattern()

        self.patternB.drawPattern(self.frameB, cellStyles["bgCell"], matrizB)
        self.patternD.drawPattern(self.frameD, cellStyles["bgCell"], matrizC)
        self.patternF.drawPattern(self.frameF, cellStyles["bgCell"], matrizF)

        #Button
        self.buttonMain = Button(self, text="Guardar elección", command=onClick)
        self.buttonMain.configure(width=99)
        self.buttonMain.place(x=buttonMainStyles["coordenadasX"], y=buttonMainStyles["coordenadasY"])

        #text distorsion
        self.textDistorsion = Text("Seleccione el porcentaje de distorsión:")
        self.textDistorsion.createUI(self)

        #combobox
        self.comboBox = SelectMultiple(self)
        self.comboBox.setValues()
        

        #methods
        def onClick():
            if radioValue.get() == 1 or radioValue.get() == 2 or radioValue.get() == 3:
                matriz = []
                if radioValue.get() == 1:
                    self.frameD.destroy()
                    self.frameF.destroy()
                    matriz = matrizB.copy()
                    self.frameB.setLocation(frameStyles["positionInitialX"], frameStyles["positionInitialY"])
                elif radioValue.get() == 2:
                    self.frameB.destroy()
                    self.frameF.destroy()
                    matriz = matrizC.copy()
                    self.frameD.setLocation(frameStyles["positionInitialX"], frameStyles["positionInitialY"])
                elif radioValue.get() == 3:
                    self.frameB.destroy()
                    self.frameD.destroy()
                    matriz = matrizF.copy()
                    self.frameF.setLocation(frameStyles["positionInitialX"], frameStyles["positionInitialY"])

                textPatronOriginal = Text("Patrón original")
                textPatronOriginal.createUI(self, ("Arial Bold", 15))
                textPatronOriginal.setLocation(textPatronOriginalStyles["coordenadasX"], textPatronOriginalStyles["coordenadasY"])
                
                self.buttonMain.destroy()
                self.radioButton1.destroy()
                self.radioButton2.destroy()
                self.radioButton3.destroy()
                
                self.textDistorsion.setLocation(titleDistorsionStyles["coordenadasX"], titleDistorsionStyles["coordenadasY"])
                
                self.comboBox.setLocation(comboBoxStyles["coordenadasX"], comboBoxStyles["coordenadasY"])

                buttonSaveChoose = Button(self, text="Generar distorsión", command=lambda: generateDistorsion(self.comboBox.getValues(), matriz))
                buttonSaveChoose.configure(width=20)
                buttonSaveChoose.place(x=buttonSaveChooseStyles["coordenadasX"], y=buttonSaveChooseStyles["coordenadasY"])
    
    
