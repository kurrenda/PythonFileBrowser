import os
from tkinter import *



class Functions():

    def __init__(self):

        self.current_path = os.getcwd()

    def get_path(self, listbox):

        self.listbox = listbox

        for parent,dirs,files in os.walk(self.current_path):

            self.listbox.insert(END,"..")

            for dirname in dirs:
                self.listbox.insert(END,dirname)
            for filename in files:
                self.listbox.insert(END,filename)

            break
