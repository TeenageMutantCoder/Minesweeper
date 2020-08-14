import tkinter as tk
from minesweeper.main_menu import MainMenu
from minesweeper.leaderboard import Leaderboard
from minesweeper.game import Game

class App(tk.Tk):
    def __init__(self, width, height):
        tk.Tk.__init__(self)
        self.width = width
        self.height = height
        self.title("Minesweeper")
        self.geometry(f"{width}x{height}")
        self.minsize(300, 300)
        self.show_main_menu()
        self.mainloop()
    
    def show_main_menu(self):
        self.main_menu = MainMenu(self)
        self.main_menu.start_btn.config(command=self.start_game)
        self.main_menu.leaderboard_btn.config(command=self.show_leaderboard)
        self.main_menu.pack(fill=tk.BOTH, expand=True)

    def show_leaderboard(self):
        self.leaderboard = Leaderboard(self)
        self.leaderboard.pack(fill=tk.BOTH, expand=True)

    def show_play_options(self):
        pass

    def start_game(self):
        Game(self.width, self.height)
        self.destroy()
    

if __name__ == "__main__":
    App(700, 700)