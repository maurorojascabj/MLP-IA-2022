import tkinter as tkinter
from UI.Cell import *
from Styles import cellStyles

class Pattern:

    # def drawPattern(self, frame, amountRow, amountColumn, coordenadasX, coordenadasY, colorCell, matriz):
    def drawPattern(self, frame, colorCell, matriz):
        # array = matriz.split()
        # arrayFinal = []
        # for x in range(len(array)):
        #     array2 = list(array[x])
        #     for y in range(len(array2)):
        #         arrayFinal.append(int(array2[y]))
        for x in range(len(matriz)):
            if (matriz[x] == 0):
                cell = Cell(frame, cellStyles["widthCell"], cellStyles["heightCell"])
                cell.setLocation(x//10, x%10)
            else:
                cell = Cell(frame, cellStyles["widthCell"], cellStyles["heightCell"], colorCell)
                cell.setLocation(x//10, x%10)

        # for x in range(amountRow):
        #     for y in range(amountColumn):
        #         cell = Cell(frame, cellStyles["widthCell"], cellStyles["heightCell"])
        #         cell.setLocation(x, y)
        # for idx in range(len(coordenadasX)):
        #     cell = Cell(frame, cellStyles["widthCell"], cellStyles["heightCell"], colorCell)
        #     cell.setLocation(coordenadasX[idx], coordenadasY[idx])