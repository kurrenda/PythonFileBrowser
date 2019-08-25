from tkinter import *
from interface import Gui
from functions import Functions
import os

window = Tk()

func = Functions()
default_path = os.getcwd()
interface = Gui(window,default_path, func)

func.get_path(interface.listbox)


window.mainloop()

