import sqlite3

conn = sqlite3.connect("database.db")

c = conn.cursor()

c.execute("""CREATE TABLE employees (
    first text,
    last text,
    pay integer
    )""")

conn.commit()

conn.close()