import tkinter as tk


class MainMenu(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.title = tk.Label(self, text="Minesweeper")
        self.button_frame = tk.Frame(self)
        self.leaderboard_btn = tk.Button(self.button_frame, text="Show Leaderboard")
        self.start_btn = tk.Button(self.button_frame, text="Start Game")

        self.title.pack(side=tk.TOP, expand=True, fill=tk.Y)
        self.button_frame.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        self.leaderboard_btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.start_btn.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

if __name__ == "__main__":
    root = tk.Tk()
    MainMenu(root).pack(expand=True, fill=tk.BOTH)
    root.mainloop()