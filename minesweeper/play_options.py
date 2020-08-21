import tkinter as tk
from tkinter import font
if __name__ == "__main__":
    from game import Game
else:
    from minesweeper.game import Game


class PlayOptions(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Set default values of height for game/window; will be changed by App class
        self.width = 700
        self.height = 700

        self.add_widgets()
    
    def add_widgets(self):
        label_font = font.Font(family='Helvetica', size=36, weight='bold')
        button_font = font.Font(family='Helvetica', size=20, weight='bold')

        # Add frame, label, and buttons for Easy difficulty
        easy_frame = tk.Frame(self)
        easy_label = tk.Label(easy_frame, text="Easy", font=label_font)
        easy_button_1 = tk.Button(easy_frame, text="8x8", command=lambda: self.start_game(9, 9, "easy"), font=button_font)
        easy_button_2 = tk.Button(easy_frame, text="9x9", command=lambda: self.start_game(9, 9, "easy"), font=button_font)
        easy_button_3 = tk.Button(easy_frame, text="10x10", command=lambda: self.start_game(10, 10, "easy"), font=button_font)
        
        easy_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        easy_label.pack(side=tk.TOP, expand=False, fill=tk.Y)
        easy_button_1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        easy_button_2.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        easy_button_3.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        # Add frame, label, and buttons for Medium difficulty
        medium_frame = tk.Frame(self)
        medium_label = tk.Label(medium_frame, text="Medium", font=label_font)
        medium_button_1 = tk.Button(medium_frame, text="13x15", command=lambda: self.start_game(15, 13, "medium"), font=button_font)
        medium_button_2 = tk.Button(medium_frame, text="16x16", command=lambda: self.start_game(16, 16, "medium"), font=button_font)
        
        medium_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        medium_label.pack(side=tk.TOP, expand=False, fill=tk.Y)
        medium_button_1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        medium_button_2.pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        # Add frame, label, and buttons for Hard difficulty
        hard_frame = tk.Frame(self)
        hard_label = tk.Label(hard_frame, text="Hard", font=label_font)
        hard_button_1 = tk.Button(hard_frame, text="30x16", command=lambda: self.start_game(16, 30, "hard"), font=button_font)
        
        hard_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        hard_label.pack(side=tk.TOP, expand=False, fill=tk.Y)
        hard_button_1.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        
    ''' Starts game with requested difficulty and grid size'''
    def start_game(self, num_rows, num_columns, difficulty):
        self.parent.destroy()
        Game(self.width, self.height, num_rows=num_rows, num_columns=num_columns, difficulty=difficulty)


if __name__ == '__main__':
    root = tk.Tk()
    PlayOptions(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()
    