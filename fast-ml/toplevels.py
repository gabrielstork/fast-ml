import tkinter as tk
from tkinter import ttk
import frames


class Steps(tk.Toplevel):
    def __init__(self, master, dir, title):
        super().__init__(master)

        self.title(f'Currently working with {title}')
        self.geometry('805x500')
        self.resizable(0, 0)

        self.split = frames.Split(self)
        self.split.pack(fill='both', expand=True, side='left')

        self.algorithm = frames.Algorithm(self)
        self.algorithm.pack(fill='both', expand=True, side='left')

        self.result = frames.Result(self)
        self.result.pack(fill='both', expand=True, side='right')

        self.focus_force()
        self.grab_set()
