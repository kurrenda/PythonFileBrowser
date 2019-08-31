from tkinter import *
from interface import Gui
from functions import Functions
from poplistbox import PopListBox

window = Tk()
func = Functions()
interface = Gui(window, func)

poplistbox = PopListBox(window, interface, selectmode = 'multiple')
func.get_path(interface.listbox)


window.mainloop()

