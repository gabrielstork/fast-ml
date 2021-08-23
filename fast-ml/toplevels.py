import tkinter as tk
import frames


class Steps(tk.Toplevel):
    def __init__(self, master, dir: str, title: str) -> None:
        super().__init__(master)

        self.title(f'Currently working with {title}')
        self.geometry('1200x700')

        self.data = frames.Data(self)
        self.data.pack(fill='both', expand=True, side='left')
        self.data.display_data(dir)

        self.algorithm = frames.Algorithm(self)
        self.algorithm.pack(fill='both', expand=True, side='left')

        self.result = frames.Result(self, dir)
        self.result.pack(fill='both', expand=True, side='left')

        self.focus_force()
        self.grab_set()
