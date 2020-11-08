import tkinter as tk
from tkinter import messagebox

import time

import fodboldtur


def stop():
    tk.messagebox.showerror("Stop", "Hvorfor?")


class MenuBar(tk.Menu):
    def __init__(self, master):
        self.window = master

        tk.Menu.__init__(self, master)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save)

        edit_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Her er ikke noget, jeg syntes bare her så lidt tomt ud...", command=stop)

    def save(self):
        fodboldtur.save()

        # lidt placebo så man kan vide at det virker
        self.window.config(cursor="wait")
        self.window.after(500, lambda: self.window.config(cursor=""))
