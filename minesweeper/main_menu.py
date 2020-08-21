import tkinter as tk
from tkinter import font


class MainMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        title_font = font.Font(family='Helvetica', size=72, weight='bold')
        button_font = font.Font(family='Helvetica', size=36, weight='bold')
        self.title = tk.Label(self, text="Minesweeper", font=title_font)
        self.start_btn = tk.Button(self, text="Play", font=button_font, background="gray")

        self.title.pack(side=tk.TOP, expand=True, fill=tk.Y)
        self.start_btn.pack(side=tk.TOP, expand=True, fill=tk.BOTH)


if __name__ == "__main__":
    root = tk.Tk()
    MainMenu(root).pack(expand=True, fill=tk.BOTH)
    root.mainloop()