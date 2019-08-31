import tkinter
import os


class PopListBox(tkinter.Listbox):

    def __init__(self, parent, interface, *args, **kwargs):

        tkinter.Listbox.__init__(self,parent,*args, **kwargs)
        self.interface = interface
        self.interface.listbox.bind("<Button-3>", self.popup)

        self.popup_menu = tkinter.Menu(self, tearoff = 0)
        self.popup_menu.add_command(label="Delete", command=lambda: self.delete_file(self.interface.listbox))
        self.popup_menu.add_command(label="Rename", command=lambda: self.popup_enter(self.interface.window, self.interface.listbox))

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
        if os.path.isfile(current_path):
            os.remove(current_path)
        else:
            os.rmdir(current_path)

        self.interface.func.refresh_listbox(listbox)

    def popup_enter(self, window, listbox):
        self.toplevel = tkinter.Toplevel()
        self.toplevel.wm_title("Window")
        self.window = window
        self.listbox = listbox

        screen_width = self.window.winfo_x()
        screen_height = self.window.winfo_y()

        self.toplevel.geometry("%dx%d+%d+%d" % (200, 100, screen_width+350, screen_height+200))

        self.entry = tkinter.Entry(self.toplevel, text="Input")
        self.entry.place(relx=.5, rely=.2, anchor="center")

        self.btn = tkinter.Button(self.toplevel, text="Okay", command=lambda: self.rename_file(self.listbox))
        self.btn.place(relx=.5, rely=.6, anchor="center")

    def rename_file(self, listbox):
        self.selectfile = self.interface.func.item_select(listbox)
        temp_path = self.interface.func.path()
        entryString = self.entry.get()
        current_path = f'{temp_path}\{self.selectfile}'
        new_path =  f'{temp_path}\{entryString}'
        os.rename(current_path, new_path)
        self.toplevel.destroy()
        self.toplevel = None
        self.interface.func.refresh_listbox(listbox)