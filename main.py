import tkinter as tkinter

window = tkinter.Tk()

widthCell = 2
heightCell = 1
bgCell = "#1E90FF"


for x in range(10):#Filas
    for y in range(10):#Columnas
        framegrid = tkinter.Frame(
            master=window,
            relief=tkinter.SUNKEN,
            borderwidth=1,
            width=385, height=460
        )
        framegrid.grid(row=x, column=y, padx=1, pady=2)
        labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell)
        if y == 2 and x in range(1, 9):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        if x == 4 and y in range(3, 7):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        if x == 8 and y in range(3, 7):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        if y == 7 and x in range(5, 8):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        # labelgrid.pack(padx=10, pady=10)
        labelgrid.grid(row=1, column=10, sticky="nsew")
for x in range(10):#Filas
    for y in range(10):#Columnas
        framegrid = tkinter.Frame(
            master=window,
            relief=tkinter.SUNKEN,
            borderwidth=1,
            width=385, height=460
        )
        framegrid.grid(row=x, column=y+10, padx=1, pady=2)
        labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell)
        if y == 7 and x in range(1, 9):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        if x == 4 and y in range(3, 7):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        if x == 8 and y in range(3, 7):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        if y == 2 and x in range(5, 8):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        # labelgrid.pack(padx=10, pady=10)
        labelgrid.grid(row=1, column=10, sticky="nsew")
for x in range(10):#Filas
    for y in range(10):#Columnas
        framegrid = tkinter.Frame(
            master=window,
            relief=tkinter.SUNKEN,
            borderwidth=1,
            width=385, height=460
        )
        framegrid.grid(row=x, column=y+20, padx=1, pady=2)
        labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell)
        if y == 4 and x in range(2, 9):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        if x == 4 and y in range(2, 7):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        if x == 1 and y in range(5, 7):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        if y == 7 and x in range(2, 3):
            labelgrid = tkinter.Label(master=framegrid, width=widthCell, height=heightCell, bg=bgCell)
        # labelgrid.pack(padx=10, pady=10)
        labelgrid.grid(row=1, column=10, sticky="nsew")
window.geometry("1000x500")
window.mainloop()