import sqlite3

conn = sqlite3.connect("tokens.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tokens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        meter_number TEXT,
        token TEXT,
        units INTEGER,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
conn.commit()

def save_token(meter_number, token, units):
    cursor.execute("INSERT INTO tokens (meter_number, token, units) VALUES (?, ?, ?)", 
                   (meter_number, token, units))
    conn.commit()

def get_latest_token(meter_number):
    cursor.execute("SELECT token, units, timestamp FROM tokens WHERE meter_number = ? ORDER BY id DESC LIMIT 1", 
                   (meter_number,))
    return cursor.fetchone()


def delete_token(meter_number):
    cursor.execute("DELETE FROM tokens WHERE meter_number = ?", (meter_number,))
    conn.commit()


def get_token_history(meter_number):
    cursor.execute("""
        SELECT token, units, timestamp FROM tokens
        WHERE meter_number = ?
        ORDER BY id DESC
    """, (meter_number,))
    return cursor.fetchall()


def get_token_history(meter_number):
    cursor.execute("SELECT token, units, timestamp FROM tokens WHERE meter_number = ? ORDER BY id DESC", 
                   (meter_number,))
    return cursor.fetchall()