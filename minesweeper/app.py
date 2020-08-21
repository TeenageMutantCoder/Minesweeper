import tkinter as tk
if __name__ == '__main__':
    from main_menu import MainMenu
    from play_options import PlayOptions
    from game import Game
else:
    from minesweeper.main_menu import MainMenu
    from minesweeper.play_options import PlayOptions
    from minesweeper.game import Game

class App():
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.configure_window()
        self.show_main_menu()
        self.window.mainloop()
    
    def configure_window(self):
        self.window = tk.Tk()
        self.window.title("Minesweeper")
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.minsize(300, 300)

    def show_main_menu(self):
        self.main_menu = MainMenu(self.window)
        self.main_menu.start_btn.config(command=self.show_play_options)
        self.main_menu.pack(fill=tk.BOTH, expand=True)

    def show_play_options(self):
        self.main_menu.pack_forget()
        self.play_options = PlayOptions(self.window)
        self.play_options.pack(fill=tk.BOTH, expand=True)

        # Used to set size of game to the same size as window
        self.play_options.width = self.width
        self.play_options.height = self.height


if __name__ == '__main__':
    App(700, 700)
    