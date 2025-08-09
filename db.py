import sqlite3
from config import DB_PATH

def connect(): # helper funtion to open connection with the db
    return sqlite3.connect(DB_PATH) #

def init_db(): # initialize schema
    conn = connect()
    cursor = conn.cursor() # cursor to create sql commands

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER UNIQUE,
            username TEXT,
            first_name TEXT
        )
    """)

    conn.commit()
    conn.close() # save and close

def add_user(telegram_id, username, first_name):
    conn = connect()
    cursor = conn.cursor() # cursor to create sql commands

    cursor.execute("""
        INSERT OR IGNORE INTO users (telegram_id, username, first_name) 
        VALUES (?, ?, ?)
    """, (telegram_id, username, first_name)) # ignore if already exists

    conn.commit()
    conn.close()

def get_user(telegram_id): # get fn to retrieve the name for intro 
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
    user = cursor.fetchone()
    conn.close()
    return user