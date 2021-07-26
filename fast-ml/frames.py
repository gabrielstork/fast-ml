import os
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import toplevels


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
            toplevels.Data(self, dir, os.path.basename(dir))
