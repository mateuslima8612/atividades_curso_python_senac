import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS usuarios(ID INTEGER NOT NULL PRIMARY KEY, usuario STRING NOT NULL, senha STRING NOT NULL)')

