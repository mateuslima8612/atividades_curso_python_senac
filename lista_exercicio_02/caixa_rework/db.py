import sqlite3

con = sqlite3.connect('database.db')
cur = con.cursor()

cur.execute('CREATE TABLE IF NOT EXISTS user_database (usuario TEXT NOT NULL, password TEXT NOT NULL, saldo REAL NOT NULL)')

class CaixaOnline:
    def __init__(self, user, password, saldo):
        self.user = user
        self.password = password
        self.saldo = saldo

    @staticmethod
    def user_registration(user, password, saldo):

        cur.execute('INSERT INTO user_database (usuario, password, saldo) VALUES (?, ?, ?)', (user, password, saldo))
        con.commit()
        cur.execute('SELECT * FROM user_database WHERE (usuario, password) VALUES (?, ?)' (user, password))
        rows = cur.fetchall()
        print(rows)

    def user_login(self):
        pass

    def return_saldo(self):
        pass

    def depositar_saldo(self):
        pass
