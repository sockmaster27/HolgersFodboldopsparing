import tkinter as tk

from components import style
from components.list import List
from components.menuBar import MenuBar


window = tk.Tk()
window.configure(background=style.BG_COLOR)
window.title("Holgers fodboldtur")

icon = tk.PhotoImage(file="Logo.png")
window.iconphoto(False, icon)

menubar = MenuBar(window)
window.config(menu=menubar)

listbox = List(window)
listbox.pack()

window.mainloop()
