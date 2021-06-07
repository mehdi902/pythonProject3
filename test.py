import sqlite3
conn = sqlite3.connect('base.db')
cursor = conn.cursor()

cursor.execute("""SELECT solde FROM compte where id = 869124""")
rows = cursor.fetchone()
print(rows[0])