import os
import toplevels
import functions
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename


LEARNING = [
    'Supervised Learning',
]

TECHNIQUES = [
    'Classification',
    'Regression',
]

ALGORITHMS = [
    'k-Nearest Neighbors (kNN)',
]


class File(tk.Frame):
    def __init__(self, master) -> None:
        super().__init__(master)

        self.label = tk.Label(self, text='FastML\nUnder Development')
        self.label.pack(fill='x', pady=40)

        self.select_button = ttk.Button(
            self, text='Choose File', command=self.choose_file
        )
        self.select_button.pack(fill='x', padx=10)

        self.about_button = ttk.Button(self, text='About')
        self.about_button.pack(fill='x', padx=10, pady=5)

    def choose_file(self) -> None:
        filetypes = (
            ('CSV files', '*.csv'),
        )

        dir = askopenfilename(title='Choose a file', filetypes=filetypes)

        if len(dir) > 0:
            toplevels.Steps(self, dir, os.path.basename(dir))


class Data(tk.LabelFrame):
    def __init__(self, master) -> None:
        super().__init__(master, text='Data')

        self.df_info = tk.Text(self, width=15, relief='solid')
        self.df_info.pack(fill='both', expand=True, padx=15, pady=15)

    def display_data(self, data: str) -> None:
        info = functions.get_data_overview(data)

        text = (
            f"Shape: {info.get('shape')}\n\n"
            f"Columns:\n{info.get('types')}\n\n"
            f"Missing Values:\n{info.get('missing')}\n\n"
            f"Duplicated Rows: {info.get('duplicated')}"
        )

        self.df_info.insert('end', text)
        self.df_info.config(state='disabled')


class Algorithm(tk.LabelFrame):
    def __init__(self, master) -> None:
        super().__init__(master, text='Algorithm')

        self.learning = ttk.Combobox(
            self, values=LEARNING, state="readonly"
        )
        self.learning.current(0)
        self.learning.pack(fill='x', padx=15, pady=5)

        self.technique = ttk.Combobox(
            self, values=TECHNIQUES, state="readonly"
        )
        self.technique.current(0)
        self.technique.pack(fill='x', padx=15, pady=5)

        self.algorithm = ttk.Combobox(
            self, values=ALGORITHMS, state="readonly"
        )
        self.algorithm.current(0)
        self.algorithm.pack(fill='x', padx=15, pady=5)


class Result(tk.LabelFrame):
    def __init__(self, master, data: str) -> None:
        super().__init__(master, text='Result')

        self.columns = ttk.Combobox(
            self, values=functions.get_columns(data), state="readonly"
        )
        self.columns.current(0)
        self.columns.pack(fill='x', padx=15, pady=5)

        self.train_button = ttk.Button(self, text='Train', width=23)
        self.train_button.pack(fill='x', padx=15, pady=5)
