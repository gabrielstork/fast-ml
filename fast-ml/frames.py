import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import toplevels


SPLIT_LIST = [
    'Train-Test Split'
]

ALGORITHM_LIST = [
    'k-Nearest Neighbors (kNN)'
]


class File(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label = tk.Label(self, text='FastML\nUnder Development')
        self.label.pack(fill='x', pady=40)

        self.select_button = ttk.Button(self,
                                        text='Choose File',
                                        command=self.choose_file)
        self.select_button.pack(fill='x', padx=10)

        self.about_button = ttk.Button(self, text='About')
        self.about_button.pack(fill='x', padx=10, pady=5)

    def choose_file(self):
        filetypes = (('CSV files', '*.csv'),)
        dir = askopenfilename(title='Choose a file', filetypes=filetypes)

        if len(dir) > 0:
            toplevels.Steps(self, dir, os.path.basename(dir))


class Split(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text='Data')

        self.split = ttk.Combobox(self, values=SPLIT_LIST, state="readonly")
        self.split.current(0)
        self.split.pack(fill='x', padx=15, pady=5)


class Algorithm(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text='Algorithm')

        self.algorithm = ttk.Combobox(self, values=ALGORITHM_LIST, state="readonly")
        self.algorithm.current(0)
        self.algorithm.pack(fill='x', padx=15, pady=5)


class Result(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text='Results')

        self.train_button = ttk.Button(self, text='Train', width=23)
        self.train_button.pack(fill='x', padx=15, pady=5)
