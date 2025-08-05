import sqlite3

conn = sqlite3.connect("tokens.db")
cursor = conn.cursor()
cursor.execute("DELETE FROM tokens")
conn.commit()
print("✅ All token data deleted successfully.")

'''Tunafuta databases ambazo zimekua tayari registers'''