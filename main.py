from tkinter import *
from interface import Gui
from functions import Functions


window = Tk()

func = Functions()
interface = Gui(window, func)

func.get_path(interface.listbox)


window.mainloop()

