import tkinter as tk


class PlayOptions(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.difficulties = {"easy": ["8x8", "9x9", "10x10"],
                        "normal": ["13x15", "16x16"],
                        "hard": ["30x16"]}
    
    def start_game(self, grid_size, difficulty):
        pass
