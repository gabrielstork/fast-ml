import tkinter as tk
import frames


class Root(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title('FastML')
        self.geometry('350x180')
        self.resizable(0, 0)

        self.frame = frames.File(self)
        self.frame.pack(expand=True, fill='both')
