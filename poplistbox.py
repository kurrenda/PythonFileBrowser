import tkinter
import os


class PopListBox(tkinter.Listbox):

    def __init__(self, parent, interface, *args, **kwargs):

        tkinter.Listbox.__init__(self,parent,*args, **kwargs)
        self.interface = interface
        self.interface.listbox.bind("<Button-3>", self.popup)
        self.popup_menu = tkinter.Menu(self, tearoff = 0)
        self.popup_menu.add_command(label="Delete", command=lambda: self.delete_file(self.interface.listbox))
        self.popup_menu.add_command(label="Select All")

        self.interface.listbox.bind("<Button-3>", self.popup)


    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()


    def delete_file(self, listbox):
        self.selectfile = self.interface.func.item_select(listbox)
        temp_path = self.interface.func.path()
        current_path = f'{temp_path}\{self.selectfile}'
        os.remove(current_path)
        self.interface.func.refresh_listbox(listbox)