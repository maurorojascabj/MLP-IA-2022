from tkinter import Menu

class Menu(Menu):

    def __init__(self, window) -> None:
        Menu.__init__(self)
        self.menuBar = Menu(window)
