import sqlite3

class Database:


    def __init__(self, name:str):
        self.name = name
    
    def execute(self, query, parameters=None):
        with sqlite3.connect(self.name) as conn:
            cur = conn.cursor()
            return cur.execute(query, parameters) if parameters else cur.execute(query)
            
    def connect(self):
        return sqlite3.connect(self.name)
