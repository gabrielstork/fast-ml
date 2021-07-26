import tkinter as tk
from tkinter import ttk
import frames


class Root(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('FastML')
        self.geometry('350x180')
        self.resizable(0, 0)

        self.frame = frames.File(self)
        self.frame.pack(expand=True, fill='both')
