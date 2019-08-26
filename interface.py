from tkinter import *

class Gui():

    def __init__(self, window, func):

        self.func = func

        self.window = window
        self.window.title("PythonFileBrowser")
        self.window.geometry('950x500')

        self.default_path = self.func.current_path

        self.menu = Menu(self.window)
        self.window.config(menu=self.menu)

        self.cascade = Menu(self.menu,tearoff=0)
        self.menu.add_cascade(label="Program", menu=self.cascade)
        self.cascade.add_command(label="opcja 1")

        self.path_frame = Frame(self.window)
        self.path_frame.grid(row=0, column=0, sticky=W+E)

        self.label_path = Label(self.path_frame, text="Path: ")
        self.label_path.grid(row=0, column = 0, padx=(10), pady =(10))

        self.entry = Entry(self.path_frame, text="", width=130)
        self.entry.grid(row=0, column= 1, padx=(10), pady =(10))
        self.entry.insert(0,self.default_path)

        self.button = Button(self.path_frame, text="Wyszukaj")
        self.button.grid(row=0, column= 3, padx=(10), pady =(10))

        self.listbox = Listbox(self.window, width = 154, height = 27)
        self.listbox.grid(row=1, column=0,  padx=10, pady=10)
        self.listbox.bind('<Double-Button-1>', lambda _: self.func.double_click(self.listbox, self.entry))


    def cursorSelection(self):

        self.clicked = self.listbox.curselection()
        print(self.clicked)
