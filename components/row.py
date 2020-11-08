import tkinter as tk
from tkinter import messagebox

import fodboldtur

from components.pixelSized import PixelSized
from components import style


class Row(tk.Frame):
    def __init__(
            self,
            master,
            name: str,
            paid: int
    ):

        self.name = name
        self.list = master

        self.state = "blank"

        tk.Frame.__init__(self, master, bg=style.LIST_COLOR)

        self.name_label = PixelSized(
            tk.Label,
            self,
            text=name,
            anchor="w",
            width=style.COL_WIDTH,
            bg=style.LIST_COLOR,
            fg=style.FG_COLOR,
            padx=style.TEXT_PADDING
        )
        self.name_label.grid(column=1, row=0)

        border = tk.Frame(self, bg=style.FG_COLOR, width=1, height=style.ROW_HEIGHT)
        border.grid(column=2, row=0)

        self.paid_label = PixelSized(
            tk.Label,
            self,
            text=f"{str(paid / 100)} kr.",
            anchor="w",
            width=style.COL_WIDTH - style.ADD_FIELD_WIDTH,
            bg=style.LIST_COLOR,
            fg=style.FG_COLOR,
            padx=style.TEXT_PADDING
        )
        self.paid_label.grid(column=3, row=0)

        # at ændre farverne på en knap er hurtigere og mere pålideligt, end at fjerne knappen
        self.add_button = PixelSized(
            tk.Button,
            self,
            command=self.show_entry_field,
            width=style.ADD_FIELD_WIDTH,
            text="+",
            bd=0,
            bg=style.LIST_COLOR,
            fg=style.FG_COLOR,
            state=tk.DISABLED,
            disabledforeground=style.LIST_COLOR,
            activebackground=style.ADD_FIELD_COLOR_HIGHLIGHT,
            activeforeground=style.FG_COLOR,
            cursor="hand2",
            highlightbackground=style.LIST_COLOR
        )
        self.add_button.grid(column=4, row=0)

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        if self.state == "blank" and self.list.state == "select":
            self.highlight()

    def on_leave(self, event):
        if self.state == "button":
            self.reset()

    def highlight(self):
        self.state = "button"

        # de her events er ikke særlig pålidelige, så jeg bliver nødt til at lave et par dobbeltsikringer
        self.list.reset_all_rows()

        self.name_label.set_bg(style.LIST_COLOR_HIGHLIGHT)
        self.paid_label.set_bg(style.LIST_COLOR_HIGHLIGHT)

        self.add_button.set_bg(style.ADD_FIELD_COLOR)
        self.add_button.inner.config(state=tk.NORMAL)

    def reset(self):
        self.state = "blank"

        self.name_label.set_bg(style.LIST_COLOR)
        self.paid_label.set_bg(style.LIST_COLOR)

        self.add_button.set_bg(style.LIST_COLOR)
        self.add_button.inner.config(state=tk.DISABLED)

    def show_entry_field(self):
        self.state = "entry"
        self.list.state = "entry"

        self.add_button.destroy()

        self.amount_entry = PixelSized(
            tk.Entry,
            self,
            width=style.ADD_FIELD_WIDTH,
            bd=0,
            bg=style.ADD_FIELD_COLOR,
            fg=style.FG_COLOR,
            insertbackground=style.FG_COLOR
        )
        self.amount_entry.grid(column=4, row=0)

        self.amount_entry.inner.insert(0, "+")
        self.amount_entry.inner.focus()

        self.amount_entry.inner.bind("<Return>", lambda e: self.deposit())

    def deposit(self):
        amount_string = self.amount_entry.inner.get()
        valid, error = fodboldtur.validate_amount(self.name, amount_string)

        if not valid:
            self.amount_entry.inner.config(fg=style.ERROR_TEXT_COLOR)
            tk.messagebox.showerror("Ugyldigt beløb", error)
            self.amount_entry.inner.config(fg=style.FG_COLOR)

        else:
            amount = round(float(amount_string) * 100)
            fodboldtur.deposit(self.name, amount)
            self.list.draw()
            self.list.state = "select"
