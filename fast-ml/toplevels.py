import tkinter as tk
from tkinter import ttk
import pandas as pd


class Data(tk.Toplevel):
    def __init__(self, master, dir, title):
        super().__init__(master)

        self.title(title)
        self.geometry('800x550')
        self.df = pd.read_csv(dir)

        self.focus_force()
        self.grab_set()
