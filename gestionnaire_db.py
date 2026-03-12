import sqlite3 

conn=SQLite.connect("base_de_donnee.db")
curs=conn.cursor()
curs.execute("CREATE TABLE IF NOT EXISTS user")
