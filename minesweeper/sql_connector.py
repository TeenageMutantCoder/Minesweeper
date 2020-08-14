import sqlite3
import os


class SqlConnector():
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join('data', 'leaderboard.db'))
        self.c = self.conn.cursor()
        self.c.execute("CREATE TABLE IF NOT EXISTS scores (primary_key INTEGER PRIMARY KEY, score INTEGER NOT NULL, player_name text NOT NULL)")

    def collect(self):
        self.c.execute("SELECT * FROM scores ORDER BY score DESC")
        return(self.c.fetchall())

    def read(self):
        self.c.execute("SELECT * FROM scores ORDER BY score DESC")
        data = self.c.fetchall()
        for row in data:
            print(row)

    def insert(self, score, player_name):
        self.c.execute("INSERT INTO scores(score, player_name) VALUES (?, ?)", 
                       (score, player_name))
        self.commit()

    def delete(self, key):
        self.c.execute("DELETE FROM scores WHERE primary_key=?", (key,))
        self.commit()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()
    
    def _empty(self):
        self.c.execute("DELETE FROM scores")
        self.commit()