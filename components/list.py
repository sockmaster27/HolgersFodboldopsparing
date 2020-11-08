import tkinter as tk

import fodboldtur

from components import style
from components.row import Row
from components.pixelSized import PixelSized


class List(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master, bd=0)

        self.state = "select"

        col_names = tk.Frame(self, bg=style.LIST_COLOR_HIGHLIGHT)
        col_names.pack()

        name_label = PixelSized(
            tk.Label,
            col_names,
            text="Navn",
            anchor="w",
            width=style.COL_WIDTH,
            bg=style.PRIMARY_COLOR,
            fg=style.SEC_FG_COLOR,
            padx=style.TEXT_PADDING
        )
        name_label.grid(column=0, row=0)

        border = tk.Frame(
            col_names,
            bg=style.SEC_FG_COLOR,
            width=1,
            height=style.ROW_HEIGHT
        )
        border.grid(column=1, row=0)

        paid_label = PixelSized(
            tk.Label,
            col_names,
            text=f"Indbetalt",
            anchor="w",
            width=style.COL_WIDTH,
            bg=style.PRIMARY_COLOR,
            fg=style.SEC_FG_COLOR,
            padx=style.TEXT_PADDING
        )
        paid_label.grid(column=2, row=0)

        self.rows = []
        self.draw()

        self.bind("<Leave>", lambda e: self.reset_all_rows())

    def draw(self):
        for row in self.rows:
            row.destroy()

        items = fodboldtur.sort_by_amount(fodboldtur.paid_all(), reverse=True)

        self.rows.clear()
        for name, paid in items:
            row = Row(self, name, paid)
            self.rows.append(row)
            row.pack()

    def reset_all_rows(self):
        for row in self.rows:
            if row.state != "entry":
                row.reset()
