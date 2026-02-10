import sqlite3

def create_database():

    conn = sqlite3.connect('./4tema/mlapa/database.db')
    conn.execute(""" CREATE TABLE IF NOT EXISTS preiksmeti (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prieksmets TEXT,
                    atzime TEXT
                    ); """)
    conn.commit()
    conn.close()
if __name__ == "__main__":
    create_database()