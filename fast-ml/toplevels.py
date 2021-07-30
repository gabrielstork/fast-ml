import tkinter as tk
from tkinter import ttk
import frames


class Steps(tk.Toplevel):
    def __init__(self, master, dir, title):
        super().__init__(master)

        self.title(f'Currently working with {title}')
        self.geometry('1080x720')

        self.data = frames.Data(self)
        self.data.pack(fill='both', expand=True, side='left')
        self.data.display_data(dir)

        self.algorithm = frames.Algorithm(self)
        self.algorithm.pack(fill='both', expand=True, side='left')

        self.result = frames.Result(self)
        self.result.pack(fill='both', expand=True, side='left')

        self.focus_force()
        self.grab_set()
