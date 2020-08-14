import tkinter as tk
if __name__ == "__main__":
    from sql_connector import SqlConnector
else:
    from .sql_connector import SqlConnector


class Leaderboard(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        conn = SqlConnector()
        title = tk.Label(self, text="Leaderboard")
        scrollbar = tk.Scrollbar(self)
        scores_list = tk.Listbox(self, yscrollcommand=scrollbar.set)
        for score in conn.collect():
            scores_list.insert(tk.END, f"{score[0]} : {score[1]}")
        
        title.pack(side=tk.TOP, fill=tk.X, expand=True)
        scores_list.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    Leaderboard(root).pack(expand=True, fill=tk.BOTH)
    root.mainloop()