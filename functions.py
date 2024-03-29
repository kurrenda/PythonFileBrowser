import os
from tkinter import *



class Functions():

    def __init__(self):

        self.current_path = os.getcwd()

    def get_path(self, listbox):

        self.listbox = listbox

        for self.parent, self.dirs, self.files in os.walk(self.current_path):

            self.listbox.insert(END,"..")

            for dirname in self.dirs:
                self.listbox.insert(END,dirname)
            for filename in self.files:
                self.listbox.insert(END,filename)

            break

    def item_select(self, listbox):
        self.listbox = listbox
        item = self.listbox.curselection()[0]
        self.selected_item = self.listbox.get(item)
        return self.selected_item


    def double_click(self, listbox, entry):
        self.item = self.item_select(listbox)
        self.get_path(listbox)
        self.current_path = self.new_path()
        self.refresh_listbox(listbox)
        self.entry = entry
        self.entry_refresh()

    def new_path(self):
        if self.item == "..":

            split = os.path.split(self.current_path)
            self.current_path = split[0]
            return self.current_path

        elif self.item in self.dirs:
            self.current_path = f'{self.current_path}\{self.item}'
            return self.current_path


    def entry_refresh(self):
        self.entry.delete(0,END)
        self.entry.insert(0, self.current_path)


    def path(self):
        return self.current_path

    def refresh_listbox(self, listbox):
        self.listbox = listbox
        self.listbox.delete(0, END)
        self.get_path(listbox)


    def entry_read_search(self,listbox, entry):
        self.entry = entry
        self.entryString = self.entry.get()
        self.current_path = self.entryString
        self.refresh_listbox(listbox)