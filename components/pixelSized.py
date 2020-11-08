import tkinter as tk

from components import style


# for at ting som ellers blev skaleret med text units kan skaleres med pixels
class PixelSized(tk.Frame):
    def __init__(self, sub_class, master, width: int, bg: str = None, **kwargs):

        tk.Frame.__init__(self, master, width=width, height=style.ROW_HEIGHT, bg=bg)
        self.pack_propagate(0)

        self.inner = sub_class(
            self,
            bg=bg,
            **kwargs
        )

        self.inner.pack(fill=tk.BOTH, expand=1)

    def set_bg(self, color: str):
        self.config(bg=color)
        self.inner.config(bg=color)

    def set_fg(self, color: str):
        self.inner.config(fg=color)
