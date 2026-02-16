import sqlite3
import os

def create_database():

    # Put the database file next to this module so path works regardless of CWD
    base = os.path.dirname(__file__)
    db_path = os.path.join(base, 'database.db')
    conn = sqlite3.connect(db_path)
    conn.execute(""" CREATE TABLE IF NOT EXISTS preiksmeti (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prieksmets TEXT,
                    atzime TEXT
                    ); """)
    
    conn.execute(""" CREATE TABLE IF NOT EXISTS videjas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prieksmets TEXT NOT NULL,
                    atzime INTEGER NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    ); """)
    
    conn.execute(""" CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    description TEXT,
                    due_date TEXT,
                    priority TEXT DEFAULT 'normal',
                    status TEXT DEFAULT 'pending',
                    progress INTEGER DEFAULT 0,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    ); """)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()